#Modules
import os
import csv

#Set path for file
csvpath = os.path.join(".", "PyBankResources", "budget_data.csv")

#Read using CSV module
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
# Read the header row first
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    for row in csvreader:
        print(row[0])
        #print(row)