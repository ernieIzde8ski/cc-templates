"""
Main entry point for the `cookiecutter` command.

The code in this module is also a good example of how to use Cookiecutter as a
library rather than a script.
"""

from typing import Any

from ._typeshed import StrPath

__all__ = ["cookiecutter"]

def cookiecutter(
    template: StrPath,
    checkout: str | None = None,
    no_input: bool = False,
    extra_context: dict[str, Any] | None = None,
    replay: bool | None = None,
    overwrite_if_exists: bool = False,
    output_dir: StrPath = ".",
    config_file: StrPath | None = None,
    default_config: bool = True,
    password: str | None = None,
    directory: StrPath | None = None,
    skip_if_file_exists: bool = False,
    accept_hooks: bool = True,
    keep_project_on_failure: bool = True,
) -> str:
    """
    Run Cookiecutter just as if using it from the command line.

    :param template: A directory containing a project template directory,
        or a URL to a git repository.
    :param checkout: The branch, tag or commit ID to checkout after clone.
    :param no_input: Do not prompt for user input.
        Use default values for template parameters taken from `cookiecutter.json`, user
        config and `extra_dict`. Force a refresh of cached resources.
    :param extra_context: A dictionary of context that overrides default
        and user configuration.
    :param replay: Do not prompt for input, instead read from saved json. If
        ``True`` read from the ``replay_dir``.
        if it exists
    :param overwrite_if_exists: Overwrite the contents of the output directory
        if it exists.
    :param output_dir: Where to output the generated project dir into.
    :param config_file: User configuration file path.
    :param default_config: Use default values rather than a config file.
    :param password: The password to use when extracting the repository.
    :param directory: Relative path to a cookiecutter template in a repository.
    :param skip_if_file_exists: Skip the files in the corresponding directories
        if they already exist.
    :param accept_hooks: Accept pre and post hooks if set to `True`.
    :param keep_project_on_failure: If `True` keep generated project directory even when
        generation fails
    """
