from gendiff.generate_diff import generate_diff
import gendiff.parsers as parser
from gendiff.cli import render
import os


def test_generate_diff():
    """
    expected_file = open(
        os.path.join(os.getcwd(), "tests/fixtures/internal_diff"), 'r'
    )
    expected_data = json.load(expected_file)
    """
    expected_data = {
        "first_name": ("Sammy", "Artem"),
        "last_name": ("Shark", "Stepanenko"),
        "age": 32,
        "e-mail": (None, "artem.stepanenko.ks.ua@gmail.com"),
        "phone": ("+380663254548", None),
        "email-account": {
            "address": "artem@stepanenko.ks.ua",
            "port": 993,
            "password": ("34656", "4568")
        }
    }
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


def test_render_json():
    expected = open(
        os.path.join(os.getcwd(), "tests/fixtures/rendered_diff"), 'r'
    )
    checking_data = render(generate_diff(
        'tests/fixtures/testfiles/test3.json',
        'tests/fixtures/testfiles/test4.json'))
    assert "".join(expected) == checking_data