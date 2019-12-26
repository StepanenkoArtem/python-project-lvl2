import argparse
import os
import json


parser = argparse.ArgumentParser(
    description='Generate difference between two files'
)


def get_keys(dictionary):
    return set(dictionary.keys())


def append_to_result(key, value, sign=" "):
    return '{sign} {key}: {value}\n'.format(sign=sign, key=key, value=value)


def get_path(path):
    if "~" in path:
        path = os.path.expanduser(path)
    path = os.path.abspath(os.path.normpath(path))
    print(path)
    return path


def generate_diff(before_file, after_file):
    diff = ""
    before = json.load(open(get_path(before_file)))
    after = json.load(open(get_path(after_file)))
    before_keys = get_keys(before)
    after_keys = get_keys(after)
    all_keys = before_keys.union(after_keys)
    for key in all_keys:
        if key in before_keys and key in after_keys:
            if before[key] == after[key]:
                diff = diff + append_to_result(key, before[key])
            else:
                diff = diff + append_to_result(key, before[key], sign='-')
                diff = diff + append_to_result(key, after[key], sign='+')
        elif key in before_keys and key not in after_keys:
            diff = diff + append_to_result(key, before[key], sign='-')
        elif key not in before_keys and key in after_keys:
            diff = diff + append_to_result(key, after[key], sign='+')
    return diff
