INITIAL_INDENT = 0
DEFAULT_INDENT = 4
FILLER = ' '
TAMPLATE = '{}{}: {}\n'.format
BACKSHIFT = 2


def generate_view(data, indent=INITIAL_INDENT):
    def set_sign(sign=" "):
        return ''.join([
            (shift-BACKSHIFT) * FILLER,
            sign,
            FILLER]
        )

    def get_child():
        return TAMPLATE(
            set_sign(), key, generate_view(value, shift))

    def set_removed_item():
        return TAMPLATE(
            set_sign("-"), key, value[0])

    def set_removed_child():
        return TAMPLATE(
            set_sign("-"), key, generate_view(value[0], shift))

    def set_added_item():
        return TAMPLATE(
            set_sign("+"), key, value[1])

    def set_added_child():
        return TAMPLATE(
            set_sign("+"), key, generate_view(value[1], shift))

    def set_unchanged_item():
        return TAMPLATE(
            set_sign(), key, value)

    lines = ["{\n"]
    for key, value in sorted(data.items()):
        value = 'true' if str(value) == 'True' else value
        value = 'false' if str(value) == 'false' else value
        value = 'null' if str(value) == 'None' else value
        shift = indent + DEFAULT_INDENT
        if isinstance(value, dict):
            lines.append(get_child())
        elif isinstance(value, tuple):
            if value[0]:
                if isinstance(value[0], dict):
                    lines.append(set_removed_child())
                else:
                    lines.append(set_removed_item())
            if value[1]:
                if isinstance(value[1], dict):
                    lines.append(set_added_child())
                else:
                    lines.append(set_added_item())
        else:
            lines.append(set_unchanged_item())
    lines.append("{}{}".format(indent * FILLER, "}"))
    return "".join(lines)


def render(internal_diff):
    return generate_view(internal_diff)
