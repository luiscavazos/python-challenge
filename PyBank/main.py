#Import the OS and csv modules
import os
import csv

#Set the path to read the csv file
csvpath = os.path.join("Resources", "budget_data.csv")

sum_total = 0
month_total = 0
min_total = 0
max_total = 0
#Begin the Loop, setting delimiter to the ,
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader)
    
    #Add all months to a new value
    for row in csvreader:
        month_total = month_total + 1

    #Add total of all months
        sum_total = sum_total + int(row[1])
    
    #Average of changes in the entire period
        avg_change = sum_total / month_total

        if int(row[1]) >= int(max_total):
            max_total = row[1]
            max_st = row

        if int(row[1]) <= int(min_total):
            min_total = row [1]
            min_st = row
 
      
    f = open("analysis/Analysis.txt", "a")
    print("Financial Analysis", file=f)
    print("-"*28, file=f)
    print("Total Months: " + str(month_total), file=f)
    print("Total: " + str(sum_total), file=f)
    print("Average Change: " + str(avg_change), file=f)
    print("Greatest Increase in Profits: ", file=f) 
    print(max_st, file =f)
    print("Greatest Decrease in Profits: ", file=f)
    print(min_st, file=f)
    f.close()

    print("Financial Analysis")
    print("-"*28)
    print("Total Months: " + str(month_total))
    print("Total: " + str(sum_total))
    print("Average Change: " + str(avg_change))
    print("Greatest Increase in Profits: ") 
    print(max_st)
    print("Greatest Decrease in Profits: ")
    print(min_st)
