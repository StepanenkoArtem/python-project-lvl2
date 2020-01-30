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
    default=format.DEFAULT,
    help='set format of output',
    type=formatter,
)


def _get_diff_items(minuend, subtrahend, status):
    deff_items = {}
    diff_item_keys = minuend.keys() - subtrahend.keys()
    for key in diff_item_keys:
        deff_items.update({key: (status, minuend[key])})
    return deff_items


def _get_modified_items(before_data, after_data):
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
    return changed


def compare(before_data, after_data):
    internal_diff = {}
    internal_diff.update(_get_diff_items(before_data, after_data, REMOVED))
    internal_diff.update(_get_diff_items(after_data, before_data, ADDED))
    internal_diff.update(_get_modified_items(before_data, after_data))
    return internal_diff


def generate_diff(before_file, after_file):
    before_file_data = parsers.get_data_from(before_file)
    after_file_data = parsers.get_data_from(after_file)
    return compare(before_file_data, after_file_data)
