import argparse
import gendiff.parsers as parsers


parser = argparse.ArgumentParser(
    description='Generate difference between two files'
)


def get_keys(dictionary):
    return set(dictionary.keys())


def recognize_del_items(before_data, after_data):
    deleted_items = {}
    deleted_keys = before_data.keys() - after_data.keys()
    for key in deleted_keys:
        deleted_items.update({key: {"deleted": before_data[key]}})
    return deleted_items


def recognize_add_items(before_data, after_data):
    added_items = {}
    added_keys = after_data.keys() - before_data.keys()
    for key in added_keys:
        added_items.update({key: {"added": after_data[key]}})
    return added_items


def recognize_changed_items(before_data, after_data):
    changed = {}
    common_keys = before_data.keys() & after_data.keys()
    for key in common_keys:
        if (
            isinstance(before_data[key], dict) &
            isinstance(after_data[key], dict)
        ):
            changed.update(
                {
                    key: build_inner_diff(
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
                    key: {
                        "deleted": before_data[key],
                        "added": after_data[key],
                    }
                }
            )
    return changed


def build_inner_diff(before_data, after_data):
    inner_diff = {}
    deleted_items = recognize_del_items(before_data, after_data)
    added_items = recognize_add_items(before_data, after_data)
    changed_items = recognize_changed_items(before_data, after_data)
    inner_diff.update(deleted_items)
    inner_diff.update(added_items)
    inner_diff.update(changed_items)
    return inner_diff


def generate_diff(before_file, after_file):
    before_file_data = parsers.get_data_from(before_file)
    after_file_data = parsers.get_data_from(after_file)
    return build_inner_diff(before_file_data, after_file_data)
