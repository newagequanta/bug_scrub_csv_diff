"""
pytest unit tests
Functions should start with ``test_`` and contain a list of assertions that
evaluate to True if the test succeeds.
For more info see: http://pytest.org/latest/
"""

import io
import task_bug_scrub_csv_diff as bs
def test_open_text_file():
    assert type(bs.open_text_file('test_file.txt')) == io.TextIOWrapper
