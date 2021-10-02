#import data 
import csv
import os

#Load election data
inputFile = os.path.join('Resources\election_data.csv')


#variables
totalVotes = 0
Candidate = []
candidateVotes ={}
winningcount = 0
Winner = ""

#read csv file
with open(inputFile) as electionData:
    csvreader = csv.reader(electionData)

    #read header
    header = next(csvreader)


    # List of Candidates- 0 = voter id; 1-county;- 2- candidate
    for row in csvreader:
        totalVotes += 1

        #check to see if the candidate is in the list of candidates
        if row[2] not in Candidate:
            Candidate.append(row[2])

            #start the count at 1 for votes
            candidateVotes[row[2]] = 1

        else:
            #add to the list of votes for the candidate
            candidateVotes[row[2]] += 1

voteOutput = ""

for Candidate in candidateVotes:
    # Get total votes and percentage
    votes = candidateVotes.get(Candidate)
    votePCT =(float(votes) / float(totalVotes)) * 100.00
    voteOutput += f"{Candidate}: {votePCT:.2f}%\n"

    #compare the votes to find the winning count
    if votes > winningcount:
        winningcount = votes

        #update winner
        Winner = Candidate

#Variable to hold the output for the Winner's name
WinnerOutput = f"Winner:{Winner}\n"

#Output for election results
output = (
    f"\nElection Results\n"
    "----------------------------\n"
    f"Total Votes {totalVotes:,}\n"
    f"----------------------------\n"
    f"{voteOutput}"
    f"----------------------------\n"
    f"{Winner}"
)
 
print(output) 

#output for Election results
outputFile = os.path.join('Analysis',"ElectionResults.txt")
with open(outputFile, "w") as textfile:
    textfile.write(output)
