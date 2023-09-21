import os
import csv

# defining variables up front
netincome = 0
difference = 0
previousvalue = 0
netchange = 0
max_inc = 0
max_dec = 0
average = 0.0
list_change = []
list_month = []
difference = 0
count =0
cwd = os.getcwd()


csvpath = os.path.join("Resources", "budget_data.csv")
txtpath = os.path.join("analysis", "budget_analysis.txt")

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csvheader = next(csvreader)
    # counting number of lines
    first_row = next(csvreader)
    count = count +1
    previousvalue = int(first_row[1])
    netincome += int(first_row[1])

    for line in csvreader:
        count = count +1
        netincome = netincome + int(line[1])

        difference = int(line[1]) - previousvalue
        list_change += [difference]
        list_month += [line[0]]
        previousvalue = int(line[1])
        #Using if statements to capture max and min profits (along with date) for each iteration
        if difference > max_inc:
            max_inc = difference
            max_mon = line[0]
        if difference < max_dec:
            max_dec = difference
            min_mon = line[0]
        else:
            max_dec = max_dec
            max_inc = max_inc
            min_mon = min_mon
            max_mon = max_mon 
    previousvalue = int(line[1])

    # Calculating net change and average of net change over the time period
    netchange = sum(list_change)
    average = netchange/len(list_change) 
    
# printing outuputs
output = f"Total Months {count}\n" f"Your net income is ${netincome}\n" f"Average Change: ${round(average,2)}\n" f"Greatest Increase in Profits: {max_mon} ({max_inc})\n" f"Greatest Decrease in Profits: {min_mon} ({max_dec})\n"
# printing outuputs

# print(f"Average change: ${average}")
print(output)
with open(txtpath, "w") as txtfile:
    txtfile.write(output)
