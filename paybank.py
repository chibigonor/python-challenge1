import os
import csv

csvpath = os.path.join('Python-challenge1','python-challenge1', 'budget_data.csv')
print(csvpath)

# Initialize variables
column_sum = 0
row_count = 0
changes = []
previous_value = None
greatest_increase = {"date": None, "amount": float("-inf")}
greatest_decrease = {"date": None, "amount": float("inf")}

# Open the CSV file
with open(csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)  # Skip header row
    
    # Iterate over the rows in the CSV file
    for row in csvreader:
        # Extract the value from the second column
        value = float(row[1])
        
        # Calculate change from previous value (skipping first row)
        if previous_value is not None:
            change = value - previous_value
            changes.append(change)
            
            # Check for greatest increase and decrease
            if change > greatest_increase["amount"]:
                greatest_increase["amount"] = change
                greatest_increase["date"] = row[0]
            if change < greatest_decrease["amount"]:
                greatest_decrease["amount"] = change
                greatest_decrease["date"] = row[0]
        
        # Update previous value for the next iteration
        previous_value = value
        
        # Accumulate sum of the second column
        column_sum += value
        
        # Increment row count
        row_count += 1

# Calculate the average change
average_change = sum(changes) / len(changes)

# Print the results
print("Total months:", row_count)
print("Total:", column_sum)
print("Average change:", average_change)
print("Greatest increase in profits:", greatest_increase["date"], greatest_increase["amount"])
print("Greatest decrease in profits:", greatest_decrease["date"], greatest_decrease["amount"])
