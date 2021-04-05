import os
import csv

electiondata_path = os.path.join('Resources', 'election_data.csv')

#empty list to store data
voter_id = []
county = []
candidate = []
total_votes = []

prof_change = []
average_change = []
inc_profits = []
dec_profits = []


#open and read csv file
with open(electiondata_path) as electiondata_handler:
	#when a command is made, electiondata_object will pass it in a list (separated by commas)
	electiondata_object = csv.reader(electiondata_handler, delimiter=',')
	electiondata_header = next(electiondata_object)
	#print(electiondata_header)

	for row in electiondata_object:
		#Total Votes
		voter_id.append(row[0])
		total_votes = len(voter_id)
		#Total
		# prof_row = prof_loss.append(int(row[1]))
		# net_total = sum(prof_loss)


print(f"Election Results")
print(f"--------------------------------")
print(f"Total Votes: {total_votes}")
print(f"--------------------------------")
print(f"Khan: ")
print(f"Correy: ")
print(f"Li: ")
print(f"O'Tooley: ")
