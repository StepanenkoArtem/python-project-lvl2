import argparse
import os
import json


parser = argparse.ArgumentParser(
    description='Generate difference between two files'
)


def get_abspath(path):
    return os.path.abspath(path)


def get_keys(dictionary):
    return list(dictionary.keys())


def common_keys_differense(first_dict, second_dict):
    result = ""
    first_dict_keys = set(get_keys(first_dict))
    second_dict_keys = set(get_keys(second_dict))
    common_keys = first_dict_keys.intersection(second_dict_keys)
    for key in common_keys:
        if first_dict[key] != second_dict[key]:
            result = result + "+ {}: {}\n- {}: {}\n".format(
                key, first_dict[key],
                key, second_dict[key],
            )
    return result


def get_difference_between(first_dict, second_dict):
    result = ""
    first_dict_keys = set(get_keys(first_dict))
    second_dict_keys = set(get_keys(second_dict))
    different_keys = first_dict_keys.difference(second_dict_keys)
    for key in different_keys:
        result = result + "- {}: {}\n".format(
            key, first_dict[key]
        )
    different_keys = second_dict_keys.difference(first_dict_keys)
    for key in different_keys:
        result = result + "+ {}: {}\n".format(
            key, second_dict[key]
        )
    return result


def generate_diff(before, after):
    before_dict = json.load(open(get_abspath(before)))
    after_dict = json.load(open(get_abspath(after)))
    diff = common_keys_differense(before_dict, after_dict) + \
           get_difference_between(before_dict, after_dict)
    return diff
