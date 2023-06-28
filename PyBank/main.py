# Module 3 Challenge: python-challenge
# Author: Daiana Spataru
# Date: June 24, 2023

# PyBank is a python script developed to analyze company financial records from a financial dataset called budget_csv.
# The dataset is composed of two columns: "Date" and "Profit/Losses". 
# The Python script analyzes the records to calculate each of the following values:
    # The total number of months included in the dataset.
    # The net total amount of "Profit/Losses" over the entire period.
    # The changes in "Profit/Losses" over the entire period, and then the average of those changes.
    # The greatest increase in profits (date and amount) over the entire period.
    # The greatest decrease in profits (date and amount) over the entire period.
# The PyBank script prints the analysis summary to the terminal and exports a text file with the results.

# importing the libraries needed to accomplish the tasks mentioned above
import os
import csv


# path to collect data from the Resources folder
budget_data_csv = os.path.join("Resources", "budget_data.csv")


# read in the CSV file and appending data to lists for each of manipulation
with open(budget_data_csv, 'r') as csvfile:

    csvreader = csv.reader(csvfile, delimiter = ',') # reading the csv file

    header = next(csvreader) # skipping the header file to not include in the count

    date = []
    profit_losses = []
    for row in csvreader:
        date.append(row[0])
        profit_losses.append(row[1])



# ---------------------------------
# performing the financial analysis
# ---------------------------------

# determining the number of rows in the csv file not including the header
row_count = sum(1 for i in range(len(date)))
    
# calculating the net total amount of "Profit/Losses" over the entire period
total_profit_losses = 0
for amount in profit_losses:
        total_profit_losses += int(amount)

# calculating the average changes between entries in the profit/losses column
delta = []
for i in range(len(profit_losses) - 1):
    delta.append(int(profit_losses[i + 1]) - int(profit_losses[i]))
average_change = round((sum(change for change in delta) / len(delta)), 2)

#finding the greatest increase in profit and the date associated with it
greatest_inc = max(delta)
greatest_inc_date = date[delta.index(greatest_inc) + 1]

#finding the greatest decrease in profit and the date associated with it
greatest_dec = min(delta)
greatest_dec_date = date[delta.index(greatest_dec) + 1]


# ----------------------------------------------------------------
# printing the election analysis data to the terminal
# ----------------------------------------------------------------
print("Financial Analysis\n\n------------------------------------\n")
print(f"Total Months: {row_count}\n")
print(f"Total: ${total_profit_losses}\n")
print(f"Average Change: ${average_change}\n")
print(f"Greatest Increase in Profits: {greatest_inc_date} (${greatest_inc}) \n")
print(f"Greatest Decrease in Profits: {greatest_dec_date} (${greatest_dec})")


# ----------------------------------------------------------------
# creating an output txt file to store the financial analysis data
# ----------------------------------------------------------------

with open("analysis\Financial_analysis.txt", "a") as f:
    print("Financial Analysis\n\n------------------------------------\n", file = f)
    print(f"Total Months: {row_count}\n", file = f)
    print(f"Total: ${total_profit_losses}\n", file = f)
    print(f"Average Change: ${average_change}\n", file = f)
    print(f"Greatest Increase in Profits: {greatest_inc_date} (${greatest_inc}) \n", file = f)
    print(f"Greatest Decrease in Profits: {greatest_dec_date} (${greatest_dec})", file = f)