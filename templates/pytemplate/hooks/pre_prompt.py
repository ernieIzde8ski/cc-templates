import json
import sys
from functools import partial

println = print
print = partial(print, end=None)
eprintln = partial(println, file=sys.stderr)
eprint = partial(println, file=sys.stderr, end=None)

try:
    import yaml
except ModuleNotFoundError:
    eprintln("ERROR: `pyyaml` not found.")
    sys.exit(1)

SOURCE = "cookiecutter.yaml"
TARGET = "cookiecutter.json"

if __name__ == "__main__":
    with open(SOURCE) as source, open(TARGET, "w+") as target:
        obj: object = yaml.full_load(source)  # pyright: ignore[reportAny]
        json.dump(obj, target)
