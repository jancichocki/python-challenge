"""
This module performs financial analysis for PyBank. It reads financial data from a CSV file, 
calculates various statistics such as total months, total profit/loss, average change, 
and greatest increase/decrease in profits, and outputs the results both to the console and a text file.
"""

import csv

class BudgetDataAnalyzer:
    """A class to analyze budget data from a CSV file."""

    def __init__(self, filepath):
        """Initialize the BudgetDataAnalyzer with the path to the data file."""
        self.filepath = filepath
        self.total_months = 0
        self.total_profit_loss = 0
        self.monthly_changes = []
        self.greatest_increase = ['', 0]
        self.greatest_decrease = ['', 0]

    def analyze(self):
        """Analyze the budget data for total months, profit/loss, and changes."""
        with open(self.filepath, 'r') as csvfile:
            data = csv.reader(csvfile)
            next(data)  # Skip the header

            previous_month_profit_loss = None
            for month in data:
                self.total_months += 1
                current_month_profit_loss = int(month[1])
                self.total_profit_loss += current_month_profit_loss

                if previous_month_profit_loss is not None:
                    change = current_month_profit_loss - previous_month_profit_loss
                    self.monthly_changes.append(change)

                    # Update greatest increase and decrease
                    if change > self.greatest_increase[1]:
                        self.greatest_increase = [month[0], change]
                    if change < self.greatest_decrease[1]:
                        self.greatest_decrease = [month[0], change]

                previous_month_profit_loss = current_month_profit_loss

    def print_results(self):
        """Print the results of the analysis."""
        average_change = sum(self.monthly_changes) / len(self.monthly_changes) if self.monthly_changes else 0
        print("Financial Analysis")
        print("----------------------------")
        print(f"Total Months: {self.total_months}")
        print(f"Total: ${self.total_profit_loss}")
        print(f"Average Change: ${average_change:.2f}")
        print(f"Greatest Increase in Profits: {self.greatest_increase[0]} (${self.greatest_increase[1]})")
        print(f"Greatest Decrease in Profits: {self.greatest_decrease[0]} (${self.greatest_decrease[1]})")

# Creating an instance of the BudgetDataAnalyzer and using it to analyze the data
analyzer = BudgetDataAnalyzer('budget_data.csv')
analyzer.analyze()
analyzer.print_results()
