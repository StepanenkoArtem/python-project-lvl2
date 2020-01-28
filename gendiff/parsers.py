import os
import json
import yaml


def _get_path(path):
    path = os.path.expanduser(path)
    path = os.path.abspath(os.path.normpath(path))
    return path


def get_data_from(file):
    path = _get_path(file)
    if os.path.splitext(file)[-1] in ['.yml', '.yaml']:
        return yaml.safe_load(open(path))
    return json.load(open(path))
