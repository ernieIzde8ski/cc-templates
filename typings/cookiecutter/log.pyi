"""Module for setting up logging."""

__all__ = []

from logging import Logger
from typing import Literal

from ._typeshed import StrPath

_Level = Literal["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]

LOG_LEVELS: dict[_Level, int] = ...
LOG_FORMATS: dict[_Level, str] = ...

def configure_logger(
    stream_level: _Level = "DEBUG", debug_file: StrPath | None = None
) -> Logger:
    """Configure logging for cookiecutter.

    Set up logging to stdout with given level. If ``debug_file`` is given set
    up logging to file with DEBUG level.
    """
