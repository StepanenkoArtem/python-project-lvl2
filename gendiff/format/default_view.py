from gendiff.py_to_json import convert
from gendiff.diff import ADDED, REMOVED, MODIFIED

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
    end_wrapper = "{}{}".format(indent * _FILLER, "}")

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
        if isinstance(_value, dict):
            format_line(generate_view(_value, shift), sign)
        else:
            format_line(convert(_value), sign)

    def set_sign_for_lines(_value):
        status, param = _value
        if status == REMOVED:
            add_line(param, _REM_SIGN)
        if status == ADDED:
            add_line(param, _ADD_SIGN)
        if status == MODIFIED:
            add_line(param[0], _REM_SIGN)
            add_line(param[1], _ADD_SIGN)

    for key, value in sorted(data.items()):
        shift = indent + _DEFAULT_INDENT
        if isinstance(value, dict):
            format_line(generate_view(value, shift))
        elif isinstance(value, tuple):
            set_sign_for_lines(value)
        else:
            format_line(convert(value))
    lines.append(end_wrapper)
    return "".join(lines)


def render(internal_diff):
    return generate_view(internal_diff)
