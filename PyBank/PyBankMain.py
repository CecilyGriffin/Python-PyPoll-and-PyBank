#Modules
import os
import csv

# Set path for file
csvpath = os.path.join(".", "PyBankResources", "budget_data.csv")
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
            if (difference == min(negativeChangeList)):
                greatestDecreaseMonth = row[0]
                greatestDecreaseAmount = difference
        if (previousrow < int(row[1])):
            difference = abs(previousrow - int(row[1]))
            difference = int(difference)
            positiveChangeList.append(difference)
            if(difference == max(positiveChangeList)):
                greatestIncreaseMonth = row[0]
                greatestIncreaseAmount = difference
        previousrow = int(row[1])

    changeTotal = int(0)
    changeList = []
    changeList.extend(positiveChangeList)
    changeList.extend(negativeChangeList)
    for change in changeList:
        changeTotal = changeTotal + int(change)

    averageChange = changeTotal / (row_count - 1) #Subtracted first row from months count as there wasn't a change in the first month
    
    #Print to terminal
    print("Financial Analysis")
    print("~~~~~~~~~~~~~~~~~~")
    print(f"Number of Months: {row_count}")
    print(f"Total: ${ProfitLoss}")
    print(f"Average Change: ${round(averageChange,2)}")
    print(f"Greatest Increase in Profits Month : {greatestIncreaseMonth} - (${greatestIncreaseAmount})")
    print(f"Greatest Decrease in Losses Month : {greatestDecreaseMonth} - (${greatestDecreaseAmount})")

    #Export to txt file
    resultspath = os.path.join(".", "PyBankAnalysis.txt")
    if os.path.exists(resultspath):
        os.remove(resultspath)
    f = open(resultspath, "a")
    f.write("Financial Analysis\n")
    f.write("~~~~~~~~~~~~~~~~~~\n")
    f.write(f"Number of Months: {row_count}\n")
    f.write(f"Total: ${ProfitLoss}\n")
    f.write(f"Average Change: ${round(averageChange,2)}\n")
    f.write(f"Greatest Increase in Profits Month and Amount: {greatestIncreaseMonth}  (${greatestIncreaseAmount})\n")
    f.write(f"Greatest Decrease in Losses Month and Amount: {greatestDecreaseMonth}  (${greatestDecreaseAmount})\n")
    f.close()
csvfile.close()