#Name: Ashok Surujdeo
#Email: Ashok.Surujdeo65@myhunter.cuny.edu
#Date: February 9, 2021
#This program runs: Encrypted Message

word = input("Enter a word:")
for i in word:
    newword = ord(i)+13
    if (newword > ord("Z")):
        newword = newword - ord("Z")+ord("A")-1
    print(chr(newword), end="")
