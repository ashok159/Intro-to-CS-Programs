#Name: Ashok Surujdeo
#Email: Ashok.Surujdeo65@myhunter.cuny.edu
#Date: March 23, 2021
#This program runs: Dinosaurs

import pandas as pd

filename = input("Enter file name: ")
dino = pd.read_csv(filename)
print("There are", dino['Name'].count(),"dinosaur genera.")

print("The number of dinosaur genera in each period:")
print(dino['Period'].value_counts())

print("The three most dinosaur-populated countries were:")
print(dino['Country'].value_counts()[:3])
