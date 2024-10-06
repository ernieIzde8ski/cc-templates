import json
import logging
import os
import subprocess
from collections.abc import Callable, Iterator
from contextlib import AbstractContextManager
from functools import wraps
from pathlib import Path
from typing import Any, LiteralString, Self, override

import pytest
from cookiecutter.main import cookiecutter


class RemovableList[T](list[T]):
    def remove_by[U](self, func: Callable[[T], bool]) -> T:
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


class cwd(AbstractContextManager["cwd"]):
    def __init__(self, origin_path: Path, target_path: Path):
        self.origin_path = origin_path
        self.target_path = target_path

    @override
    def __enter__(self) -> Self:  # pyright: ignore[reportMissingSuperCall]
        os.chdir(self.target_path)
        return self

    @override
    def __exit__(self, *args: Any) -> None:  # pyright: ignore[reportAny]
        os.chdir(self.origin_path)


@pytest.mark.parametrize("template", TEMPLATES.use("pytemplate"))
def test_templates(template: Path, tmp_path: Path) -> None:
    pwd = Path.cwd()
    print(tmp_path)

    with cwd(pwd, tmp_path):
        extra_content: dict[str, Any] | None
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
