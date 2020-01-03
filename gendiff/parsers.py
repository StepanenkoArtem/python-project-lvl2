import os
import json
import yaml


def _get_path(path):
    if "~" in path:
        path = os.path.expanduser(path)
    path = os.path.abspath(os.path.normpath(path))
    return path


def _get_extension(file):
    basename = os.path.basename(file)
    return basename.split('.')[-1:][0]


def get_data_from(file):
    path = _get_path(file)
    if _get_extension(path) == 'yml':
        return yaml.safe_load(open(path))
    return json.load(open(path))
