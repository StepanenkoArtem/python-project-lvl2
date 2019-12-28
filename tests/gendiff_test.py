from gendiff.generate_diff import generate_diff
import gendiff.parsers as parser
import os



def test_generate_diff():
    check_file = open(os.path.join(os.getcwd(), "tests/fixtures/diff"), 'r')
    check_text = check_file.read()
    checking_string = generate_diff(
        'tests/fixtures/testfiles/test1.json',
        'tests/fixtures/testfiles/test2.json')
    assert set(check_text.split('\n')) == set(checking_string.split('\n'))




def test_parse():
    directory = 'tests/fixtures/testfiles/'
    test_files = [os.path.join(directory, file) for file in os.listdir(
        directory)]
    for file in test_files:
        assert isinstance(parser.parse(file), dict)


def test_get_extension():
    assert parser.get_extension('file.json') == 'json'
    assert parser.get_extension('file.yml') == 'yml'
    assert parser.get_extension('test/test.json') == 'json'
    assert parser.get_extension('~/home/user/test.2.png') == 'png'
    assert parser.get_extension('/arjs/test.tar.gz') == 'gz'
