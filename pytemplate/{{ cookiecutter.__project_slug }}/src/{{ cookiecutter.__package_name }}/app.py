#: if cookiecutter.include_bin
import typer

__all__ = ["app"]

app = typer.Typer()

@app.command()
def main(left: int, right: int):
    from {{ cookiecutter.__package_name }} import add

    print(add(left, right))

#: endif
