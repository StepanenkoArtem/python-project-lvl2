import json
import os


def absolutize_path(path):
    return os.path.abspath(path)


def get_json_data_from(file):
    return json.load(open(absolutize_path(file)))


def compare_value_from_key():
    pass


def generate_diff(f1, f2):
    first_file_data = get_json_data_from(f1)
    second_file_data = get_json_data_from(f2)
    common_set_of_keys = set.union(set(first_file_data.keys()),
                                set(second_file_data.keys())
                            )
    print(common_set_of_keys)
    return "Some string"
