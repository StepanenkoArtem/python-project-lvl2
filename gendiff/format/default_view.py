from gendiff.py_to_json import convert
from gendiff.status import *

# Indentation settings
INITIAL_INDENT = 0
DEFAULT_INDENT = 4
FILLER = ' '
BACKSHIFT = 2

format_line = '{sign}{key}: {value}\n'.format


def generate_view(data, indent=INITIAL_INDENT):
    lines = ["{\n"]

    def add_line(_value, sign=" "):
        left = (shift - BACKSHIFT) * FILLER
        right = FILLER
        formatted_sign = '{}{}{}'.format(left, sign, right)
        line = format_line(
            sign=formatted_sign,
            key=key,
            value=_value
        )
        return lines.append(line)

    for key, param in sorted(data.items()):
        shift = indent + DEFAULT_INDENT
        if isinstance(param, dict):
            add_line(
                _value=generate_view(param, shift)
            )
        elif isinstance(param, tuple):
            status, value = param
            if status == REMOVED:
                if isinstance(value, dict):
                    add_line(
                        _value=generate_view(value, shift),
                        sign="-"
                    )
                else:
                    add_line(
                        _value=convert(value),
                        sign="-"
                    )
            if status == ADDED:
                if isinstance(value, dict):
                    add_line(
                        _value=generate_view(value, shift),
                        sign="+"
                    )
                else:
                    add_line(
                        _value=convert(value),
                        sign="+"
                    )
            if status == MODIFIED:
                value_before = value[0]
                value_after = value[1]
                if isinstance(value_before, dict):
                    add_line(
                        _value=generate_view(value_before, shift),
                        sign="-"
                    )
                else:
                    add_line(
                        _value=convert(value_before),
                        sign="-"
                    )
                if isinstance(value_after, dict):
                    add_line(
                        _value=generate_view(value_after, shift),
                        sign="+"
                    )
                else:
                    add_line(
                        _value=convert(value_after),
                        sign="+"
                    )
        else:
            add_line(
                _value=convert(param)
            )
    lines.append("{}{}".format(indent * FILLER, "}"))
    return "".join(lines)


def render(internal_diff):
    return generate_view(internal_diff)
