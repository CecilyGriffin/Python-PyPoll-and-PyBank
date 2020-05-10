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


    resultspath = os.path.join(".", "PyPollAnalysis.txt")
    if os.path.exists(resultspath):
        os.remove(resultspath)
    f = open(resultspath, "a")
    f.write("Election Results\n")
    f.write("~~~~~~~~~~~~~~~~\n")
    #Row counter to count total votes
    row_count = 0
    next(csvreader)
    for row in csvreader:
        if(len(row) < 1): #csv file had blank rows after every record
            continue
        row_count = row_count + 1
    print(f"Total Votes: {row_count}")
    print("~~~~~~~~~~~~~~~~")
    f.write(f"Total Votes: {row_count}\n")
    f.write("~~~~~~~~~~~~~~~~\n")
    csvfile.seek(0)
    next(csvreader)
    #loop for candidates
    candidates = []
    for row in csvreader:
      if row[2] not in candidates:
        candidates.append(row[2])

    
    candidateCount = 0
    winningCandidate = "" 
    for candidate in candidates:
      csvfile.seek(0)
      next(csvreader)
      counter = 0
      for row in csvreader:
        if(row[2] == candidate):
          counter = counter + 1
      percent = (counter / row_count) * 100
      if(counter > candidateCount):
        winningCandidate = candidate
        candidateCount = counter
      f.write(f"{candidate}: {round(percent,3)}% {counter}\n")
      print(f"{candidate}: {round(percent,3)}% {counter}")
    f.write("~~~~~~~~~~~~~~~~\n")
    f.write(f"Winner: {winningCandidate}\n")
    f.write("~~~~~~~~~~~~~~~~\n")
    print("---------------------------")
    print(f"Winner: {winningCandidate}")
    print("~~~~~~~~~~~~~~~~\n")

    f.close()
csvfile.close()
