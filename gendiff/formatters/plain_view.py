# Templates

REMOVED = "Property '{prop}' was removed".format
ADDED = "Property '{prop}' was added with value: '{value}'".format
CHANGED = "Property '{prop}' was changed. From '{before}' to '{after}'".format


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
                    result.append(REMOVED(prop=".".join(path)))
                if value[0] == 'added':
                    if isinstance(value[1], dict):
                        result.append(ADDED(prop=".".join(path),
                                            value="complex value"))
                    else:
                        result.append(ADDED(prop=".".join(path),
                                            value=value[1]))
                if value[0] == 'modified':
                    result.append(CHANGED(
                        prop=".".join(path),
                        before=value[1][0],
                        after=value[1][1]
                    ))
            path.pop(-1)
        return "\n".join(result)
    return inner


def render(internal_diff):
    return generate_view()(internal_diff)
