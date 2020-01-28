import json


def render(internal_diff):
    return json.dumps(internal_diff, indent=4)
