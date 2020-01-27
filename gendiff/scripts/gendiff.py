#! /usr/bin/env python
from gendiff.generate_diff import generate_diff, option, render


def main():
    internal_diff = generate_diff(option.first_file, option.second_file)
    print(render(internal_diff))


if __name__ == '__main__':
    main()
