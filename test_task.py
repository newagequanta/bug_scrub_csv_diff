"""
pytest unit tests
Functions should start with ``test_`` and contain a list of assertions that
evaluate to True if the test succeeds.
For more info see: http://pytest.org/latest/
"""
import sys
import task_bug_scrub_csv_diff
import hashlib

sys.path = ['', '/venv/python361-1/lib/python36.zip', '/venv/python361-1/lib/python3.6',
            '/venv/python361-1/lib/python3.6/lib-dynload',
            '/home/bdb/.pyenv/versions/3.6.1/lib/python3.6',
            '/venv/python361-1/lib/python3.6/site-packages',
            '/venv/python361-1/src/jtextfsm']


def test_task():
    '''
    test the hashes of the files created against precalculated hashes
    '''
    task_bug_scrub_csv_diff.task(None,
                                 '/var/bdb/sessions/sandboxed-user/test_666.csv',
                                 '/var/bdb/sessions/sandboxed-user/test_852.csv')
    hash_added = hashlib.sha256(open('records_added.csv',
                                     'rb').read()).hexdigest()
    hash_deleted = hashlib.sha256(open('records_deleted.csv',
                                       'rb').read()).hexdigest()
    hash_total = hash_added + hash_deleted
    assert hash_total == (
        '84217c0024d9966b25c8ec4988b457bfbc58af02381188af95479d702ab45b24' +
        '17db7b957ebba1e8e7d3812a9f349e43eb4da0d0da053fb773e42162f1e9d30f')
