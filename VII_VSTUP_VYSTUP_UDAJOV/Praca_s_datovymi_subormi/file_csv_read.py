# file_csv_read.py
import csv

# opening the CSV file
with open(r'C:\Users\tomast\Documents\sss-trencin\Vyuka\Aplikovana_Informatika\VII_VSTUP_VÝSTUP_ÚDAJOV\Praca_s_datovymi_subormi\Giants03.csv', mode='r') as file:
                    
# reading the CSV file
    csvFile = csv.reader(file)
                    
# displaying the contents of the CSV file
    for lines in csvFile:
        print(lines)
