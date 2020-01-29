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


def _get_removed_items(diff, before_data, after_data):
    removed_items = {}
    removed_keys = before_data.keys() - after_data.keys()
    for key in removed_keys:
        removed_items.update({key: (REMOVED, before_data[key])})
    return diff.update(removed_items)


def _get_added_items(diff, before_data, after_data):
    added_items = {}
    added_keys = after_data.keys() - before_data.keys()
    for key in added_keys:
        added_items.update({key: (ADDED, after_data[key])})
    return diff.update(added_items)


def _get_modified_items(diff, before_data, after_data):
    changed = {}
    common_keys = before_data.keys() & after_data.keys()
    for key in common_keys:
        item_before = before_data[key]
        item_after = after_data[key]
        if (
            isinstance(item_before, dict) &
            isinstance(item_after, dict)
        ):
            compared = compare(
                 item_before,
                 item_after
            )
        elif item_before == item_after:
            compared = item_before
        else:
            compared = (MODIFIED, (
                item_before,
                item_after)
                    )
        changed[key] = compared
    return diff.update(changed)


def compare(before_data, after_data):
    internal_diff = {}
    for update in (_get_added_items,
                   _get_modified_items,
                   _get_removed_items):
        update(internal_diff, before_data, after_data)
    return internal_diff


def generate_diff(before_file, after_file):
    before_file_data = parsers.get_data_from(before_file)
    after_file_data = parsers.get_data_from(after_file)
    return compare(before_file_data, after_file_data)
