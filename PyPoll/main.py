#Import the OS and csv modules
import os
import csv

#Set the path to read the csv file
csvpath = os.path.join("Resources", "election_data.csv")

#set variables to count each vote and each candidate vote
voto = 0
cand1 = 0
cand2 = 0
cand3 = 0
cand4 = 0
#Begin the Loop, setting delimiter to the ,
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader)
    #check each row and add the corresponding vote to the candidate and the total
    for row in csvreader:
        voto = voto + 1

        if row[2] =="Khan":
            cand1 = cand1 + 1
            cand1_name = str(row[2])

        if row[2] =="Correy":
            cand2 = cand2 + 1
            cand2_name = str(row[2])

        if row[2] =="Li":
            cand3 = cand3 + 1
            cand3_name = str(row[2])

        if row[2] =="O'Tooley":
            cand4 = cand4 + 1
            cand4_name = str(row[2])
#transfer vote numbers into percentage
cand_1_percent= cand1 * 100 / voto
cand_2_percent= cand2 * 100 / voto
cand_3_percent= cand3 * 100 / voto
cand_4_percent= cand4 * 100 / voto

#create a dict in order to check which candidate has more votes and detect the winner
winner = {cand1_name : cand1, cand2_name : cand2, cand3_name : cand3, cand4_name : cand4}

winner_name = max(winner,key=lambda x:winner[x])

#write the results in a txt file 
f = open("Analysis.txt", "a")
print("Election Results", file=f)
print("-"*25, file=f)
print("Total Votes: " + str(voto), file=f)
print("-"*25, file=f)
print(cand1_name + ": " + str(round(cand_1_percent, 3)) + "% " + "(" + str(cand1) + ")", file=f)
print(cand2_name + ": " + str(round(cand_2_percent, 3)) + "% " + "(" + str(cand2) + ")", file=f)
print(cand3_name + ": " + str(round(cand_3_percent, 3)) + "% " + "(" + str(cand3) + ")", file=f)
print(cand4_name + ": " + str(round(cand_4_percent, 3)) + "% " + "(" + str(cand4) + ")", file=f)
print("-"*25, file=f)
print("Winner: " + winner_name, file=f)
print("-"*25, file=f)
f.close()

#print the results in the screen
print("Election Results")
print("-"*25)
print("Total Votes: " + str(voto))
print("-"*25)
print(cand1_name + ": " + str(round(cand_1_percent, 3)) + "% " + "(" + str(cand1) + ")")
print(cand2_name + ": " + str(round(cand_2_percent, 3)) + "% " + "(" + str(cand2) + ")")
print(cand3_name + ": " + str(round(cand_3_percent, 3)) + "% " + "(" + str(cand3) + ")")
print(cand4_name + ": " + str(round(cand_4_percent, 3)) + "% " + "(" + str(cand4) + ")")
print("-"*25)
print("Winner: " + winner_name)
print("-"*25)



