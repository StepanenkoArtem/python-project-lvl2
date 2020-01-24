INITIAL_INDENT = 0
DEFAULT_INDENT = 4
FILLER = ' '
TAMPLATE = '{}{}: {}\n'.format
BACKSHIFT = 2


def convert(value):
    value = 'null' if str(value) == 'None' else value
    value = 'true' if str(value) == 'True' else value
    value = 'false' if str(value) == 'False' else value
    return value


def generate_view(data, indent=INITIAL_INDENT):

    def set_sign(sign=" "):
        return ''.join([
            (shift - BACKSHIFT) * FILLER,
            sign,
            FILLER]
        )
    lines = ["{\n"]
    for key, value in sorted(data.items()):
        shift = indent + DEFAULT_INDENT
        if isinstance(value, dict):
            lines.append(
                TAMPLATE(
                    set_sign(), key, generate_view(value, shift))
            )
        elif isinstance(value, tuple):
            if value[0] == 'removed':
                if isinstance(value[1], dict):
                    lines.append(TAMPLATE(
                        set_sign("-"),
                        key,
                        generate_view(value[1], shift))
                    )
                else:
                    lines.append(TAMPLATE(
                        set_sign("-"),
                        key,
                        convert(value[1]))
                    )
            if value[0] == 'added':
                if isinstance(value[1], dict):
                    lines.append(TAMPLATE(
                        set_sign("+"),
                        key,
                        generate_view(value[1], shift)
                        )
                    )
                else:
                    lines.append(TAMPLATE(
                        set_sign("+"),
                        key,
                        convert(value[1]))
                    )
            if value[0] == 'modified':
                if isinstance(value[1][0], dict):
                    lines.append(TAMPLATE(
                        set_sign("-"),
                        key,
                        generate_view(value[1][0], shift))
                    )
                else:
                    lines.append(
                        TAMPLATE(
                            set_sign("-"),
                            key,
                            convert(value[1][0]))
                    )
                if isinstance(value[1][1], dict):
                    lines.append(TAMPLATE(
                        set_sign("+"),
                        key,
                        generate_view(value[1][1], shift))
                    )
                else:
                    lines.append(
                        TAMPLATE(
                            set_sign("+"),
                            key,
                            convert(value[1][1]))
                    )
        else:
            lines.append(TAMPLATE(
                set_sign(),
                key,
                convert(value))
            )
    lines.append("{}{}".format(indent * FILLER, "}"))
    return "".join(lines)


def render(internal_diff):
    return generate_view(internal_diff)
