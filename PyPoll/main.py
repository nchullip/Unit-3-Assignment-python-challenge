# Importing Modules
import os, csv

# Initializing Variables
tot_votes = 0
candidate_list = []
vot_counts = {}
vote_share_perc = []
max = 0
winner = ""

# Fetching the Dataset
csvpath = os.path.join('election_data.csv')



with open(csvpath, newline='') as csvfile:
	# Creating the  CSV reader object
	csvreader = csv.reader(csvfile, delimiter=',')
	next(csvreader, None)

	# Traversing through each row in the CSV
	for row in csvreader:
		vot_id = row[0]
		county = row[1]
		candidate = row[2]
		if candidate in candidate_list:
			vot_counts[candidate] +=1
		else:
			candidate_list.append(candidate)
			vot_counts[candidate] = 1
		tot_votes += 1

for i in range(len(candidate_list)):
	vote_share = round((vot_counts[candidate_list[i]]/tot_votes)*100, 3)
	vote_share_perc.append(vote_share)
	if vot_counts[candidate_list[i]] > max:
		max = vot_counts[candidate_list[i]]
		winner = candidate_list[i]

# Creating Output Directory
if not os.path.exists("Output"):
	os.makedirs("Output")

# Creating Output Text Document and populating output values
f= open("Output/Election Results.txt","w+")
f.write("Election Results \n")
f.write("------------------------------------- \n")
f.write("Total Votes: " + str(tot_votes) + "\n")
f.write("------------------------------------- \n")
for i in range(len(candidate_list)):
	f.write(str(candidate_list[i]) + ": " + str(vote_share_perc[i]) + "% (" + str(vot_counts[candidate_list[i]]) + ") \n")
f.write("------------------------------------- \n")
f.write("Winner: " + str(winner) + "\n")
f.write("------------------------------------- \n")
f.close()

# Display Output on the Terminal
print("Election Results")
print("-------------------------------------")
print("Total Votes: " + str(tot_votes))
print("-------------------------------------")
for i in range(len(candidate_list)):
	print(str(candidate_list[i]) + ": " + str(vote_share_perc[i]) + "% (" + str(vot_counts[candidate_list[i]]) + ")")
print("-------------------------------------")
print("Winner: " + str(winner))
print("------------------------------------- ")
