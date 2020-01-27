import argparse
from gendiff import parsers
from gendiff import format


REMOVED = 'removed'
ADDED = 'added'
MODIFIED = 'modified'


def formatter(name):
    if name == format.JSON:
        return format.json
    elif name == format.PLAIN:
        return format.plain
    elif name == format.DEFAULT:
        return format.default
    raise argparse.ArgumentTypeError(
        'Unknown formatter: {}'.format(name)
    )


parser = argparse.ArgumentParser(
    description='Generate difference between two files'
)
parser.add_argument(
    '-f', '--format',
    default=format.DEFAULT,
    choices=format.FORMATTERS,
    help='set format of output',
)
parser.add_argument('first_file')
parser.add_argument('second_file')

option = parser.parse_args()
render = formatter(option.format)


def _recognize_del_items(before_data, after_data):
    deleted_items = {}
    deleted_keys = before_data.keys() - after_data.keys()
    for key in deleted_keys:
        deleted_items.update({key: (REMOVED, before_data[key])})
    return deleted_items


def _recognize_add_items(before_data, after_data):
    added_items = {}
    added_keys = after_data.keys() - before_data.keys()
    for key in added_keys:
        added_items.update({key: (ADDED, after_data[key])})
    return added_items


def _recognize_changed_items(before_data, after_data):
    changed = {}
    common_keys = before_data.keys() & after_data.keys()
    for key in common_keys:
        if (
            isinstance(before_data[key], dict) &
            isinstance(after_data[key], dict)
        ):
            changed.update(
                {
                    key: compare(
                        before_data[key],
                        after_data[key]
                    )
                }
            )
        elif before_data[key] == after_data[key]:
            changed.update({key: before_data[key]})
        else:
            changed.update(
                {
                    key: (MODIFIED, (
                        before_data[key],
                        after_data[key]
                          )
                          )
                }
            )
    return changed


def compare(before_data, after_data):
    internal_diff = {}
    deleted_items = _recognize_del_items(before_data, after_data)
    added_items = _recognize_add_items(before_data, after_data)
    changed_items = _recognize_changed_items(before_data, after_data)
    internal_diff.update(deleted_items)
    internal_diff.update(added_items)
    internal_diff.update(changed_items)
    return internal_diff


def generate_diff(before_file, after_file):
    before_file_data = parsers.get_data_from(before_file)
    after_file_data = parsers.get_data_from(after_file)
    return compare(before_file_data, after_file_data)
