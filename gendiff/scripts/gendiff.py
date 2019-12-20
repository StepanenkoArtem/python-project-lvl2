from gendiff.generate_diff import parser, generate_diff
import gendiff.cli as cli


def main():
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format', default='json')
    option = parser.parse_args()
    cli.output(
        generate_diff(
            option.first_file,
            option.second_file,
        ),
        option.format)


if __name__ == '__main__':
    main()
