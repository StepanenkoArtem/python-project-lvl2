from gendiff.py_to_json import convert


INITIAL_INDENT = 0
DEFAULT_INDENT = 4
FILLER = ' '
BACKSHIFT = 2


format_line = '{}{}: {}\n'.format


def generate_view(data, indent=INITIAL_INDENT):

    def set_sign(sign=" "):
        return '{left_padding}{sign}{right_padding}'.format(
            left_padding=(shift - BACKSHIFT) * FILLER,
            sign=sign,
            right_padding=FILLER
        )
    lines = ["{\n"]
    for key, value in sorted(data.items()):
        shift = indent + DEFAULT_INDENT
        if isinstance(value, dict):
            lines.append(
                format_line(
                    set_sign(), key, generate_view(value, shift))
            )
        elif isinstance(value, tuple):
            if value[0] == 'removed':
                if isinstance(value[1], dict):
                    lines.append(format_line(
                        set_sign("-"),
                        key,
                        generate_view(value[1], shift))
                    )
                else:
                    lines.append(format_line(
                        set_sign("-"),
                        key,
                        convert(value[1]))
                    )
            if value[0] == 'added':
                if isinstance(value[1], dict):
                    lines.append(format_line(
                        set_sign("+"),
                        key,
                        generate_view(value[1], shift)
                        )
                    )
                else:
                    lines.append(format_line(
                        set_sign("+"),
                        key,
                        convert(value[1]))
                    )
            if value[0] == 'modified':
                if isinstance(value[1][0], dict):
                    lines.append(format_line(
                        set_sign("-"),
                        key,
                        generate_view(value[1][0], shift))
                    )
                else:
                    lines.append(
                        format_line(
                            set_sign("-"),
                            key,
                            convert(value[1][0]))
                    )
                if isinstance(value[1][1], dict):
                    lines.append(format_line(
                        set_sign("+"),
                        key,
                        generate_view(value[1][1], shift))
                    )
                else:
                    lines.append(
                        format_line(
                            set_sign("+"),
                            key,
                            convert(value[1][1]))
                    )
        else:
            lines.append(format_line(
                set_sign(),
                key,
                convert(value))
            )
    lines.append("{}{}".format(indent * FILLER, "}"))
    return "".join(lines)


def render(internal_diff):
    return generate_view(internal_diff)
