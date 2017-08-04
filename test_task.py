"""
pytest unit tests
Functions should start with ``test_`` and contain a list of assertions that
evaluate to True if the test succeeds.
For more info see: http://pytest.org/latest/
"""

import io
import task_bug_scrub_csv_diff as bs
def test_task():
    return_text = ('Task Finished.\n'
                   'records_added.csv and records_deleted.csv created.\n'
                   'Please download them from your files.')
    assert bs.task(None, 'GDC_852.csv', 'GDC_666.csv') == return_text

