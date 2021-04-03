#Name: Ashok Surujdeo
#Email: Ashok.Surujdeo65@myhunter.cuny.edu
#Date: February 23, 2021
#This program runs: T-Logo

import matplotlib.pyplot as plt
import numpy as np

logoImg = np.ones((30,30,3)) 

logoImg[:10,:,0] = 0
logoImg[:10,:,2] = 0

logoImg[10:30,10:20,0] = 0
logoImg[10:30,10:20,2] = 0

plt.imsave("logo.png", logoImg)
