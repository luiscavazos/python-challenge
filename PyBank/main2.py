#Import the OS and csv modules
import os
import csv

#Set the path to read the csv file
csvpath = os.path.join("Resources", "budget_data.csv")

#Set values and dict
total_dict={}
sum_total = 0
month_total = 0
min_total = 0
max_total = 0

#Begin the Loop, setting delimiter to the ,
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader)
    
    #Add all months to a new value and add rows to dict
    for row in csvreader:
        total_dict.update({row[0] : row[1]})
        month_total = month_total + 1

    #Add total of all months
        sum_total = sum_total + int(row[1])
    
    #Average of changes in the entire period
        avg_change = sum_total / month_total

    #Tried getting the max with the key and the value but couldnt so I let it only with the key and still couldnt get the biggest value.
    Total_increase = max(total_dict,key=lambda x:total_dict[x])   
    Total_decrease = min(total_dict, key=lambda x:total_dict[x])   
      
    f = open("analysis/Analysis2.txt", "a")
    print("Financial Analysis", file=f)
    print("-"*28, file=f)
    print("Total Months: " + str(month_total), file=f)
    print("Total: " + str(sum_total), file=f)
    print("Average Change: " + str(avg_change), file=f)
    print("Greatest Increase in Profits: "+ str(Total_increase), file=f) 
    print("Greatest Decrease in Profits: "+ str(Total_decrease), file=f)
    f.close()

    print("Financial Analysis")
    print("-"*28)
    print("Total Months: " + str(month_total))
    print("Total: " + str(sum_total))
    print("Average Change: " + str(avg_change))
    print("Greatest Increase in Profits: " + str(Total_increase)) 
    print("Greatest Decrease in Profits: " + str(Total_decrease))
