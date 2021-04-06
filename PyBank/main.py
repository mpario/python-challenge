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
	
	for row in range(len(prof_loss) - 1):
		#Average Change
			change = prof_loss[row + 1] - prof_loss[row]
			prof_change.append(change)
			
			net_prof = sum(prof_change)
			average_change = round(net_prof / len(prof_change), 2)


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



