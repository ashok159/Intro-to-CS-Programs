#Name: Ashok Surujdeo
#Date: March 2, 2021
#Email: Ashok.Surujdeo65@myhunter.cuny.edu
#This program runs: Purple-Cyan Stripes

import matplotlib.pyplot as plt
import numpy as np

num = int(input("Enter the size: "))

logoImg = np.ones((num,num,3))

logoImg[::2,::,1] = 0
logoImg[1:num:2,::,0] = 0

plt.imsave(str(num) + "stripes.png" ,logoImg)
 
