from gendiff.py_to_json import convert
from gendiff.status import *

# Indentation settings
_INITIAL_INDENT = 0
_DEFAULT_INDENT = 4
_FILLER = ' '
_BACKSHIFT = 2

_LINE_TEMPLATE = '{sign}{key}: {value}\n'

# Tokens
_ADD_SIGN = '+'
_REM_SIGN = '-'


def generate_view(data, indent=_INITIAL_INDENT):
    lines = ["{\n"]

    def format_line(_value, sign=" "):
        formatted_sign = '{left}{sign}{right}'.format(
            left=(shift - _BACKSHIFT) * _FILLER,
            sign=sign,
            right=_FILLER
        )
        line = _LINE_TEMPLATE.format(
            sign=formatted_sign,
            key=key,
            value=_value
        )
        return lines.append(line)

    def add_line(_value, sign):
        if isinstance(value, dict):
            format_line(generate_view(_value, shift), sign)
        else:
            format_line(convert(_value), sign)

    for key, param in sorted(data.items()):
        shift = indent + _DEFAULT_INDENT
        if isinstance(param, dict):
            format_line(generate_view(param, shift))
        elif isinstance(param, tuple):
            status, value = param
            if status == REMOVED:
                add_line(value, _REM_SIGN)
            if status == ADDED:
                add_line(value, _ADD_SIGN)
            if status == MODIFIED:
                value_before = value[0]
                value_after = value[1]
                add_line(value_before, _REM_SIGN)
                add_line(value_after, _ADD_SIGN)
        else:
            format_line(convert(param))
    lines.append("{}{}".format(indent * _FILLER, "}"))
    return "".join(lines)


def render(internal_diff):
    return generate_view(internal_diff)
