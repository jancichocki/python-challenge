import csv
from pathlib import Path

# Initialize variables for analysis
total_months = 0
total_profit_loss = 0
previous_month_profit_loss = 0
monthly_change = []
greatest_increase = ["", 0]
greatest_decrease = ["", float('inf')]

# Open and read the budget data file
with open(Path('budget_data.csv'), 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    header = next(csvreader)  # Skip the header row

    # Process each row in the CSV file
    for month in csvreader:
        total_months += 1
        current_month_profit_loss = int(month[1])
        total_profit_loss += current_month_profit_loss

        # Only calculate changes from the second month onwards
        if total_months > 1:
            change = current_month_profit_loss - previous_month_profit_loss
            monthly_change.append(change)

            # Check and update the greatest increase and decrease in profits
            if change > greatest_increase[1]:
                greatest_increase = [month[0], change]
            if change < greatest_decrease[1]:
                greatest_decrease = [month[0], change]

        previous_month_profit_loss = current_month_profit_loss

# Calculate the average change in profit/loss
average_change = sum(monthly_change) / len(monthly_change)

# Print the financial analysis results
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${total_profit_loss}")
print(f"Average  Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})")
print(f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})")

# Write the analysis to a text file
output_path = Path('financial_analysis.txt')
with open(output_path, 'w') as file:
    file.write("Financial Analysis\n")
    file.write("----------------------------\n")
    file.write(f"Total Months: {total_months}\n")
    file.write(f"Total: ${total_profit_loss}\n")
    file.write(f"Average  Change: ${average_change:.2f}\n")
    file.write(f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n")
    file.write(f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})\n")
