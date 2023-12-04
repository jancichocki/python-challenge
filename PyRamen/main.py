import csv

# Part 1: Read the Data
menu = []
with open('menu_data.csv', 'r') as file:
    csvreader = csv.reader(file)
    next(csvreader)  # Skip the header
    for row in csvreader:
        menu.append(row)

sales = []
with open('sales_data.csv', 'r') as file:
    csvreader = csv.reader(file)
    next(csvreader)  # Skip the header
    for row in csvreader:
        sales.append(row)

# Part 2: Manipulate the Data
report = {}

for sale in sales:
    quantity = int(sale[3])
    sales_item = sale[4]

    if sales_item not in report:
        report[sales_item] = {"01-count": 0, "02-revenue": 0, "03-cogs": 0, "04-profit": 0}

    for item in menu:
        if sales_item == item[0]:
            price = float(item[3])
            cost = float(item[4])
            profit = (price - cost) * quantity

            report[sales_item]["01-count"] += quantity
            report[sales_item]["02-revenue"] += price * quantity
            report[sales_item]["03-cogs"] += cost * quantity
            report[sales_item]["04-profit"] += profit

# An extra screen formatted report
print("Ramen Sales Report")
print("------------------")
for item, metrics in report.items():
    print(f"Item: {item}")
    for key, value in metrics.items():
        print(f"  {key}: {value}")
    print("------------------")

# Write out report to a text file
with open('ramen_report.txt', 'w') as file:
    for key, value in report.items():
        file.write(f"{key} {value}\n")
