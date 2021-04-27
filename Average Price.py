#Name: Ashok Surujdeo
#Email: Ashok.Surujdeo65@myhunter.cuny.edu
#Date: April 13, 2021
#This program runs: Average Price

total = 0
itemCount = 0

price = float(input("Enter the price of an item: "))

while price >= 0:
    total = total + price
    itemCount = itemCount + 1
    price = float(input("Enter the price of an item: "))

average = total / itemCount
print("$",average)
        
