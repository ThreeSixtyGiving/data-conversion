'''
Checks the identifiers given in a number of 360Giving data files (csv)

Given a number files it can check that identifiers are unique across a 
dataset

Usage: 
If your csv files are in the same directory, simply run:

python check_titles.py

Optionally you can add a command line argument with the path to your csvs
e.g. If your files are in a 'data' directory 
python check_titles.py data

You might want to pipe the results to a file:
python check_titles.py > results.txt
'''

import csv
import os
import sys



# Find all csv files in the current directory
# Ignore the example csv file tho!
if len(sys.argv) == 2:
    folder = sys.argv[1] 
else:
    folder = os.getcwd()

csvs = []
for i in os.listdir(folder):
    if i.endswith(".csv") and i != '360Activity.csv': 
        csvs.append(i)
        continue
    else:
        continue


'''
Loop through all the csv files and compare the column headings with
the example and with required fields.

Uses the python 'set' function to compare lists
'''

identifiers=[]
count_sheets = 0
count_rows = 0
count_rows_in_sheets = []
for csv_file in csvs:
    count_sheets +=1
    # print ('Checking ' + csv_file)

    with open(folder + '/' + csv_file, 'rb') as csvfile:
          reader = csv.reader(csvfile, delimiter=',', quotechar='"')
          first_row = next(reader)
          #Find the position of 'Identifier' in the row
          identifier_column = first_row.index('Identifier')
          
          count_rows_in_this_sheet = 0
          for row in reader:
              identifiers.append(row[identifier_column])
              count_rows +=1
              count_rows_in_this_sheet +=1
          #   print ', '.join(row)
          # print (first_row)
    count_rows_in_sheets.append(count_rows_in_this_sheet)
      
print ('Total sheets: {0}').format(count_sheets)
print ('Total rows: {0}').format(count_rows)
print(count_rows_in_sheets)
print ('No. Identifiers: {0}').format(len(identifiers))
print ('Unique Identifiers: {0}').format(len(set(identifiers)))
print (count_rows)
print (len(identifiers))
print (len(set(identifiers)))

