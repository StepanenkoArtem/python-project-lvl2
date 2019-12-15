import argparse


def main():
    parser = argparse.ArgumentParser(description='Generate diff')
    parser.add_argument("first_file", help="Input path to first file")
    parser.add_argument("second_file", help="input path to second file")
    parser.parse_args()


if __name__ == "__main__":
    main()
