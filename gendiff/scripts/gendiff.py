from gendiff.generate_diff import parser, generate_diff


def main():
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format')
    option = parser.parse_args()
    generate_diff(
        option.first_file,
        option.second_file,
    )


if __name__ == '__main__':
    main()
