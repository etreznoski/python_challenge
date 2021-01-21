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
total_change = 0
for x in range(1, len(profit_losses)):
    y = profit_losses[x] - profit_losses[x-1]
    profit_change.append(int(y))

#print(profit_change)
#find mean of new list
for x in range (0, len(profit_change)):
    total_change += profit_change[x]
    avg_change = round((total_change / len(profit_change)), 2)
#print(avg_change)    

    #find greatest value in new list-grab corresponding date
    #find lowest value in new list-grab corresponding date
    #start by using a for loop and if statements to find and store min & max
#set up initial variables-value 0
min_value = 0
max_value = 0
#start for loop
for x in profit_losses:
    #use if & elif (start everything off with first value)
    if min_value == 0:
        min_value = x
        max_value = x
    if x > max_value:
        max_value = x
    elif x < min_value:
        min_value = x
# print(min_value)
# print(max_value)

#grab corresponding dates to min and max
#use min and max as index value in main list
max_value_index = profit_losses.index(max_value)
min_value_index = profit_losses.index(min_value)

#use index to pull date
max_date = total_months[max_value_index]
min_date = total_months[min_value_index]
##--------------------------------------------------------
## End Result

## print to terminal

print("Finantial Anlaysis")
print("-------------------------------")
print(f"Total Months: {len(total_months)}")
print(f"Total: ${total_profit_losses}")
print(f"Average Change: ${avg_change}")
print(f"Greatest Increase in Profits: ${max_value} on {max_date}")
print(f"Greatest Decrease in Profits: ${min_value} on {min_date}")

#Write to text file
analysis_file = open("analysis.txt", "w")
l = ["Financial Analysis\n",
f"Total Months: {len(total_months)}\n",
f"Total: ${total_profit_losses}\n",
f"Average Change: ${avg_change}\n",
f"Greatest Increase in Profits: ${max_value} on {max_date}\n",
f"Greatest Decrease in Profits: ${min_value} on {min_date}\n"]

analysis_file.writelines(l)
analysis_file.close




