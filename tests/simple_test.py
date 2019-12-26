from gendiff.generate_diff import generate_diff
import os


def test_generate_diff():
    check_file = open(os.path.join(os.getcwd(), "tests/fixtures/diff"), 'r')
    check_text = check_file.read()
    checking_string = generate_diff(
        'tests/fixtures/testfiles/test1.json',
        'tests/fixtures/testfiles/test2.json')
    assert set(check_text.split('\n')) == set(checking_string.split('\n'))

