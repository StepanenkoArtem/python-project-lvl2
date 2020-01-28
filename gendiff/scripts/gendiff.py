#! /usr/bin/env python
from gendiff.diff import generate_diff, parser


def main():
    option = parser.parse_args()
    internal_diff = generate_diff(option.first_file, option.second_file)
    print(option.format(internal_diff))


if __name__ == '__main__':
    main()
