#Modules
import os
import csv

# Set path for file
csvpath = os.path.join(".", "PyBankResources", "budget_data.csv")
print("Financial Analysis")
print("~~~~~~~~~~~~~~~~~~")
# Read using CSV module
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)

    ProfitLoss = 0
    for rows in csvreader:
        if (len(rows) < 1): #csv file had blank rows after every record
            continue
        ProfitLoss = ProfitLoss + int(rows[1])
    print(f"Profit: ${ProfitLoss}")

    # Return to Second row in .csv
    csvfile.seek(1)

    # Start loop to get row count for number of months
    #row_count = sum(1 for row in csvreader)
    row_count = 0
    next(csvreader)
    for row in csvreader:
        if(len(row) < 1): #csv file had blank rows after every record
            continue
        row_count = row_count + 1
    print(f"Number of Months: {row_count}")

    csvfile.seek(0)
    next(csvreader)
    positiveChangeList = []
    negativeChangeList = []
    previousrow = "firstrow"
    greatestIncreaseMonth = ""
    greatestIncreaseAmount = 0
    greatestDecreaseMonth = ""
    greatestDecreaseAmount = 0
    for row in csvreader:
        if (len(row) < 1): #csv file had blank rows after every record
            continue
        if (previousrow == "firstrow"):
            previousrow = int(row[1])
            continue
        if (previousrow > int(row[1])):
            difference = abs(previousrow - int(row[1]))
            difference = "-" + str(difference)
            difference = int(difference)
            negativeChangeList.append(difference)
            if (difference == max(negativeChangeList)):
                greatestDecreaseMonth = row[0]
                greatestDecreaseAmount = row[1]
        if (previousrow < int(row[1])):
            difference = abs(previousrow - int(row[1]))
            difference = int(difference)
            positiveChangeList.append(difference)
            if(difference == max(positiveChangeList)):
                greatestIncreaseMonth = row[0]
                greatestIncreaseAmount = row[1]
        previousrow = int(row[1])

    changeTotal = int(0)
    changeList = []
    changeList.extend(positiveChangeList)
    changeList.extend(negativeChangeList)
    for change in changeList:
        changeTotal = changeTotal + int(change)

    averageChange = changeTotal / (row_count - 1) #Subtracted first row from months count as there wasn't a change in the first month
    print(f"Average Change: ${round(averageChange,2)}")

    print(f"Greatest Increase in Profits Month : {greatestIncreaseMonth}")
    print(f"Greatest Increase in Profits Amount : ${greatestIncreaseAmount}")
    print(f"Greatest Decrease in Losses Month : {greatestDecreaseMonth}")
    print(f"Greatest Decrease in Losses Amount : ${greatestDecreaseAmount}")