""" {{ cookiecutter.project_description }} """

__author__ = "{{ cookiecutter.author_name }}"
__copyright__ = "Copyright {{ cookiecutter.copyright_year }}, {{ cookiecutter.author_name }}"
__credits__ = ["{{ cookiecutter.author_name }}"]
#: if cookiecutter.license != "unlicensed"
__license__ = "{{ cookiecutter.license }}"
#: endif
__version__ = "{{ cookiecutter.initial_version }}"
__maintainer__ = "{{ cookiecutter.author_name }}"

__all__ = ["add"]

def add(left: int, right: int) -> int:
    """Returns the sum of two numbers."""
    return left + right
