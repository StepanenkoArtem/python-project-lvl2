import argparse
from gendiff import format


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
