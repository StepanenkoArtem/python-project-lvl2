from gendiff.py_to_json import convert
from gendiff import status

REMOVED = "Property '{prop}' was removed"
ADDED = "Property '{prop}' was added with value: '{value}'"
MODIFIED = "Property '{prop}' was changed. From '{before}' to '{after}'"
COMPLEX = "complex value"


def generate_view():
    result = []
    path = []

    def inner(data):
        for key, value in data.items():
            path.append(key)
            if isinstance(value, dict):
                inner(value)
            elif isinstance(value, tuple):
                if value[0] == status.REMOVED:
                    result.append(
                        REMOVED.format(
                            prop=".".join(path)))
                if value[0] == status.ADDED:
                    if isinstance(value[1], dict):
                        result.append(
                            ADDED.format(
                                prop=".".join(path),
                                value=COMPLEX))
                    else:
                        result.append(
                            ADDED.format(
                                prop=".".join(path),
                                value=convert(value[1])))
                if value[0] == status.MODIFIED:
                    result.append(
                        MODIFIED.format(
                            prop=".".join(path),
                            before=convert(value[1][0]),
                            after=convert(value[1][1])
                        )
                    )
            path.pop(-1)
        return "\n".join(result)
    return inner


def render(internal_diff):
    return generate_view()(internal_diff)
