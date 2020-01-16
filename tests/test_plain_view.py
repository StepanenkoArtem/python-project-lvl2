import os
from gendiff.generate_diff import generate_diff
from gendiff.formatters import plain_view


def test_render():
    expected = open(
        os.path.join(os.getcwd(), "tests/fixtures/plain_diff"), 'r'
    )
    checking_data = plain_view.render(
        generate_diff(
            'tests/fixtures/testfiles/before.json',
            'tests/fixtures/testfiles/after.json')
    )
    assert "".join(expected) == checking_data
