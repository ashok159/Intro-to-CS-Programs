#Name: Ashok Surujdeo
#Email: Ashok.Surujdeo65@myhunter.cuny.edu
#Date: March 2, 2021
#This program runs: Snow Count

import matplotlib.pyplot as plt
import numpy as np

name = input("Enter file name: ")
ca = plt.imread(name)
countSnow = 0
t = 0.8

for i in range(ca.shape[0]):
    for j in range(ca.shape[1]):
        if (ca[i,j,0] > t) and (ca[i,j,1] >t) and (ca[i,j,2] > t):
            countSnow = countSnow +1

print("Snow count is", countSnow)
