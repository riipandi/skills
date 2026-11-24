import json
from pathlib import Path

import handlers

ROUTES = json.loads((Path(__file__).parent / "routes.json").read_text())


def dispatch(name, payload):
    return getattr(handlers, ROUTES[name])(payload)


if __name__ == "__main__":
    for route in ROUTES:
        dispatch(route, 1)
    print("ok")
