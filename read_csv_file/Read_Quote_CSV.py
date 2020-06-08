# To remove the quote, using optional parameter: quoting
import csv

with open("quote_csv.csv") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',', skipinitialspace=True, quoting=csv.QUOTE_ALL)
    for row in csv_reader:
        print(row)
