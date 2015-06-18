'''
Checks the titles in a 360Giving data file (csv) against the titles
set out in the schema.

Uses the example csv file from:
http://docs.threesixtygiving.org/assets/standard/schema/summary-table/360-giving-schema-titles.csv/Activity.csv
renamed as 360Activity.csv, and in the same directory as this script

Usage: 
Make sure 360Activity.csv is in the same directory as this script
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
#import pandas as pd

# Required fields as defined here:
# http://docs.threesixtygiving.org/docs/#toc5
required_fields = ['Identifier',
                    'Title',
                    'Description',
                    'Currency',
                    'Amount Awarded',
                    'Award Date',
                    'Recipient Org:Identifier',
                    'Recipient Org:Name',
                    'Funding Org:Identifier',
                    'Funding Org:Name'
                  ]

# Get a list of titles used in the example csv file
with open('360Activity.csv', 'rb') as csvfile:
      reader = csv.reader(csvfile, delimiter=',', quotechar='"')
      titles = next(reader)
      
#df = pd.read_csv('360Activity.csv')
#print (df)
#print df['Identifier'].count()
#print (list(df))


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
for csv_file in csvs:
    # print ('Checking ' + csv_file)
    with open(folder + '/' + csv_file, 'rb') as csvfile:
          reader = csv.reader(csvfile, delimiter=',', quotechar='"')
          first_row = next(reader)
          #for row in spamreader:
          #   print ', '.join(row)
          # print (first_row)
          
          print('Standard fields used: ' + csv_file)
          common_list = []
          common_list = set(first_row) & set(titles)
          for title_item in sorted(common_list):
              #dfList = df['Identifier']
              #print (dfList)
              if title_item in required_fields:
                  print ('*' + title_item + '*')
                  #print dfList.count()
                  #print ('*' + title_item + '*')
              else:
                  print (title_item)
          
          print ('\n')
          print('Fields NOT in standard: ' + csv_file)
          listA = []
          listA = sorted(list(set(first_row)-set(titles)))
          for item in listA:
              print (item)
          
          print ('\n')
          print('Standard fields not used: ' + csv_file)
          listB = []
          listB = sorted(list(set(titles)-set(first_row)))
          for item in listB:
              if item in required_fields:
                  print ('*' + item + '*')
              else:
                  print (item)
          print ('\n')


