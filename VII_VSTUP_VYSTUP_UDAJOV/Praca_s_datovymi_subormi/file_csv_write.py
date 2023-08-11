# file_csv_write.py

# Python program to demonstrate
# writing to CSV

import csv

# field names
header = ['Name', 'Branch', 'Year', 'CGPA']

# data rows of csv file
data = [
    ['Nikhil', 'COE', '2', '9.0'],

    ['Sanchit', 'COE', '2', '9.1'],

    ['Aditya', 'IT', '2', '9.3'],

    ['Sagar', 'SE', '1', '9.5'],

    ['Prateek', 'MCE', '3', '7.8'],

    ['Sahil', 'EP', '2', '9.1']
]

# meno csv suboru
filename = "countries.csv"

# zapis do csv suboru
with open(filename, 'w', encoding='UTF8', newline='') as csvfail:

	# vytvorenie obektu pre zapis do csv
    writer = csv.writer(csvfail)

    # zapis jedneho riadku - hlavicky csv suboru (nazvy poli v csv)
    writer.writerow(header)

    # zapis jednotlivych riadkov s udajmi
    writer.writerows(data)