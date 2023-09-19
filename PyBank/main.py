import os
import csv

netincome = int(0)
cwd = os.getcwd()
csvpath = os.path.join('..', 'Resources', 'budget_data.csv')
print(csvpath)


#with open(csvpath, 'r') as file_handler:
    #lines = file_handler.read()
    # print(lines)
    # print(type(lines))

with open(csvpath) as csvfile:
    

    csvreader = csv.reader(csvfile, delimiter=',')
    
    for count, line in enumerate(csvreader):
        pass
        if count == 0: 
            netincome == 0
        elif count != 0:
            netincome = netincome + int(line[1])
            netincome_dollar = '$'+ str(netincome)
        if count <= 1:
            difference == 0
            sum == 0
        elif count > 1:
            newline = line - 1
            difference = int(line[1])-int(newline[1])
            
            
print("Your net income is", netincome_dollar)
print('Total Months', count)
print(difference)


