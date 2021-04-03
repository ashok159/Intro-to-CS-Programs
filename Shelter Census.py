#Name: Ashok Surujdeo
#Email: Ashok.Surujdeo65@myhunter.cuny.edu
#Date: March 15, 2021
#This program runs: Shelter Census

import pandas as pd
import matplotlib.pyplot as plt

data = input("Enter name of input file: ")
newname = input("Enter name of output file: ")

homeless = pd.read_csv(data)
homeless["Fraction Children"] = homeless["Total Children in Shelter"]/homeless["Total Individuals in Shelter"]
homeless.plot(x = "Date of Census", y = "Fraction Children")

fig = plt.gcf()
fig.savefig(newname)
