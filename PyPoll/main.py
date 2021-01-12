#Import OS module and module for reading csv files
import os
import csv

#set up path to csv file
csvpath = os.path.join('Resources', 'election_data.csv')

votes_cast = []

#read CSV file
with open(csvpath, newline='') as csvfile:
    #specify deliminator and variable to hold contents
    csvreader = csv.reader(csvfile, delimiter=',')

    #print(csvreader)

    #read header row
    csv_header = next(csvreader)
    # print(csv_header)
    for row in csvreader:
        votes_cast.append(row[2])
    total_votes = len(votes_cast)

##-------------------------------------------------------
##End Analysis
##Print to terminal

# print("Election Results")
# print("--------------------------")
print(f"Total Votes: {total_votes}")
# print("--------------------------")
# print(f"Khan: {percent won} ( {num of votes} )")
# print(f"Correy: {percent won} ( {num of votes} )")
# print(f"Li: {percent won} ( {num of votes} )")
# print(f"O'Tooley: {percent won} ( {num of votes} )")
# print("--------------------------")
# print("Winner: {winner}")
# print("--------------------------")
