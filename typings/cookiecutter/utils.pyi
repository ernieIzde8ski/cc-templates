"""
This type stub file was generated by pyright.
"""

import contextlib
import os
from pathlib import Path
from typing import Dict

from jinja2.ext import Extension

"""Helper functions used throughout Cookiecutter."""
logger = ...

def force_delete(func, path, exc_info) -> None:
    """Error handler for `shutil.rmtree()` equivalent to `rm -rf`.

    Usage: `shutil.rmtree(path, onerror=force_delete)`
    From https://docs.python.org/3/library/shutil.html#rmtree-example
    """
    ...

def rmtree(path) -> None:
    """Remove a directory and all its contents. Like rm -rf on Unix.

    :param path: A directory path.
    """
    ...

def make_sure_path_exists(path: os.PathLike[str]) -> None:
    """Ensure that a directory exists.

    :param path: A directory tree path for creation.
    """
    ...

@contextlib.contextmanager
def work_in(dirname=...) -> Generator[None, Any, None]:
    """Context manager version of os.chdir.

    When exited, returns to the working directory prior to entering.
    """
    ...

def make_executable(script_path) -> None:
    """Make `script_path` executable.

    :param script_path: The file to change
    """
    ...

def simple_filter(filter_function) -> type[SimpleFilterExtension]:
    """Decorate a function to wrap it in a simplified jinja2 extension."""

    class SimpleFilterExtension(Extension): ...

def create_tmp_repo_dir(repo_dir: os.PathLike[str]) -> Path:
    """Create a temporary dir with a copy of the contents of repo_dir."""
    ...

def create_env_with_context(context: Dict) -> StrictEnvironment:
    """Create a jinja environment using the provided context."""
    ...
