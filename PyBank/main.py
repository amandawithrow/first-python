import os
import csv

# Path to collect data from CSV file
bank_csv = os.path.join("budget_data.csv")

#declare variable for counting months
months = 0

#declare variable for total profit/loss
net_total = 0

# Read in the CSV file
with open(bank_csv, 'r') as csvfile:
    
    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')
    
    #skip header row
    header = next(csvreader)
    
    #Loop through data to count rows and get net total profit/loss
    for row in csvreader:
        months += 1
        month_total = float(row[1])
        net_total = net_total + month_total

#print summary
print("Finanacial Analysis")
print("---------------------------------")
print(f"Total Months: {months}")
print(f"Total: {net_total}")



