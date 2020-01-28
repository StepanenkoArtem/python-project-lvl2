import os
from gendiff.diff import generate_diff
from gendiff.format.default_view import render


def test_render():
    expected = open(
        os.path.join(os.getcwd(), "tests/fixtures/default_diff"), 'r'
    )
    checking_data = render(
        generate_diff(
            'tests/fixtures/testfiles/before.json',
            'tests/fixtures/testfiles/after.json'
        )
    )
    assert "".join(expected) == checking_data
