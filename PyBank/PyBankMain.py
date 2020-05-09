#Modules
import os
import csv

#Set path for file
csvpath = os.path.join(".", "PyBankResources", "budget_data.csv")

print("Financial Analysis")
print("~~~~~~~~~~~~~~~~~~")
#Read using CSV module
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)

    ProfitLoss = 0
    for rows in csvreader:
        ProfitLoss = ProfitLoss + int(rows[1])
    print(f"Profit: ${ProfitLoss}")
    
    #Return to Second row in .csv
    csvfile.seek(1)

    #Start loop to get row count for number of months
    row_count = sum(1 for row in csvreader)
    print(f"Number of Months: {row_count}")

    csvfile.seek(0)
    changeList = []
    previousrow = 0
    next(csvreader)
    for row in csvreader:
        if (int(row[1]) > previousrow):
            #print(f"add {previousrow}")
            changeList.append(int(row[1]) - previousrow)
        if (int(row[1]) < previousrow):
            #print(f"subtract {previousrow}")
            changeList.append(int(row[1]) - previousrow)
        previousrow = int(row[1])

    changeTotal = 0
    for change in changeList:
        changeTotal = changeTotal + change

    averageChange = changeTotal / row_count
    print(f"Average Change: ${averageChange}")

    greatestIncrease = max(changeList)
    greatestDecrease = min(changeList)

    print(f"Greatest Increase: ${greatestIncrease}")
    print(f"Greatest Decrease: ${greatestDecrease}")

csvfile.close()