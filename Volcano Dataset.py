#Name: Ashok Surujdeo
#Email: Ashok.Surujdeo65@myhunter.cuny.edu
#Date: March 9, 2021
#This program runs: Volcanoes Dataset

import pandas as pd

file = input("Enter file name: ")
volcano = pd.read_csv(file)

rocktype = volcano.groupby('Dominant Rock Type')
print("The average height per rock type is as follows: ")
print(rocktype['Elevation (Meters)'].mean())

italy = volcano.groupby('Country').get_group('Italy')
print("The tallest volcano in Italy is", italy['Elevation (Meters)'].max(), "meters high.")
