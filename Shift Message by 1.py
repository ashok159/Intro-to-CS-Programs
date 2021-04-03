#Name: Ashok Surujdeo
#Email: Ashok.Surujdeo65@myhunter.cuny.edu
#Date: February 9, 2021
#This program creates a message and prints each character, its Unicode number +1 and the character corresponding to that number.

myString = "hello"

for c in myString:
    print(c, ord(c)+1, chr(ord(c)+1))

message = input("Please enter a word:")

for c in message:
    print(c, ord(c)+1, chr(ord(c)+1))


