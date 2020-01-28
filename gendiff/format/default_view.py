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

    def add_line(_value, _sign=" "):
        left = (shift - BACKSHIFT) * FILLER
        right = FILLER
        sign = '{}{}{}'.format(left, _sign, right)
        line = format_line(
            sign=sign,
            key=key,
            value=_value
        )
        return lines.append(line)

    for key, value in sorted(data.items()):
        shift = indent + DEFAULT_INDENT
        if isinstance(value, dict):
            add_line(
                _value=generate_view(value, shift),
                _sign=" "
            )
        elif isinstance(value, tuple):
            status, param = value
            if status == REMOVED:
                if isinstance(param, dict):
                    add_line(
                        _value=generate_view(param, shift),
                        _sign="-"
                    )
                else:
                    add_line(
                        _value=convert(param),
                        _sign="-"
                    )
            if status == ADDED:
                if isinstance(param, dict):
                    add_line(
                        _value=generate_view(param, shift),
                        _sign="+"
                    )
                else:
                    add_line(
                        _value=convert(param),
                        _sign="+"
                    )
            if status == MODIFIED:
                if isinstance(param[0], dict):
                    add_line(
                        _value=generate_view(param[0], shift),
                        _sign="-"
                    )
                else:
                    add_line(
                        _value=convert(param[0]),
                        _sign="-"
                    )
                if isinstance(param[1], dict):
                    add_line(
                        _value=generate_view(param[1], shift),
                        _sign="+"
                    )
                else:
                    add_line(
                        _value=convert(param[1]),
                        _sign="+"
                    )
        else:
            add_line(
                _value=convert(value),
                _sign=" "
            )
    lines.append("{}{}".format(indent * FILLER, "}"))
    return "".join(lines)


def render(internal_diff):
    return generate_view(internal_diff)
