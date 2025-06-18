#: if cookiecutter.module_type == "bin"
import typer

__all__ = ["app"]

app = typer.Typer()

@app.command()
def main(left: int, right: int):
    from {{ cookiecutter.package_name }} import add

    print(add(left, right))

#: endif
