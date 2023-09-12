import os
import csv
election_data = os.path.join("election_data.csv")

#lists
candidates = [] #names of candidates
num_votes = [] #number of votes each candidate receives
percent_votes = [] #percentage of total votes each candidate garners 
total_votes = 0 #counter for the total number of votes 

with open(election_data, newline = "") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    csv_header = next(csvreader)

    for row in csvreader:
        #vote-counter 
        total_votes += 1 
        candidate_name = row[2]

        if candidate_name not in candidates:
            candidates.append(candidate_name)
            num_votes.append(1)
        else:
            candidate_index = candidates.index(candidate_name)
            num_votes[candidate_index] += 1
            
    #percent_votes list 
    for votes in num_votes:
        percentage = (votes/total_votes) * 100
        percentage = round(percentage)
        percentage = "%.3f%%" % percentage
        percent_votes.append(percentage)
    
    #finding winner
    winner = max(num_votes)
    index = num_votes.index(winner)
    winning_candidate = candidates[index]

#results
print("Election Results")
print("--------------------------")
print(f"Total Votes: {str(total_votes)}")
print("--------------------------")
for i in range(len(candidates)):
    print(f"{candidates[i]}: {str(percent_votes[i])} ({str(num_votes[i])})")
print("--------------------------")
print(f"Winner: {winning_candidate}")
print("--------------------------")

#save analysis results to .txt file
output = open("output.txt", "w")
line1 = "Election Results"
line2 = "--------------------------"
line3 = str(f"Total Votes: {str(total_votes)}")
line4 = str("--------------------------")
output.write('{}\n{}\n{}\n{}\n'.format(line1, line2, line3, line4))
for i in range(len(candidates)):
    line = str(f"{candidates[i]}: {str(percent_votes[i])} ({str(num_votes[i])})")
    output.write('{}\n'.format(line))
line5 = "--------------------------"
line6 = str(f"Winner: {winning_candidate}")
line7 = "--------------------------"
output.write('{}\n{}\n{}\n'.format(line5, line6, line7))
