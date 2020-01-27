import os
from gendiff.generate_diff import generate_diff
from gendiff.format import default_view


def test_render():
    expected = open(
        os.path.join(os.getcwd(), "tests/fixtures/default_diff"), 'r'
    )
    checking_data = default_view.render(
        generate_diff(
            'tests/fixtures/testfiles/before.json',
            'tests/fixtures/testfiles/after.json'
        )
    )
    assert "".join(expected) == checking_data
