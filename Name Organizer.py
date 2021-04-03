#Name: Ashok Surujdeo
#Date: February 16,2021
#Email: Ashok.Surujdeo65@myhunter.cuny.edu
#This program runs: Name Organizer

nameList = input("Please enter your list of names:")
persons = nameList.split(" - ")
for person in persons:
    names = person.split()
    upperWord = names[0]
    initial = upperWord[0]
    print(names[1] + ' ' + initial + ".")
