import os
import csv

# Define variables
total_votes = 0
candidate_votes = {}
candidates = []
winner = ""

# Path to the CSV file
csvpath = os.path.join('election_data.csv')

# Read the CSV file
with open(csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader)  # Skip header row
    
    # Iterate over each row in the CSV file
    for row in csvreader:
        # Count total votes cast
        total_votes += 1
        
        # Extract candidate's name from the row
        candidate_name = row[2]
        
        # Add candidate to the list if not already present
        if candidate_name not in candidates:
            candidates.append(candidate_name)
            candidate_votes[candidate_name] = 0
        
        # Increment candidate's vote count
        candidate_votes[candidate_name] += 1

# Calculate the percentage of votes each candidate won
candidate_percentages = {candidate: (votes / total_votes) * 100 for candidate, votes in candidate_votes.items()}

# Determine the winner based on the candidate with the most votes
winner = max(candidate_votes, key=candidate_votes.get)

# Print the analysis results
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")
for candidate in candidates:
    print(f"{candidate}: {candidate_percentages[candidate]:.3f}% ({candidate_votes[candidate]})")
print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")
