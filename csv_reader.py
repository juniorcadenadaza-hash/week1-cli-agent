import csv

# Open the file
with open("sample.csv", "r") as file:
    reader = csv.reader(file)
    
    # Skip the header row (name, age, hobby)
    next(reader) 
    
    # 1. Start the counter at 1 BEFORE the loop starts
    row_number = 1

    for row in reader:
        # 2. Print the number, then the data from the columns
        # row[0] is Name, row[1] is Age, row[2] is Hobby
        print(str(row_number) + ". Name: " + row[0] + ", Age: " + row[1])
        
        # 3. CRITICAL: Increase the number by 1 for the next row
        row_number = row_number + 1