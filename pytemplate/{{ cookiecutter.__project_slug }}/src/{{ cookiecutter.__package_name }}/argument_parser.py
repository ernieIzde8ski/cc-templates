#: if cookiecutter.include_bin
# pyright: reportUninitializedInstanceVariable=false
from typing import override

from tap import Tap

__all__ = ["run"]


class ArgumentParser(Tap):
    left: int
    right: int

    @override
    def configure(self) -> None:
        self.add_argument("left")
        self.add_argument("right")


def run():
    """Run the CLI."""
    from {{ cookiecutter.__package_name }} import add

    args = ArgumentParser(underscores_to_dashes=True).parse_args()
    res = add(args.left, args.right)
    print(res)
#: endif
