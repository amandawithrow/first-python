import os
import csv
from datetime import datetime

# Path to collect data from CSV file
employee_csv = os.path.join("..", "employee_data.csv")

id = []
first_name = []
last_name = []
dob = []
ssn = []
state = []

#add state dictionary
us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
}
#read in CSV
with open(employee_csv, 'r') as csvfile:
    
    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')
    
    #skip header row
    header = next(csvreader)

    
    #iterate through rows in CSV making changes to each element, and storing into a list.
    
    for row in csvreader:
        #add id# to list
        id.append(row[0])

        #splitting name into 2 columns
        name_split = row[1].split(" ")
        first_name.append(name_split[0])
        last_name.append(name_split[1])

        #change date format
        oldformat = row[2]
        datetimeobject = datetime.strptime(oldformat, "%Y-%m-%d")
        newformat = datetimeobject.strftime("%m/%d/%Y")
        dob.append(newformat)

        #mask SSN
        num = row[3]
        new_num = "***-**" + num[-4:]
        ssn.append(new_num)

        #change to state abbreviation
        abbrev = us_state_abbrev.get(row[4])
        state.append(abbrev)

# zip lists together,  and write into new csv
new_employee_data = zip(id, first_name, last_name, dob, ssn, state)

# save the output file path
output_file = os.path.join("output.csv")

# open the output file, create a header row, and then write the zipped object to the csv
with open(output_file, "w", newline="") as datafile:
    writer = csv.writer(datafile)

    writer.writerow(["ID", "First Name", "Last Name", "DOB", "SSN", "State"])

    writer.writerows(new_employee_data)
    