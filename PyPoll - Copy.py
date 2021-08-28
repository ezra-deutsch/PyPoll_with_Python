# The data we need to retrieve
##1. The total number of votes cast
##2. A complete list of candidates who received votes
#3. The % of votes each candidate won
##4. The total number of votes each candidate won
#5. The winner of the election based on popular vote

# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("Analysis", "election_analysis.txt")

#Initialize variables and lists: total_votes, candidate_options
total_votes = 0
candidate_options = []
candidate_votes = {}

winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file.
with open(file_to_load) as election_data:
    # Read the file object with the reader function.  #To do: read and analyze the data here.
    file_reader = csv.reader(election_data)
    #Read and print the header row
    headers = next(file_reader)
    #Print each row in the CSV file.
    for row in file_reader:
        #Add to the total vote count.
        total_votes+=1
        #Print the candidate name from each row
        candidate_name = row[2]
        #If the candidate does not match any exsisting candidate...
        if candidate_name not in candidate_options:
            #add the candidate name to the candidate list
            candidate_options.append(candidate_name)
            #Instantiate candidate key and track vote count
            candidate_votes[candidate_name] = 0
        #increment each vote cast with the correct candidate
        candidate_votes[candidate_name] +=1

# Save results to our text file.
with open(file_to_save, "w") as txt_file:
    #Print the final vote count to the terminal
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes:{total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end="")
    #Save the final vote count to the text file
    txt_file.write(election_results)
    #vote_percentage = (votes / total_votes) * 100
    for candidate_name in candidate_votes:
        votes = candidate_votes[candidate_name]
        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results = (
            f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        #print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        print(candidate_results)
        txt_file.write(candidate_results)
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_percentage = vote_percentage
            winning_candidate = candidate_name
        #print(f"{candidate_name}: received {vote_percentage:.1f}% of the vote.")
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)
    txt_file.write(winning_candidate_summary)


    #Print the total votes
    #print(total_votes)
    #print(candidate_options)
    #print(candidate_votes)


