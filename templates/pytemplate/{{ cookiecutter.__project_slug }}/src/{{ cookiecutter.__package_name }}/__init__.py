"""{{ cookiecutter.project_description }}"""

from .info import (
    __author__,
    __copyright__,
    __credits__,
    #: if cookiecutter.license != "unlicensed"
    __license__,
    #: endif
    __maintainer__,
    __version__,
)

__all__ = [
    "__author__",
    "__copyright__",
    "__credits__",
    #: if cookiecutter.license != "unlicensed"
    "__license__",
    #: endif
    "__version__",
    "__maintainer__",
    "add",
]


def add(left: int, right: int) -> int:
    """Returns the sum of two numbers."""
    return left + right
