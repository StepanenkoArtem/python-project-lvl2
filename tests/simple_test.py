from gendiff.generate_diff import generate_diff, get_path
import os


def test_generate_diff():
    check_file = open(os.path.join(os.getcwd(), "tests/fixtures/diff"), 'r')
    check_text = check_file.read()
    checking_string = generate_diff(
        'tests/fixtures/testfiles/test1.json',
        'tests/fixtures/testfiles/test2.json')
    assert set(check_text.split('\n')) == set(checking_string.split('\n'))


def test_get_path():
    control_path = "/home/chief/pyprojects/python-project-lvl2/tests/" \
                   "fixtures/testfiles/test2.json"
    paths = open(
        os.path.join(os.getcwd(), "tests/fixtures/paths.txt"), 'r'
    )
    for path in paths:
        assert get_path(path.rstrip()) == control_path
