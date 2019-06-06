#Import modules
import os
import csv
csvpath = os.path.join("election_data.csv")

#List Variables
Total_Votes = 0
Candidate = []
Candidate_Votes = []
Winner = 0
Winner_Name = ""
i = 0

# Loop thru file
with open(csvpath, newline="") as csvfile:
	csvreader = csv.reader(csvfile, delimiter=",")
	
	# Skip header
	next(csvreader, None)
	
    # Read one row at a time
	for row in csvreader:
		Total_Votes = Total_Votes + 1
		if row[2] not in Candidate:
			Candidate.append(row[2])
			Candidate_Votes.append(0)
		else:
			Candidate_Votes[Candidate.index(row[2])] = Candidate_Votes[Candidate.index(row[2])] + 1

# Designate winner
Winner = max(range(len(Candidate_Votes)), key = lambda x: Candidate_Votes[x])
Winner_Name = Candidate[int(Winner)]

# Print analysis
print("Election Results:")
print("-----------------------")
print("Total Votes: " + str(Total_Votes))
print("-----------------------")
while i <= (len(Candidate) - 1):
	print(Candidate[i] + ": " + str(round((Candidate_Votes[i]/Total_Votes * 100),2)) + "% (" + str(Candidate_Votes[i]) + ")")
	i = i + 1
print("-----------------------")
print("Winner: " + str(Winner_Name))

#Reset i for txt output
i = 0

# Output to txt
filepath = os.path.join("output","election_results_.txt")
with open(filepath, "w") as writefile:
    writefile.writelines("Election Results:"+ '\n')
    writefile.writelines("-----------------------"+ '\n')
    writefile.writelines("Total Votes: "+ '\n')
    writefile.writelines(str(Total_Votes)+ '\n')
    writefile.writelines("-----------------------"+ '\n')  
    while i <= (len(Candidate) - 1):
	    writefile.writelines(Candidate[i] + ": " + str(round((Candidate_Votes[i]/Total_Votes * 100),2)) + "% (" + str(Candidate_Votes[i]) + ")" + "\n")
	    i = i + 1
    writefile.writelines("-----------------------" + "\n")
    writefile.writelines("Winner: " + str(Winner_Name))