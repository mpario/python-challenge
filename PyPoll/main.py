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

		#Winning candidate
		winning_candidate = {"Khan":khan_votes, "Correy":correy_votes, "Li":li_votes, "O'Tooley":otooley_votes}
		winner = max(winning_candidate, key=winning_candidate.get)


print(f"Election Results")
print(f"-----------------------")
print(f"Total Votes: {total_votes}")
print(f"-----------------------")
print(f"Khan: {khan_ratio}% ({khan_votes})")
print(f"Correy: {correy_ratio}% ({correy_votes})")
print(f"Li: {li_ratio}% ({li_votes})")
print(f"O'Tooley: {otooley_ratio}% ({otooley_votes})")
print(f"-----------------------")
print(f"Winner: {winner}")
print(f"-----------------------")



