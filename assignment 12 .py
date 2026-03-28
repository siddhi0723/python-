import csv

# Open your file (saved as csv.txt) in read mode
with open("csv.txt", "r") as file:
    reader = csv.reader(file)
    
    # Count the number of rows
    row_count = sum(1 for row in reader)

print("Total number of rows:", row_count)