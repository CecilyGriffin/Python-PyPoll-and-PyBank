#Module
import os
import csv

#Set Path for file
csvpath = os.path.join(".", "PyPollResources", "election_data.csv")

#Title
print("Election Results")
print("~~~~~~~~~~~~~~~~")

#Open CSV
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)