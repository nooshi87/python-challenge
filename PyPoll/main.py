import os
import csv
#variable for total votes = 'count'
total_vote= 0
candidate_vote = 0
candidate_list = []
vote_numbers =[]
percent_list = []
county_list =[]
organized_list =[]
#Creating a path for input and output files
csvpath = os.path.join("Resources", "election_data.csv")
txtpath = os.path.join("analysis", "election_analysis.txt")

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    #Saving header as separate line item
    csvheader = next(csvreader)
    first_row = next(csvreader)
    candidate1 = str(first_row[2])
    candidate_vote = 1
    candidate_list.append (first_row[2])
    # counting number of lines
    total_vote = total_vote + 1
    for row in csvreader:
        total_vote = total_vote + 1
        if row[2] == candidate1:
            candidate_vote = candidate_vote + 1
        elif row[2] != candidate1: 
            candidate1 =row[2]
            candidate_list.append(candidate1)
            vote_numbers.append (candidate_vote)
            candidate_vote = 1
    lastvote = candidate_vote
    vote_numbers.append(candidate_vote)
    #creating a zipped list to ensure number of candidate entries and vote number per candidate & county line up
    organized_list = list(zip(candidate_list,vote_numbers))
    print(organized_list)


#Calculate total number of votes per candidate & percent votes rounded to 3 decimal points. Index numbers based on position in appended lists.

    x = vote_numbers[0]+ vote_numbers[3] + vote_numbers[6]
    percentx =round((x)/total_vote*100, 3)
    print (x, percentx)
    y = vote_numbers[1]+ vote_numbers[4] + vote_numbers[7]
    percenty =round((y)/total_vote*100, 3)
    print (y, percenty)
    z = vote_numbers[2]+ vote_numbers[5] + vote_numbers[8]
    percentz =round((z)/total_vote*100, 3)
    print (z, percentz)

    #Finding the winner:
    if max(x,y,z) == x:
        Winner = candidate_list[0]
    if max(x,y,z) ==y:
        Winner = candidate_list[1]
    elif max(x,y,z) ==z:
        Winner = candidate_list[2]

#print Election outputs to text file
output = f"Election Results\n" f"Total Votes: {total_vote}\n" f"{candidate_list[0]}: {percentx} ({x})\n" f"{candidate_list[1]}: {percenty} ({y})\n" f"{candidate_list[2]}: {percentx} ({z})\n"f"Winner: {Winner}\n"
with open(txtpath, "w") as txtfile:
    txtfile.write(output)



