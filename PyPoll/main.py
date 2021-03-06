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
    #print(candidate_list)
    
    
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
#round percent
#repeat for each candidate
li_percent = round(((len(li_votes) / total_votes) * 100), 3)
khan_percent = round(((len(khan_votes) / total_votes) * 100), 3)
correy_percent = round(((len(correy_votes) / total_votes) * 100), 3)
otooley_percent = round(((len(otooley_votes) / total_votes) * 100), 3)

# print(li_percent)


#winner = candidate with greatest vote total
if li_percent > khan_percent and li_percent > correy_percent and li_percent > otooley_percent:
    winner = "Li"
elif khan_percent > li_percent and khan_percent > correy_percent and khan_percent > otooley_percent:
    winner = "Khan"
elif correy_percent > khan_percent and correy_percent > li_percent and correy_percent > otooley_percent:
    winner = "Correy"
elif otooley_percent > khan_percent and otooley_percent > correy_percent and otooley_percent > li_percent:
    winner = "O'Tooley"
# print(winner)


##-------------------------------------------------------
##End Analysis


print("Election Results")
print("--------------------------")
print(f"Total Votes: {total_votes}")
print("--------------------------")
print(f"Khan: {khan_percent}% ( {len(khan_votes)} )")
print(f"Correy: {correy_percent}% ( {len(correy_votes)} )")
print(f"Li: {li_percent}% ( {len(li_votes)} )")
print(f"O'Tooley: {otooley_percent}% ( {len(otooley_votes)} )")
print("--------------------------")
print(f"Winner: {winner}")
print("--------------------------")

##Print to txt file
analysis_file = open("analysis.txt", "w")
l = [f"Election Results\n",
"--------------------------\n",
f"Total Votes: {total_votes}\n",
"--------------------------\n",
f"Khan: {khan_percent}% ( {len(khan_votes)} )\n",
f"Correy: {correy_percent}% ( {len(correy_votes)} )\n",
f"Li: {li_percent}% ( {len(li_votes)} )\n",
f"O'Tooley: {otooley_percent}% ( {len(otooley_votes)} )\n",
"--------------------------\n",
f"Winner: {winner}\n",
"--------------------------\n"]

analysis_file.writelines(l)
analysis_file.close