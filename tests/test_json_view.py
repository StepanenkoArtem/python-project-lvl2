import os
import json
from gendiff.generate_diff import generate_diff
from gendiff.format import json_view


def test_render():
    expected = json.load(
        open(os.path.join(os.getcwd(), "tests/fixtures/json_diff"), 'r')
    )
    checking_data = json_view.render(
            generate_diff(
                'tests/fixtures/testfiles/before.json',
                'tests/fixtures/testfiles/after.json'
            )
        )
    assert expected == json.loads(checking_data)
