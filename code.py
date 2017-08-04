'''
Version 2:
    Improved the file read to ensure the file object is closed properly
Program to find the following:
    1. Accept two CSVs - New and Old
    2. Create two CSVs:
        a. Records added to the New CSV
        b. Records removed from the OLD CSV
        b. Total number of differences
'''
import csv

def create_diff_csvs(old_filename, new_filename):
    '''
    INPUT - 2 CSV file objects
    OUTPUT:
        CSV with records added
        CSV with records deleted
    '''

    fo_old = open(old_filename, 'r')
    fo_new = open(new_filename, 'r')
    csv_old = csv.reader(fo_old)
    csv_new = csv.reader(fo_new)

    list_old = []
    list_new = []
    bugs_old = []
    bugs_new = []

    for line in csv_old:
        bugs_old.append(line[0])
        list_old.append(line)

    for line in csv_new:
        bugs_new.append(line[0])
        list_new.append(line)

    #Responsible thing is to close open files
    fo_old.close()
    fo_new.close()

    fo_records_added = open('records_added.csv', 'w')
    fo_records_deleted = open('records_deleted.csv', 'w')

    records_added = csv.writer(fo_records_added, delimiter=',',
                               quoting=csv.QUOTE_ALL)
    records_deleted = csv.writer(fo_records_deleted, delimiter=',',
                                 quoting=csv.QUOTE_ALL)

    for bug, record in zip(bugs_new, list_new):
        if bug not in bugs_old:
            records_added.writerow(record)
        else:
            bugs_old.remove(bug)

    for record in list_old:
        if record[0] in bugs_old:
            records_deleted.writerow(record)

    fo_records_added.close()
    fo_records_deleted.close()
