#Import OS module and module for reading csv files
import os
import csv

#set up path to csv file
csvpath = os.path.join('Resources', 'budget_data.csv')

#set empty lists
total_months = []
profit_losses = []


#read CSV file
with open(csvpath, newline='') as csvfile:
    #specify deliminator and variable to hold contents
    csvreader = csv.reader(csvfile, delimiter=',')

    #print(csvreader)

    #read header row
    csv_header = next(csvreader)
    #print(csv_header)

    #fill in list contents
    for row in csvreader:

         total_months.append(row[0])
         profit_losses.append(row[1])

    #test to see if prints total number of months
    print(len(total_months))
    




