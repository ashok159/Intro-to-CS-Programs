#Name: Ashok Surujdeo
#Email: Ashok.Surujdeo65@myhunter.cuny.edu
#Date: February 9, 2021
#This program prints: Backwards Acronym

phrase = input("Your phrase in capital letters:")
print(phrase.upper())
newphrase = phrase.split()
newphrase.reverse()
acronym = ""
for i in newphrase:
    acronym = acronym + i[0].upper()

print("Acronym:", acronym)



