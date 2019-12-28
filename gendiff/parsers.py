import os
import json
import yaml


def get_path(path):
    if "~" in path:
        path = os.path.expanduser(path)
    path = os.path.abspath(os.path.normpath(path))
    return path


def get_extension(path):
    basename = os.path.basename(path)
    return basename.split('.')[-1:][0]


def parse(file):
    path = get_path(file)
    if get_extension(path) == 'json':
        return json.load(open(path))
    elif get_extension(path) == 'yml':
        return yaml.safe_load(open(path))
