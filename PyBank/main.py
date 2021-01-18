#Import OS module and module for reading csv files
import os
import csv

#set up path to csv file
csvpath = os.path.join('Resources', 'budget_data.csv')

#set empty lists/variables
total_months = []
profit_losses =[]
total_profit_losses = 0

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
         profit_losses.append(int(row[1]))
         total_profit_losses += int(row[1])
        

#calculate changes in profit/losses over entire period
#THen find average of those changes
    #calculate change from one month to the next-store in new list
   
profit_change = []

for x in range(1, len(profit_losses)):
    y = profit_losses[x] - profit_losses[x-1]
    profit_change.append(int(y))

#print(profit_change)
#find mean of new list


    #find greatest value in new list-grab corresponding date
    #find lowest value in new list-grab corresponding date


##--------------------------------------------------------
## End Result

## print to terminal

print("Finantial Anlaysis")
print("-------------------------------")
print(f"Total Months: {len(total_months)}")
print(f"Total: ${total_profit_losses}")
# print(f"Average Change: ${}")
# print(f"Greatest Increase in Profits: {}")
# print(f"Greatest Decrease in Profits: {}")





