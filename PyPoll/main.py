import os
import csv
csvpath = os.path.join('Resources', 'election_data.csv')
print(csvpath)

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',') 
    csv_header = next(csvfile)
    print(csv_header)
    print(csvreader)

