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
        Total number of differences
        CSV with records added
        CSV with records deleted
    '''

    fo_old = open(old_filename, 'r')
    fo_new = open(new_filename, 'r')
    csv_old = csv.reader(fo_old)
    csv_new = csv.reader(fo_new)

    dict_old = {}
    dict_new = {}

    for line in csv_old:
        dict_old[line[0]] = line[1:]

    for line in csv_new:
        dict_new[line[0]] = line[1:]

    #Responsible thing is to close open files
    fo_old.close()
    fo_new.close()

    fo_records_added = open('records_added.csv', 'w')
    fo_records_deleted = open('records_deleted.csv', 'w')

    records_added = csv.writer(open('records_added.csv', 'w'), delimiter=',',
                               quoting=csv.QUOTE_ALL)
    records_deleted = csv.writer(open('records_deleted.csv', 'w'), delimiter=',',
                                 quoting=csv.QUOTE_ALL)

    for line in dict_new:
        if line not in dict_old:
            records_added.writerow([line]+dict_new[line])
        else:
            del dict_old[line]

    for line in dict_old:
        records_deleted.writerow([line]+dict_old[line])

def main():
    '''
    Main caller function
    '''

    old_filename = input('Input the name of old CSV in CWD: ')
    new_filename = input('Input the name of new CSV in CWD: ')

    create_diff_csvs(old_filename, new_filename)

main()
