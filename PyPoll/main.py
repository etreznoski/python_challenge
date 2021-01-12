#Import OS module and module for reading csv files
import os
import csv

#set up path to csv file
csvpath = os.path.join('Resources', 'election_data.csv')

#read CSV file
with open(csvpath, newline='') as csvfile:
    #specify deliminator and variable to hold contents
    csvreader = csv.reader(csvfile, delimiter=',')

    #print(csvreader)

    #read header row
    csv_header = next(csvreader)
    # print(csv_header)

##-------------------------------------------------------
##End Analysis
##Print to terminal

# Print("Election Results")
# Print("--------------------------")
# Print(f"Total Votes: {}")
# Print("--------------------------")
# Print(f"Khan: {percent won} ( {num of votes} )")
# Print(f"Correy: {percent won} ( {num of votes} )")
# Print(f"Li: {percent won} ( {num of votes} )")
# Print(f"O'Tooley: {percent won} ( {num of votes} )")
# Print("--------------------------")
# Print("Winner: {winner}")
# Print("--------------------------")
