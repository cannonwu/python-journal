# python journal
# allow user to write to journal, record entry date
# journal should store user entry in some way
# allow user to access previous journal entries by identifying with date
# probably need to use, tuple, matrix, or write to file

from journal import Journal

date = input('Enter the Date (mm/dd/yy): ')
entry = input('Enter your thoughts: ')
journal_entry1 = Journal(date, entry)

with open('savejournal.txt', 'w') as myFile:
    myFile.write(date + '\n')

print('Journal entry recorded.')

# print(journal_entry1.date)
