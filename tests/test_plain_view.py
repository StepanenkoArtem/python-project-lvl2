import os
from gendiff.diff import generate_diff
from gendiff.format import plain_view


def test_render():
    expected = list(open(
        os.path.join(os.getcwd(), "tests/fixtures/plain_diff"), 'r'
    ))
    checking_data = plain_view.render(
            generate_diff(
                'tests/fixtures/testfiles/before.json',
                'tests/fixtures/testfiles/after.json'
            )
        )
    for line in expected:
        assert line.strip() in checking_data
