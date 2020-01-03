from gendiff.generate_diff import generate_diff
import gendiff.parsers as parser
import os, json


def test_generate_diff():
    expected_file = open(
        os.path.join(os.getcwd(), "tests/fixtures/expected_tree_diff"), 'r'
    )
    expected_data = json.load(expected_file)
    checking_data = generate_diff(
        'tests/fixtures/testfiles/test3.json',
        'tests/fixtures/testfiles/test4.json')
    for key in expected_data:
        assert expected_data[key] == checking_data[key]


def test_parse():
    directory = 'tests/fixtures/testfiles/'
    test_files = [
        os.path.join(directory, file) for file in os.listdir(directory)
    ]
    for file in test_files:
        assert isinstance(parser.get_data_from(file), dict)
