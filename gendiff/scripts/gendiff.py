from gendiff.generate_diff import parser, generate_diff
from gendiff.formatters import get_formatter, FORMATS


def main():
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format', default='default', choices=FORMATS)
    option = parser.parse_args()

    internal_diff = generate_diff(option.first_file, option.second_file)
    render = get_formatter(option.format)
    print(render(internal_diff))


if __name__ == '__main__':
    main()
