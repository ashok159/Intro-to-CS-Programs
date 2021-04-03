#Name: Ashok Surujdeo
#Email: Ashok.Surujdeo65@myhunter.cuny.edu
#Date: February 23, 2021
#This program runs: Marginal Tax Rate

income = int(input("Enter taxable income: "))

if income < 0:
    print("Error")
elif 0 <= income <= 9700:
    print("Marginal tax rate: 10%")
elif 9701 <= income <= 39475:
    print("Marginal tax rate: 12%")
elif 39476 <= income <= 84200:
    print("Marginal tax rate: 22%")
elif 84201 <= income <= 160725:
    print("Marginal tax rate: 24%")
elif 160726 <= income <= 204100:
    print("Marginal tax rate: 32%")
elif 204101 <= income <= 510300:
    print("Marginal tax rate: 35%")
elif income >= 510301:
    print("Marginal tax rate: 37%")

