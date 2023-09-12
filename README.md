# Python Challenge
**Project Overview**

It's time to put away the Excel sheet and enter the world of programming with Python. In this assignment, you'll use the concepts you've learned to complete two Python challenges, PyBank and PyPoll. Both tasks present a real-world situation where your newly developed Python scripting skills come in handy.

**PyPoll Instructions**

In this Challenge, you are tasked with helping a small, rural town modernize its vote-counting process.

You will be given a set of poll data called election_data. The dataset is composed of three columns: "Voter ID", "County", and "Candidate". Your task is to create a Python script that analyzes the votes and calculates each of the following values: the total number of votes cast, a complete list of candidates who received votes, the percentage of votes each candidate won, the total number of votes each candidate won, and the winner of the election based on popular vote

**PyBank Instructions**

In this Challenge, you are tasked with creating a Python script to analyze the financial records of your company. You will be given a financial dataset called budget_data.csv. The dataset is composed of two columns: "Date" and "Profit/Losses".

Your task is to create a Python script that analyzes the records to calculate each of the following values:
The total number of months included in the dataset, the net total amount of "Profit/Losses" over the entire period, the changes in "Profit/Losses" over the entire period, and then the average of those changes, the greatest increase in profits (date and amount) over the entire period, and the greatest decrease in profits (date and amount) over the entire period

**Resources and Challenges**

The biggest challenge I ran into with the code was getting this error: 

Exception has occurred: FileNotFoundError
[Errno 2] No such file or directory: 'Resources/election_data.csv'
  File "/Users/lizasadykova/Downloads/Starter_Code/PyPoll/Resources/main.py", line 13, in <module>
    with open(load_data) as csv_file:
FileNotFoundError: [Errno 2] No such file or directory: 'Resources/election_data.csv'

But I figured it out by adding it to the working directory using the code, election_data = os.path.join("election_data.csv")

I used StackOverflow, my group, AskBCS, and the internet for assistance with writing the code as well as with the errors I encountered

