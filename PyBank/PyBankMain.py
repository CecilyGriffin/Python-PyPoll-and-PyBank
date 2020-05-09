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

     #Average of the changes in profit losses
    average = int(ProfitLoss/row_count)
    print(f"Average Change ${average}")

csvfile.close()