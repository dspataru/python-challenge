# Module 3 Challenge: python-challenge
# Author: Daiana Spataru
# Date: June 24, 2023

# PyPoll is a python script designed to help a small, rural town modernize its vote-counting process. 
# The script runs on poll data called election_data.csv which is composed of three columns: "Voter ID", "County", and "Candidate". 
# PyPoll analyzes the votes and calculates each of the following values:
    # The total number of votes cast.
    # A complete list of candidates who received votes.
    # The percentage of votes each candidate won.
    # The total number of votes each candidate won.
    # The winner of the election based on popular vote.
# The PyPoll script prints the analysis summary to the terminal and exports a text file with the results.


# importing the libraries needed to accomplish the tasks mentioned above
import os
import csv
import operator
import subprocess


# path to collect data from the Resources folder
election_data_csv = os.path.join("Resources", "election_data.csv")


# read in the CSV file and appending data to lists for each of manipulation
with open(election_data_csv, 'r') as csvfile:

    csvreader = csv.reader(csvfile, delimiter = ',') # reading the csv file

    header = next(csvreader) # skipping the header file to not include in the count

    # ordering the csv file by Candidate
    sorted_election_data = sorted(csvreader, key=operator.itemgetter(2), reverse=False)
    
    ballot_ID = []
    country = []
    candidate = []
    for row in sorted_election_data:
        ballot_ID.append(row[0])
        country.append(row[1])
        candidate.append(row[2])


# ---------------------------------
# performing the election analysis
# ---------------------------------

# determining the number of rows in the csv file not including the header to find the total number of votes
num_votes = sum(1 for i in range(len(ballot_ID)))

# finding a complete list of candidates who received votes, along with the total number of votes per each candidate
candidate_name = []
num_votes_per_candidate = []
sum = 0

for i in range(len(candidate)):
    if i == 0: 
        candidate_name.append(candidate[i])
    if candidate[i] != candidate [i - 1] and i != 0:
        candidate_name.append(candidate[i])
        num_votes_per_candidate.append(sum)
        sum = 0
    sum += 1
num_votes_per_candidate.append(sum) #appending the number of votes from the last candidate to the num_votes_per_candidate list


# calculating the percentage of votes each candidate won
percentage_votes = []
for i in range(len(num_votes_per_candidate)):
    percentage_votes.append(round((num_votes_per_candidate[i] / num_votes) * 100, 3))


# calculating the candidate winner based on total number of votes
winner_name = candidate_name[num_votes_per_candidate.index(max(num_votes_per_candidate))]


# ----------------------------------------------------------------
# printing the election analysis data to the terminal
# ----------------------------------------------------------------

print("Election Results\n\n------------------------------------\n")
print(f"Total Votes: {num_votes} \n\n------------------------------------\n")

for i in range(len(candidate_name)):
    print(f"{candidate_name[i]}: {percentage_votes[i]}% ({num_votes_per_candidate[i]}) \n")

print("------------------------------------\n")
print(f"Winner: {winner_name} \n\n------------------------------------")



# ----------------------------------------------------------------
# creating an output txt file to store the election analysis data
# ----------------------------------------------------------------

with open("analysis\Election_results.txt", "a") as f:
    print("Election Results\n\n------------------------------------\n", file = f)
    print(f"Total Votes: {num_votes} \n\n------------------------------------\n", file = f)
    
    for i in range(len(candidate_name)):
        print(f"{candidate_name[i]}: {percentage_votes[i]}% ({num_votes_per_candidate[i]}) \n", file = f)
    
    print("------------------------------------\n", file = f)
    print(f"Winner: {winner_name} \n\n------------------------------------", file = f)