#!/bin/bash
# Pull all the csv data listed on the 360 Giving DKAN
# Run over each file and check the column headers against the 
# standard column headers
# Generate a report
# Convert the report to a HTML file

python dkan_calls.py
python check_titles.py data > report.txt
sed 's/$/<br>/' report.txt > index.html 
