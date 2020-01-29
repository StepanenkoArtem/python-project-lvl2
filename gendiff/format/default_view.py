from gendiff.py_to_json import convert
from gendiff.status import *

# Indentation settings
_INITIAL_INDENT = 0
_DEFAULT_INDENT = 4
_FILLER = ' '
_BACKSHIFT = 2

# Tokens
_ADD = '+'
_REM = '-'


def generate_view(data, indent=_INITIAL_INDENT):
    format_line = '{sign}{key}: {value}\n'.format
    lines = ["{\n"]

    def add_line(_value, sign=" "):
        left = (shift - _BACKSHIFT) * _FILLER
        right = _FILLER
        formatted_sign = '{}{}{}'.format(left, sign, right)
        line = format_line(
            sign=formatted_sign,
            key=key,
            value=_value
        )
        return lines.append(line)

    for key, param in sorted(data.items()):
        shift = indent + _DEFAULT_INDENT
        if isinstance(param, dict):
            add_line(generate_view(param, shift))
        elif isinstance(param, tuple):
            status, value = param
            if status == REMOVED:
                if isinstance(value, dict):
                    add_line(generate_view(value, shift), _REM)
                else:
                    add_line(convert(value), _REM)
            if status == ADDED:
                if isinstance(value, dict):
                    add_line(generate_view(value, shift), _ADD)
                else:
                    add_line(convert(value), _ADD)
            if status == MODIFIED:
                value_before = value[0]
                value_after = value[1]
                if isinstance(value_before, dict):
                    add_line(generate_view(value_before, shift), _REM)
                else:
                    add_line(convert(value_before), _REM)
                if isinstance(value_after, dict):
                    add_line(generate_view(value_after, shift), _ADD)
                else:
                    add_line(convert(value_after), _ADD)
        else:
            add_line(
                _value=convert(param)
            )
    lines.append("{}{}".format(indent * _FILLER, "}"))
    return "".join(lines)


def render(internal_diff):
    return generate_view(internal_diff)
