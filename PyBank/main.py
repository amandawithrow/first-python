import os
import csv

# Path to collect data from CSV file
bank_csv = os.path.join("budget_data.csv")

#declare variable for counting months
months = 0

#declare variable for total profit/loss
net_total = 0

#declare variable to store previous month profit/loss to find change
prev = 0

#declare lists to find greatest increase and decrease later
calendar = []
profit = []

# Read in the CSV file
with open(bank_csv, 'r') as csvfile:
    
    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')
    
    #skip header row
    header = next(csvreader)

    #start with first row, so that first iteration of loop has something to compare profit/loss to
    first_row = next(csvreader)
    months += 1
    month_total = float(first_row[1])
    net_total = net_total + month_total
    calendar.append(first_row[0])
    profit.append(0)
    prev = int(first_row[1])

    #Loop through data to count rows, get net total profit/loss, and add to calendar and profit lists
    for row in csvreader:
        
        months += 1
        month_total = float(row[1])
        net_total = net_total + month_total
        calendar.append(row[0])
        profit.append(int(row[1]) - prev)
        prev = int(row[1])
        
#calculate net average profit/loss
sum_profit= sum(profit)
avg_profit = round(sum_profit/(months-1), 2)

#Find Greatest increase in profits
maxpos = profit.index(max(profit))
minpos = profit.index(min(profit))

#print summary
print("Finanacial Analysis")
print("---------------------------------")
print(f"Total Months: {months}")
print(f"Total: {net_total}")
print(f"Average Change: {avg_profit}")
print(f"Greatest Increase in Profits: {calendar[maxpos]}: {profit[maxpos]}")
print(f"Greatest Decrease in Profits: {calendar[minpos]}: {profit[minpos]}")

#print summary to file
with open("output.txt", "a") as w:
    print("Finanacial Analysis", file=w)
    print("---------------------------------", file=w)
    print(f"Total Months: {months}", file=w)
    print(f"Total: {net_total}", file=w)
    print(f"Average Change: {avg_profit}", file=w)
    print(f"Greatest Increase in Profits: {calendar[maxpos]}: {profit[maxpos]}", file=w)
    print(f"Greatest Decrease in Profits: {calendar[minpos]}: {profit[minpos]}", file=w)


