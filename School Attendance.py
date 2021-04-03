#Name: Ashok Surujdeo
#Email: Ashok.Surujdeo65@myhunter.cuny.edu
#Date: March 16, 2021
#This program runs: School Attendance

import matplotlib.pyplot as plt
import pandas as pd

name = input("Enter name of input file: ")
newname = input("Enter name of output file: ")

df = pd.read_csv(name)
df["Date"] = pd.to_datetime(df["Date"].apply(str))
df["% Absent"] = (df["Absent"]/df["Enrolled"])*100
df.plot(x = "Date", y = "% Absent")

fig = plt.gcf()
fig.savefig(newname)
