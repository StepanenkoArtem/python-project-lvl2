from gendiff.format.default_view import render as default
from gendiff.format.json_view import render as json
from gendiff.format.plain_view import render as plain


FORMATTERS = (JSON, PLAIN, DEFAULT) = (
    'json', 'plain', 'default'
)
