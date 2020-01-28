import argparse
from gendiff import parsers
from gendiff import format
from gendiff.status import *


def formatter(arg_format):
    if arg_format == format.JSON:
        return format.json
    elif arg_format == format.PLAIN:
        return format.plain
    elif arg_format == format.DEFAULT:
        return format.default
    raise argparse.ArgumentTypeError(
            'Unknown formatter: {}'.format(arg_format)
    )


parser = argparse.ArgumentParser(
    description='Generate difference between two files'
)
parser.add_argument('first_file')
parser.add_argument('second_file')
parser.add_argument(
    '-f', '--format',
#   choices=format.FORMATTERS,
    default=format.DEFAULT,
    help='set format of output',
    type=formatter,
)


def _recognize_del_items(diff, before_data, after_data):
    deleted_items = {}
    deleted_keys = before_data.keys() - after_data.keys()
    for key in deleted_keys:
        deleted_items.update({key: (REMOVED, before_data[key])})
    return diff.update(deleted_items)


def _recognize_add_items(diff, before_data, after_data):
    added_items = {}
    added_keys = after_data.keys() - before_data.keys()
    for key in added_keys:
        added_items.update({key: (ADDED, after_data[key])})
    return diff.update(added_items)


def _recognize_changed_items(diff, before_data, after_data):
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
    return diff.update(changed)


def compare(before_data, after_data):
    internal_diff = {}
    for update in (_recognize_add_items,
                   _recognize_changed_items,
                   _recognize_del_items):
        update(internal_diff, before_data, after_data)
    return internal_diff


def generate_diff(before_file, after_file):
    before_file_data = parsers.get_data_from(before_file)
    after_file_data = parsers.get_data_from(after_file)
    return compare(before_file_data, after_file_data)
