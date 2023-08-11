# Open function to open the file "LICENSE.txt"
# (same directory) in read mode and

file1 = open("LICENSE.txt", "w")

# store its reference in the variable file1
# and "SW_licencia.txt" in C:\Users\tomast\Documents\sss-trencin\Vyuka\Aplikovana_Informatika\VIII_PRÁCA_SO_SÚBORMI in file2

file2 = open(r"C:\Users\tomast\Documents\sss-trencin\Vyuka\Aplikovana_Informatika\VIII_PRÁCA_SO_SÚBORMI\SW_licencia.txt", "w+")

# zobrazit obsah suboru
file3 = open('LICENSE.txt', 'r')
file_contents = file3.read()
print(file_contents)

# Po dokončení nezabudnite súbor zavrieť.
file1.close()
file2.close()
file3.close()
