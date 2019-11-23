# Modules
import os

import csv

 # Set path for file
csvpath = os.path.join('..', "Resources", "budget_data.csv")

# Things that I have tried to see if csvpath has been activated
# open(csvpath)
# print(csvpath)


# Open the CSV

with open(csvpath, newline="") as csvfile:

    csvreader = csv.reader(csvfile, delimiter=" ")

    print(csvreader)

    for row in csvreader:
        print(row)

        




