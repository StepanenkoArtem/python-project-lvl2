# Templates

REMOVED = "Property '{prop}' was removed"
ADDED = "Property '{prop}' was added with value: '{value}'"
CHANGED = "Property '{prop}' was changed. From '{before}' to '{after}'"

COMPLEX = "complex value"


def convert(value):
    value = 'null' if value is None else value
    value = 'true' if value is True else value
    value = 'false' if value is False else value
    return value


def generate_view():
    result = []
    path = []

    def inner(data):
        for key, value in data.items():
            path.append(key)
            if isinstance(value, dict):
                inner(value)
            elif isinstance(value, tuple):
                if value[0] == 'removed':
                    result.append(REMOVED.format(prop=".".join(path)))
                if value[0] == 'added':
                    if isinstance(value[1], dict):
                        result.append(
                            ADDED.format(prop=".".join(path),
                                         value=COMPLEX))
                    else:
                        result.append(
                            ADDED.format(prop=".".join(path),
                                         value=convert(value[1])))
                if value[0] == 'modified':
                    result.append(
                        CHANGED.format(
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
