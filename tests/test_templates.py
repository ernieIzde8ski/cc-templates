import json
import logging
import os
import subprocess
from collections.abc import Callable, Iterator
from contextlib import AbstractContextManager
from functools import wraps
from pathlib import Path
from typing import LiteralString, Self, final, override

import pytest
from cookiecutter.main import cookiecutter


class RemovableList[T](list[T]):
    def remove_by(self, func: Callable[[T], bool]) -> T:
        for n, item in enumerate(self):
            if func(item):
                break
        else:
            raise StopIteration
        return self.pop(n)


def generator_to_list[**P, T](callable: Callable[P, Iterator[T]]) -> Callable[P, list[T]]:
    @wraps(callable)
    def to_list(*args: P.args, **kwargs: P.kwargs):
        return list(callable(*args, **kwargs))

    return to_list


class Templates(list[Path]):
    """List of all template directories."""

    def __init__(self, template_dir: Path) -> None:
        super().__init__()

        for path in template_dir.iterdir():
            if path.is_dir():
                if (path / "cookiecutter.json").exists():
                    self.append(path)
                else:
                    logging.warning(
                        f"Path {path} is in the template directory, "
                        "but doesn't appear to be a template directory."
                    )

    @generator_to_list
    def use(self, *names: LiteralString) -> Iterator[Path]:
        for name in names:
            for path in list(self):
                if path.name == name:
                    yield path
                    self.remove(path)
                    break
            else:
                raise RuntimeError(
                    f"Path {name=} does not have a matching directory.\n"
                    f"Available directories: {self}"
                )


_this_file = Path(__file__)
_root_directory = _this_file.parent.parent
_template_directory = _root_directory / "templates"

TEMPLATES = Templates(_template_directory)


@final
class cwd(AbstractContextManager["cwd"]):
    """
    Update chdir to a target path while this context manager is open.
    """

    def __init__(self, target_path: Path):
        self.origin_path = Path.cwd()
        self.target_path = target_path.resolve()

    @override
    def __enter__(self) -> Self:  # pyright: ignore[reportMissingSuperCall]
        os.chdir(self.target_path)
        return self

    @override
    def __exit__(self, *args: object) -> None:
        os.chdir(self.origin_path)


@pytest.mark.parametrize("template", TEMPLATES.use("pytemplate", "rstemplate"))
def test_templates(template: Path, tmp_path: Path) -> None:
    print(tmp_path)

    with cwd(tmp_path):
        extra_content: dict[str, object] | None
        extra_context_path = template / "test_defaults.json"

        if extra_context_path.exists():
            extra_content = json.loads(extra_context_path.read_text())
        else:
            extra_content = None

        resulting_directory = cookiecutter(
            str(template), extra_context=extra_content, no_input=True
        )

        os.chdir(resulting_directory)
        _ = subprocess.check_output(["pre-commit", "run", "--all"])


def test_all_templates_accounted_for():
    assert len(TEMPLATES) == 0, "Some templates are not being tested: {TEMPLATES}"
