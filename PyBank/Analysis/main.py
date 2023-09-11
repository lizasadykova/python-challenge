# This will allow us to create file paths across operating systems
import os

# Module for reading CSV files
import csv
from datetime import date

text_output = ""
def load_data(budget_data):
    mylist = []
    with open(budget_data) as csv_file:
        csv_reader = csv.DictReader(csv_file)

        diff = 0
        tot_diff = 0
        net = 0
        prev = 0
        greatest_increase = 0
        greatest_increase_month = ''
        greatest_decrease = 0
        greatest_decrease_month = ''
        # We count total months
        for row in csv_reader:
            profit_loss = int(row['Profit/Losses'])
            net = net + profit_loss
            diff = profit_loss - prev
            prev = profit_loss
            
            if diff > greatest_increase:
                greatest_increase = diff
                greatest_increase_month = row['Date']

            if diff < greatest_decrease:
                greatest_decrease = diff
                greatest_decrease_month = row['Date'] 
            
            if len(mylist) > 0:
                tot_diff = tot_diff + diff

            mylist.append(row)

    average_change = round(tot_diff / (len(mylist) -1), 2)
    
    text_output = ('Financial Analysis\n'
    
    f'------------------------\n'

    f'Months {len(mylist)}\n' 
    f'Net Profit/Loss: {net}\n'
    f'Avg. Change: {average_change}\n'
    f'Greatest Increase: {greatest_increase_month}  ${greatest_increase}\n'
    f'Greatest Decrease: {greatest_decrease_month}  ${greatest_decrease}')
    
    return(text_output)
#Resource         
file_path = "/Users/lizasadykova/Downloads/Starter_Code/PyBank/Resources/budget_data.csv"
text_out = load_data(file_path)
# Print the analysis results
print(text_out)
# File path for the output .txt file
output_file_path = "/Users/lizasadykova/Downloads/Starter_Code/PyBank/analysis/budget_analysis.txt"

# Save the analysis results to the .txt file
with open(output_file_path, "w") as textfile:
   textfile.write(text_out)

print("Analysis results saved to 'budget_analysis.txt'")
