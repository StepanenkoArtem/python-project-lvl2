import json


def json_formatter(renderer):
    def wrapper(inner_diff):
        print("A\n")
        print(renderer(inner_diff))
        print("\nB")
    return wrapper


@json_formatter
def render(diff):
    s = json.dumps(diff, indent=4, sort_keys=True)
    return s
