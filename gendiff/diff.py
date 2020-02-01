
from gendiff import parsers
from gendiff import status_list


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
            compared = (status_list.MODIFIED, (
                item_before,
                item_after)
                    )
        changed[key] = compared
    return changed


def compare(before_data, after_data):
    internal_diff = {}
    internal_diff.update(
        _get_diff_items(before_data, after_data, status_list.REMOVED))
    internal_diff.update(
        _get_diff_items(after_data, before_data, status_list.ADDED))
    internal_diff.update(_get_modified_items(before_data, after_data))
    return internal_diff


def generate_diff(before_file, after_file):
    before_file_data = parsers.get_data_from(before_file)
    after_file_data = parsers.get_data_from(after_file)
    return compare(before_file_data, after_file_data)
