#import dependencies
import pandas as pd
import os

#Read Poll csv file
file_path = os.path.join('Resources','election_data.csv')

#Read file into a dataframe
poll_df = pd.read_csv(file_path)
poll_df.head()

#unique candidates
candidateList = poll_df['Candidate'].unique()


#vote counts per candidate
voteCounts = poll_df['Candidate'].value_counts()


#total votes cast
totalVotes = voteCounts.sum()



#create a dataframe to hold all the values
new_df = pd.DataFrame({"Votes":voteCounts,
			"Percent":(voteCounts/totalVotes * 100)
			})


#reset indexes 
final_df = new_df.reset_index()

#rename index column to Candidate
renamed_df = final_df.rename(columns={"index":"Candidate"})



#winner of the election
winner = renamed_df['Votes'].max()
winn = renamed_df.loc[renamed_df['Votes'] == winner,:]
winningCandidate = winn['Candidate']


#print to screen
print ("\nElection Results")
print ("----------------------")
print (f"Total votes: {totalVotes}")
print ("----------------------")
for index,candidate in renamed_df.iterrows():
	print(f"{candidate['Candidate']}: {round(candidate['Percent'],3)}% ({candidate['Votes']})")
print ("----------------------")
print (f"Winner: {winningCandidate[0]}")
print ("----------------------\n")


#path to output text file
txt_output = os.path.join("Output", "PyPoll_text_output.txt")

#Open file in write mode and specify variable to hold contents
with open(txt_output, 'w', newline = "") as txt_file:
	#initialize txt writer
	txt_file.write(f"\nElection Results")
	txt_file.write(f"\n----------------------")
	txt_file.write (f"\nTotal votes: {totalVotes}")
	txt_file.write ("\n----------------------")
	for index,candidate in renamed_df.iterrows():
		txt_file.write(f"\n{candidate['Candidate']}: {round(candidate['Percent'],3)}% ({candidate['Votes']})")
	txt_file.write ("\n----------------------")
	txt_file.write (f"\nWinner: {winningCandidate[0]}")
	txt_file.write ("\n----------------------\n")


	