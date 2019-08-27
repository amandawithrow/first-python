import os
import csv

# Path to collect data from CSV file
election_csv = os.path.join("..", "election_data.csv")

#declare variable for counting total votes
total_votes = 0
count = 0

#declare list of candidates that people voted for
candidates = []
vote = []

# Read in the CSV file
with open(election_csv, 'r') as csvfile:
    
    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')
    
    #skip header row
    header = next(csvreader)

    #Loop through data to count rows and get net total profit/loss
    for row in csvreader:
        total_votes += 1
        candidates.append(row[2])

#sort list alphabetically
candidates.sort()

#print summary table
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")

#set counter for while loop to zero
x = 0

#create dictionary to store candidates and the number of votes
polling = {}

#run while loop to count how many votes for each candidate
while x < total_votes:
    #count number of votes for candidate as represented by list made earlier
    count = candidates.count(str(candidates[x]))
    
    #print candidate name, percentage of the vote, and raw total of votes to summary table
    print(f'{candidates[x]}: {round((int(count)/total_votes)*100, 2)}% ({int(count)})')
    
    #store candidate name in variable
    name = candidates[x]

    #add key value pair of candidate name and vote count to dictionary
    polling.update({name :count})
    
    #increment counter to next candidate
    x = x+count

print("-------------------------")

#find max value in dictionary
def keymaxval(d):
    v = list(d.values())
    k = list(d.keys())
    return k[v.index(max(v))]

print(f"Winner: {keymaxval(polling)}")
print("-------------------------")