# {{ cookiecutter.display_name }}

{{ cookiecutter.project_description }}

## Development


#:if cookiecutter.packaging

This project uses [`pre-commit`](https://pre-commit.com) for linting purposes
and `make` for compilation purposes. See [`Makefile`](./Makefile) for available
rules.

#:else

This project uses [`pre-commit`](https://pre-commit.com) for linting purposes.

#:  if cookiecutter.module_type == "bin"
The binary can be installed locally via `pipx install [-e] .`.
#:  endif

#:endif
