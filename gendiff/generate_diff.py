import argparse
import gendiff.parsers as parsers
import json


parser = argparse.ArgumentParser(
    description='Generate difference between two files'
)


def get_keys(dictionary):
    return set(dictionary.keys())


def make_diff(before, after):
    diff = {}
    aggregate_keys = set(before.keys()).union(after.keys())
    for key in aggregate_keys:
        if (
                isinstance(before.get(key), dict) &
                isinstance(after.get(key), dict)
        ):
            diff[key] = (make_diff(before.get(key), after.get(key)))
        else:
            diff.update({key: dict(
            before_value=before.get(key, 'None'),
            after_value=after.get(key, 'None')
        )})
    return diff


def render_diff():
    pass


def generate_diff(before_file, after_file):
    before = parsers.get_data_from(before_file)
    after = parsers.get_data_from(after_file)
    diff = make_diff(before, after)
    return diff
