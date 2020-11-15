#Import Moduels 
import os 
import csv 


total_votes = 0 
winner_count = 0 
khan_votes = 0
correy_votes = 0
li_votes = 0 
otooley_votes = 0


data = os.path.join('Resources', 'election_data.csv')

with open(data, 'r' ) as csvfile:
    csvreader = csv.reader(csvfile, delimiter =',')
    next(csvreader)

    for row in csvreader:
        #Total Votes
        total_votes += 1

        #Candidate vote count 
        if (row[2] == "Khan"):
            khan_votes += 1
        elif (row[2]== "Correy"):
            correy_votes += 1
        elif (row[2] == "Li"):
            li_votes += 1
        else:
            otooley_votes += 1
            

#Determine who has most votes
Candidates = {khan_votes : "Khan", correy_votes : "Correy", li_votes : "Li", otooley_votes : "Otooley"}
winner = Candidates.get(max(Candidates))
winners_vote_count = (max(Candidates))

print(winner)
print(winners_vote_count)

# Percentage of votes 
khan_percentage = (khan_votes/total_votes)
correy_percentage = (correy_votes/total_votes)
li_percentage = (li_votes/total_votes) 
otooley_percentage = (otooley_votes/total_votes)


#Terminal Printout 
print(f"Election Results")
print(f"-" * 30)
print(f"Total Votes: {total_votes}")
print(f"-" * 30)
print(f"Kahn: {khan_percentage:.3%} ({khan_votes})")
print(f"Correy: {correy_percentage:.3%} ({correy_votes})")
print(f"Li: {li_percentage:.3%} ({li_votes})")
print(f"O'Tooley: {otooley_percentage:.3%} ({otooley_votes})")
print(f"-" * 30)
print(f"Winner: {winner}")
print(f"-" * 30)


#Output.txt
output_file = os.path.join('Analysis', 'Output.txt')

with open(output_file, "w") as new:
    new.write(f"Election Results\n")
    new.write("--------------------------\n")
    new.write(f"Total Votes: {total_votes}\n")
    new.write("--------------------------\n")
    new.write(f"Kahn: {khan_percentage:.3%} ({khan_votes})\n")
    new.write(f"Correy: {correy_percentage:.3%} ({correy_votes})\n")
    new.write(f"Li: {li_percentage:.3%} ({li_votes})\n")
    new.write(f"O'Tooley: {otooley_percentage:.3%} ({otooley_votes})")
    new.write("--------------------------\n")
    new.write(f"Winner: {winner}")
    new.write("--------------------------\n")