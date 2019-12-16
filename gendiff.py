import argparse
from gendiff import generate_diff


def main():
    parser = argparse.ArgumentParser(description='Generate diff')
    parser.add_argument("first_file", help="Input path to first file")
    parser.add_argument("second_file", help="input path to second file")
    parser.add_argument("-f", "--format", help="set format of output")
    args = vars(parser.parse_args())
    first_file, second_file = (args['first_file'], args['second_file'])
    generate_diff(first_file, second_file)


if __name__ == "__main__":
    main()
