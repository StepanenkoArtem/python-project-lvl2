def render_yaml(diff):
    return diff


def is_key_added(key):
    return (key[0] is None) & bool(key[1])


def is_key_deleted(key):
    return (key[1] is None) & bool(key[0])


def is_key_changed(key):
    return key[0] != key[1]


def render_json(diff):
    result = ""
    return result


def render(diff, view):
    if view == 'yaml':
        return render_yaml(diff)
    return print(render_json(diff))
