#Import OS module and module for reading csv files
import os
import csv

#set up path to csv file
csvpath = os.path.join('Resources', 'election_data.csv')

votes_cast = []
li_votes = []
khan_votes = []
correy_votes = []
otooley_votes = []
#read CSV file
with open(csvpath, newline='') as csvfile:
    #specify deliminator and variable to hold contents
    csvreader = csv.reader(csvfile, delimiter=',')

    #print(csvreader)

    #read header row
    csv_header = next(csvreader)
    
    #iterate through rows, grab length of votes_cast column
    for row in csvreader:
        votes_cast.append(row[2])
    total_votes = len(votes_cast)
               
#Find unique strings(candidates) in votes_cast list
#store in new variable(list)

    candidate_list = list(set(votes_cast))
    print(candidate_list)
    
    
#For each candidate vote-append to get candidate_total
for i in votes_cast:
    if i == "Li":
        li_votes.append(i)
    elif i == "Khan":
        khan_votes.append(i)
    elif i == "Correy":
        correy_votes.append(i)
    elif i == "O'Tooley":
        otooley_votes.append(i)
# print(f"Li: {len(li_votes)}")
#percent won = 'candidate_total' / total_votes

#repeat for each candidate

#winner = candidate with greatest vote total





##-------------------------------------------------------
##End Analysis
##Print to terminal

print("Election Results")
print("--------------------------")
print(f"Total Votes: {total_votes}")
print("--------------------------")
# print(f"Khan: {percent won} ( {len(khan_votes)} )")
# print(f"Correy: {percent won} ( {len(correy_votes)} )")
# print(f"Li: {percent won} ( {len(li_votes)} )")
# print(f"O'Tooley: {percent won} ( {len(otooley_votes)} )")
# print("--------------------------")
# print("Winner: {winner}")
# print("--------------------------")
