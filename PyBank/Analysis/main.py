#creating file paths
import os
#opening csv file
import csv
from datetime import date
#load financial data and define as string
text_output = ""
def load_budget_data(budget_data_file_path):
    mylist = []
    with open(budget_data_file_path) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        diff = 0 #calculate difference in profit/losses between months
        tot_diff = 0 #total difference in profit/losses over the months
        net = 0 #net profit/loss
        prev = 0 #stores profit/loss based on previous month
        greatest_increase = 0 #greatest increase between two months
        greatest_increase_month = '' #store month in which greatest increase in profit happened
        greatest_decrease = 0 #greatest decrease in profit between two months
        greatest_decrease_month = '' #store month in which greatest decrease in profit happened
#total month count
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
    
    financial_report = ('Financial Analysis\n'
#separator line
    f'------------------------\n'

    f'Months {len(mylist)}\n' 
    f'Net Profit/Loss: {net}\n'
    f'Avg. Change: {average_change}\n'
    f'Greatest Increase: {greatest_increase_month}  ${greatest_increase}\n'
    f'Greatest Decrease: {greatest_decrease_month}  ${greatest_decrease}')
    
    return(financial_report)
#Resource         
file_path = "/Users/lizasadykova/Downloads/Starter_Code/PyBank/Resources/budget_data.csv"
text_out = load_budget_data(file_path)
# Print the analysis results
print(text_out)
# File path for the output .txt file
output_file_path = "/Users/lizasadykova/Downloads/Starter_Code/PyBank/analysis/budget_analysis.txt"

# Save the analysis results to the .txt file
with open(output_file_path, "w") as textfile:
   textfile.write(text_out)

print("Analysis results saved to 'budget_analysis.txt'")
