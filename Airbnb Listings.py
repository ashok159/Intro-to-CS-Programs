#Name: Ashok Surujdeo
#Email: Ashok.Surujdeo65@myhunter.cuny.edu
#Date: March 16, 2021
#This program runs: Airbnb Listings

import matplotlib.pyplot as plt
import pandas as pd

name = input("Enter name of input file: ")
newname = input("Enter name of output file: ")

airbnb = pd.read_csv(name)
borough = airbnb.groupby('neighbourhood_group')
price = borough['price'].mean()
price.plot.bar(x = 'Borough', y = 'Average Price')
plt.xlabel('Borough')
plt.ylabel('Average Price')

plt.gcf().subplots_adjust(bottom=0.25)
fig = plt.gcf()
fig.savefig(newname)
