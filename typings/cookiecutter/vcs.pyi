"""
This type stub file was generated by pyright.
"""

import os
from typing import Optional

"""Helper functions for working with version control systems."""
logger = ...
BRANCH_ERRORS = ...

def identify_repo(
    repo_url,
) -> tuple[Any, Any] | tuple[Literal["git"], Any] | tuple[Literal["hg"], Any]:
    """Determine if `repo_url` should be treated as a URL to a git or hg repo.

    Repos can be identified by prepending "hg+" or "git+" to the repo URL.

    :param repo_url: Repo URL of unknown type.
    :returns: ('git', repo_url), ('hg', repo_url), or None.
    """
    ...

def is_vcs_installed(repo_type) -> bool:
    """
    Check if the version control system for a repo type is installed.

    :param repo_type:
    """
    ...

def clone(
    repo_url: str,
    checkout: Optional[str] = ...,
    clone_to_dir: os.PathLike[str] = ...,
    no_input: bool = ...,
) -> str:
    """Clone a repo to the current directory.

    :param repo_url: Repo URL of unknown type.
    :param checkout: The branch, tag or commit ID to checkout after clone.
    :param clone_to_dir: The directory to clone to.
                         Defaults to the current directory.
    :param no_input: Do not prompt for user input and eventually force a refresh of
        cached resources.
    :returns: str with path to the new directory of the repository.
    """
    ...
