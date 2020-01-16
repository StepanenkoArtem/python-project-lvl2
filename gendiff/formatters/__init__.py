from gendiff.formatters import default_view
from gendiff.formatters import json_view
from gendiff.formatters import plain_view


FORMATS = {
    "plain": plain_view.render,
    "json": json_view.render,
    "default": default_view.render,
}

get_formatter = FORMATS.get
