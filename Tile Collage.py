#Name: Ashok Surujdeo
#Email: Ashok.Surujdeo65@myhunter.cuny.edu
#Date: March 23, 2021
#This program runs: Tile Collage

import numpy as np
import matplotlib.pyplot as plt

def mirror(img, axis):
    '''
    Creates and returns a mirrored copy of img along axis
    Expected values for axis are 'x', 'y', 'xy' (mirrored along both x and y axes)
    If the value of axis is not one of the expected, it prints: Invalid axis
    '''
    
    if axis == 'x':
        flipped = np.flipud(img)
        plt.imshow(flipped)
    elif axis == 'y':
        flipped = np.fliplr(img)
        plt.imshow(flipped)
    elif axis == 'xy':
        flip1 = np.fliplr(img)
        plt.imshow(flip1)
        flipped = np.flipud(flip1)
        plt.imshow(flipped)
    else:
        print("Invalid axis")
    return(flipped)
    

def remove_hue(img, hue):
    if hue == 'red':
        img[:,:,0] = 0
    elif hue == 'green':
        img[:,:,1] = 0
    elif hue == 'blue':
        img[:,:,2] = 0
    else:
        print("No such hue")

def fourfold_tile(img):
    col1 = np.vstack([img, img])
    col2 = np.vstack([img, img])
    fourfold = np.hstack([col1, col2])
    return(fourfold)

######################################################################
### DO NOT CHANGE ANYTHING BELOW  AND INCLUDING THIS LINE          ###
######################################################################


def main():
    '''
    Creates a tile collage from input image
    '''

    infile = input('Enter input file name: ')
    outFile = input('Enter output file name: ')
    img = plt.imread(infile)

    #new_img consits of four copies of img, two on top and two ont the bottom
    new_img = fourfold_tile(img)

    #Remove blue from top-right quarter
    remove_hue(new_img[:img.shape[0],img.shape[1]:],'blue')
    #Remove green from bottom-left quarter
    remove_hue(new_img[img.shape[0]:,:img.shape[1]],'green')
    #Remove blue from bottom-right quarter
    remove_hue(new_img[img.shape[0]:,img.shape[1]:],'red')


    #Mirror top-right quarter along the y-axis
    new_img[:img.shape[0],img.shape[1]:] = mirror(new_img[:img.shape[0],img.shape[1]:],"y")
    #Mirror bottom-left quarter along the x-axis
    new_img[img.shape[0]:,:img.shape[1]] = mirror(new_img[img.shape[0]:,:img.shape[1]],"x")
    #Mirror bottom-right quarter along both x and y axis
    new_img[img.shape[0]:,img.shape[1]:] = mirror(new_img[img.shape[0]:,img.shape[1]:],"xy")


    #Save the tile collage to a file
    plt.imsave(outFile, new_img)


#Allow script to be run directly:
if __name__ == '__main__':
    main()


    
