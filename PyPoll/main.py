import os
import csv

electiondata_path = os.path.join('Resources', 'election_data.csv')

#empty list to store data
voter_id = []
county = []
candidate = []
#total_votes = []

prof_change = []
average_change = []
inc_profits = []
dec_profits = []

khan_count = []
correy_count = []
li_count = []
otooley_count = []

# khan_count = 0
# correy_count = 0
# li_count = 0
# otooley_count = 0
khan_vote = 0
correy_vote = 0
li_vote = 0
otooley_vote = 0


#open and read csv file
with open(electiondata_path) as electiondata_handler:
	#when a command is made, electiondata_object will pass it in a list (separated by commas)
	electiondata_object = csv.reader(electiondata_handler, delimiter=',')
	electiondata_header = next(electiondata_object)
	#print(electiondata_header)

	for row in electiondata_object:
		# Total Votes
		voter_id.append(row[0])
		total_votes = len(voter_id)
		
		# Per Candidate
		candidate.append([row[2]])
		if (row[2] == "Khan"):
			khan_count.append(candidate)
			#khan_count += 1
			khan_vote = len(khan_count)
		elif (row[2] == "Correy"):
			correy_count.append(candidate)
			#correy_count += 1
			correy_vote = len(correy_count)
		elif (row[2] == "Li"):
			li_count.append(candidate)
			#li_count += 1
			li_vote = len(li_count)
		elif (row[2] == "O'Tooley"):
			otooley_count.append(candidate)
			#otooley_count += 1
			otooley_vote = len(otooley_count)

		# candidate.append([row[2]])
		# if (candidate == "Khan"):
		# 	khan_count += 1
		# 	khan_vote = len(khan_count)
		# elif (candidate == "Correy"):
		# 	correy_count += 1
		# 	correy_vote = len(correy_count)
		# elif (candidate == "Li"):
		# 	li_count += 1
		# 	li_vote = len(li_count)
		# elif (candidate == "O'Tooley"):
		# 	otooley_count += 1
		# 	otooley_vote = len(otooley_count)

# print(candidate.append([row[2]]))

print(f"Election Results")
print(f"--------------------------------")
print(f"Total Votes: {total_votes}")
print(f"--------------------------------")
print(f"Khan: {khan_vote}")
print(f"Correy: {correy_vote}")
print(f"Li: {li_vote}")
print(f"O'Tooley: {otooley_vote}")
