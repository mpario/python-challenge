import os
import csv

budgetdata_path = os.path.join('Resources', 'budget_data.csv')

#empty list to store data
date = []
total_month_count = []
prof_loss = []
net_total = []

prof_change = []
# average_change = []


#open and read csv file
with open(budgetdata_path) as budgetdata_handler:
	#when a command is made, budgetdata_object will pass it in a list (separated by commas)
	budgetdata_object = csv.reader(budgetdata_handler, delimiter=',')
	budgetdata_header = next(budgetdata_object)
	#print(budgetdata_header)

	for row in budgetdata_object:
		#Total Months
		date.append(row[0])
		total_month_count = len(date)
		#Total
		prof_loss.append(int(row[1]))
		net_total = sum(prof_loss)
	
	# print(f"{prof_loss}")	
	
	for row in prof_loss:
		#Average Change
		if (row < (row + 1)):
			change = ((row + 1) - row)
			prof_change.append(change)
		elif (row > (row + 1)):
			change = (row - (row + 1))
			prof_change.append(change)
		else:
			change == 0
			prof_change.append(change)



	# print(f"{avgchange}")
	print(prof_change)
	net_prof = sum(prof_change)
	average_change = net_prof / total_month_count


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
print(f"Greatest Increase in Profits: ")
print(f"Greatest Decrease in Profits: ")


#		total_month_count = len(date_count)

#		'fin_rec'.count()

#fin_rec_df["Date"].value_counts()
#print(f"Total months: {total_month_count}")



