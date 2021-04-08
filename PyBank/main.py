#Coded by: Mehul Parekh

## PyBank
# In this challenge, you are tasked with creating a Python script for analyzing the financial records of your company. You will give a set of financial data called budget_data.csv. The dataset is composed of two columns: Date and Profit/Losses. (Thankfully, your company has rather lax standards for accounting so the records are simple.)
# Your task is to create a Python script that analyzes the records to calculate each of the following:
# The total number of months included in the dataset
# The net total amount of "Profit/Losses" over the entire period
# Calculate the changes in "Profit/Losses" over the entire period, then find the average of those changes
# The greatest increase in profits (date and amount) over the entire period
# The greatest decrease in losses (date and amount) over the entire period
# In addition, your final script should both print the analysis to the terminal and export a text file with the results.

import os
import csv
# from csv import DictReader
from collections import deque

budgetdata_path = os.path.join('Resources', 'budget_data.csv')

#empty list to store data
date = []
prof_loss = []
prof_change = []
prof_change_mod = []


#open and read csv file
with open(budgetdata_path) as budgetdata_handler:
	#when a command is made, budgetdata_object will pass it in a list (separated by commas)
	budgetdata_object = csv.reader(budgetdata_handler, delimiter=',')
	budgetdata_header = next(budgetdata_object)

	for row in budgetdata_object:
	#Total Months
		date.append(row[0])
		total_month_count = len(date)
	#Total
		prof_loss.append(int(row[1]))
		net_total = sum(prof_loss)
	
	#Average Change
	for row in range(len(prof_loss) - 1):
		change = prof_loss[row + 1] - prof_loss[row]
		prof_change.append(change)
		net_prof = sum(prof_change)
		average_change = round(net_prof / len(prof_change), 2)

	#Greatest Increase/Decrease in Profit
	for row in range(len(prof_change)):
		maxval = max(prof_change)
		minval = min(prof_change)

	#Corresponding Dates
	prof_change_mod = deque(prof_change)
	prof_change_mod.appendleft(1)
	combolist = dict(zip(prof_change_mod, date))
	
#Output
print(f"Financial Analysis")
print(f"--------------------------------")
print(f"Total Months: {total_month_count}")
print(f"Total: ${net_total}")
print(f"Average Change: ${average_change}")
print(f"Greatest Increase in Profits: {combolist[maxval]} (${maxval})")
print(f"Greatest Decrease in Profits: {combolist[minval]} (${minval})")

# File to write to:
output_path = os.path.join("Analysis", "PyBankResults.txt")
with open(output_path, 'w', newline='') as txthandler:
	txthandler.write(f"Financial Analysis\n")
	txthandler.write(f"--------------------------------\n")
	txthandler.write(f"Total Months: {total_month_count}\n")
	txthandler.write(f"Total: ${net_total}\n")
	txthandler.write(f"Average Change: ${average_change}\n")
	txthandler.write(f"Greatest Increase in Profits: {combolist[maxval]} (${maxval})\n")
	txthandler.write(f"Greatest Decrease in Profits: {combolist[minval]} (${minval})\n")


