from gendiff.py_to_json import convert
from gendiff.status import *

# Line Templates
REMOVED_LINE = "Property '{prop}' was removed"
ADDED_LINE = "Property '{prop}' was added with value: '{value}'"
MODIFIED_LINE = "Property '{prop}' was changed. From '{before}' to '{after}'"
COMPLEX = "complex value"


def generate_view():
    result = []
    path = []

    def append_removed_line():
        result.append(REMOVED_LINE.format(prop=".".join(path)))

    def append_added_line(line):
        result.append(
            ADDED_LINE.format(
                prop=".".join(path),
                value=line))

    def append_modified_line(value_before, value_after):
        result.append(
            MODIFIED_LINE.format(
                prop=".".join(path),
                before=convert(value_before),
                after=convert(value_after)
            )
        )

    def tuplied(param):
        status, value = param
        if status == REMOVED:
            append_removed_line()
        if status == ADDED:
            if isinstance(value, dict):
                append_added_line(COMPLEX)
            else:
                append_added_line(convert(value))
        if status == MODIFIED:
            append_modified_line(
                value_before=value[0],
                value_after=value[1]
            )

    def inner(data):
        for key, param in data.items():
            path.append(key)
            if isinstance(param, dict):
                inner(param)
            elif isinstance(param, tuple):
                tuplied(param)
            path.pop(-1)
        return "\n".join(result)
    return inner


def render(internal_diff):
    return generate_view()(internal_diff)
