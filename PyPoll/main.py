import os
import csv

electiondata_path = os.path.join('Resources', 'election_data.csv')

#empty list to store data
voter_id = []
county = []
candidate = []
#total_votes = []

khan_count = []
correy_count = []
li_count = []
otooley_count = []


khan_votes = 0
correy_votes = 0
li_votes = 0
otooley_votes = 0


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
			khan_votes = len(khan_count)
			khan_ratio = round((khan_votes / total_votes) * 100, 3)
		elif (row[2] == "Correy"):
			correy_count.append(candidate)
			correy_votes = len(correy_count)
			correy_ratio = round((correy_votes / total_votes) * 100, 3)
		elif (row[2] == "Li"):
			li_count.append(candidate)
			li_votes = len(li_count)
			li_ratio = round((li_votes / total_votes) * 100, 3)
		elif (row[2] == "O'Tooley"):
			otooley_count.append(candidate)
			otooley_votes = len(otooley_count)
			otooley_ratio = round((otooley_votes / total_votes) * 100, 3)



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
print(f"----------------------")
print(f"Total Votes: {total_votes}")
print(f"----------------------")
print(f"Khan: {khan_ratio}% ({khan_votes})")
print(f"Correy: {correy_ratio}% ({correy_votes})")
print(f"Li: {li_ratio}% ({li_votes})")
print(f"O'Tooley: {otooley_ratio}% ({otooley_votes})")
print(f"----------------------")
print(f"Winner: {}")
print(f"----------------------")



