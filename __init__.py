'''
The hook for BDB, BDB calls the task() function via GUI
This will call create_csv in bug_scrub_to_csv module
'''
#code.py is the file with all the main functions

from . import code
__copyright__ = "Copyright (c) 2017 Cisco Systems. All rights reserved."

def task(env, new_filename, old_filename):
    """
    This package accepts to CSVs, supposed to be created by another BDB script,
    bug_scrub_to_csv and find the differences between the two

    This task is run by the bdblib library, full doc and examples at:
    https://scripts.cisco.com/doc/
    Browse more examples in BDB starting with "bdblib_":
    https://scripts.cisco.com/ui/browse/used/0/bdblib_

    """
    code.create_diff_csvs(old_filename, new_filename)
    return ('Task Finished.\n'
            'records_added.csv and records_deleted.csv created.\n'
            'Please download them from your files.')
