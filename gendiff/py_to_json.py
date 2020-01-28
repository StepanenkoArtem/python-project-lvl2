def convert(value):
    value = 'null' if value is None else value
    value = 'true' if value is True else value
    value = 'false' if value is False else value
    return value
