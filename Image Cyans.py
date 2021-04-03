#Name: Ashok Surujdeo
#Date: February 17, 2021
#Email: Ashok.Surujdeo65@myhunter.cuny.edu
#This program runs: Image Cyans

import matplotlib.pyplot as plt
import numpy as np

image = input("Enter name of the input file:")
newImage = input("Enter name of the output file:")

img = plt.imread(image)
plt.imshow(img)
plt.show()

img2 = img.copy()
img2[:,:,0] = 0

plt.imshow(img2)
plt.show()

plt.imsave( newImage, img2) 
