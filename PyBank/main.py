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

budgetdata_path = os.path.join('Resources', 'budget_data.csv')

#empty list to store data
date = []
total_month_count = []
prof_loss = []
net_total = []
change = []

prof_change = []
# average_change = []


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

	#Greatest Increase/Decrease in Profits
	for row in range(len(prof_change)):
		maxval = max(prof_change)
		minval = min(prof_change)		
		#print(maxval)
		# print(prof_change.min)

		# max = prof_change.sort()
		# print(maxval)
		



		# for row in prof_change:
		# 	valuemax = prof_change[0]
		# 	print(value)
		# 	print(value.min)

			# if value < value + 1
			# 	print(value + 1)
			# else
			# 	print(value)


			# if row > row + 1
			# print(prof_change.max)
			# print(prof_change.min)


		#	pass
		#else
		#	prof_row

		#if (prof_row < prof_row+1):
		#	prof_change = 
		#elif(prof_row > prof_row+1):
		#	pass
		#else
		#	prof_row

		#Greatest Increase in Profits

		#Greatest Decrease in Profits

print(f"Financial Analysis")
print(f"--------------------------------")
print(f"Total Months: {total_month_count}")
print(f"Total: {net_total}")
print(f"Average Change: {average_change}")
print(f"Greatest Increase in Profits: {maxval}")
print(f"Greatest Decrease in Profits: {minval}")


#		total_month_count = len(date_count)

#		'fin_rec'.count()

#fin_rec_df["Date"].value_counts()
#print(f"Total months: {total_month_count}")



