import re
from collections.abc import Callable
from typing import ClassVar, Literal

from cookiecutter.utils import simple_filter
from jinja2 import Environment
from jinja2.ext import Extension

type ModuleKind = Literal["bin", "lib", "stub"]


class FunctionRegistry[Fn: Callable[..., object]](dict[str, Fn]):
    def register(self, fn: Fn) -> Fn:
        """Intended for usage as a decorator."""
        self[fn.__name__] = fn
        return fn


type FilterRegistry = FunctionRegistry[Callable[..., object]]


class SimpleFilters(Extension):
    type Fn = Callable[..., object]
    _simple_filters: ClassVar[FilterRegistry] = FunctionRegistry()
    filter = _simple_filters.register

    ########################
    ########################

    @filter
    @staticmethod
    def guess_mkind(display_name: str) -> ModuleKind:
        """
        Guesses a module kind.

        >>> SimpleFilters.guess_mkind("foobar-stubs")
        'stub'
        """
        # TODO: Configure these doctests to work automagically
        if re.search(r"(?i)-stubs?$", display_name):
            return "stub"
        if re.match(r"(?:\w|[_])+", display_name):
            return "lib"
        return "bin"

    @filter
    @staticmethod
    def guess_pypi_name(display_name: str, module_type: ModuleKind = "bin") -> object:
        res: str

        match module_type:
            case "bin":
                res = display_name.lower().replace(" ", "-")
            case "lib":
                res = display_name.lower().replace(" ", "_")
            case "stub":
                res = display_name.replace(" ", "-")
                if res.endswith("-stub"):
                    res += "s"
                elif not res.endswith("-stubs"):
                    res += "-stubs"

        res = re.sub(r"[^\w._-]", "", res)
        return res

    @filter
    @staticmethod
    def zap_suffix(__s: str, suffix: str):
        return __s.removesuffix(suffix)


    ########################
    ########################

    def __init__(self, environment: Environment):
        super().__init__(environment)
        for name, func in self._simple_filters.items():
            _ = environment.filters.setdefault(name, func)
