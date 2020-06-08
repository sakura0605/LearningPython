
# 1. First line identifies each piece of data - the name of a data column
# 2. Every subsequent line is actual data and is limited by file size constraints.
# 3. A delimiter is the separator character is caller,
# not only the comma but also the tab (\t) or colon (:) or semi-colon(;) characters
# 4. Properly parsing a CSV file depends on using of delimiters.

# Solution 1: using build-in CSV library

# delimiter: defined in csv file
# skipinitialspace: remove initial space after delimiters

import csv

with open("employee_birthday.txt") as csv_file:
    line_count = 0
    csv_reader = csv.reader(csv_file, delimiter='|', skipinitialspace=True)
    for row in csv_reader:
        line_count += 1
        # print(", ".join(row))
        print(row)

print("line count = ", line_count)
print("===========================================")

# Solution 2: using Pandas library

import pandas as pd

data = pd.read_csv("employee_birthday.txt")
print(data)
data.head()

# Get current path
import os
print(os.getcwd())
# get all files in current path
print(os.listdir(os.getcwd()))

