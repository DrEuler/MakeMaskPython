from __future__ import print_function
import matplotlib 
matplotlib.use('Agg')
import matplotlib.pyplot as plt 
import os.path
import numpy as np      # 'as' lets us use standard abbreviations

'''Read the image data'''
# Get the directory of this python script
directory = os.path.dirname(os.path.abspath(__file__)) 
# Build an absolute filename from directory + filename
filename = os.path.join(directory, 'woman.jpg')
filename2 = os.path.join(directory, 'mask.png')

# Read the image data into an array
img = plt.imread(filename)
img2 = plt.imread(filename2)

'''Show the image data'''
# Create figure with 2 subplot
fig, ax = plt.subplots(1, 2)

# Show the image data in a subplot
ax[0].imshow(img, interpolation='none')
ax[1].imshow(img2, interpolation='none')
# Saves the figure
###
# Make a rectangle of pixels yellow
###

###
# Change a region if condition is True
###
"""
height = len(img)
width = len(img[0])
for r in range(155):
    for c in range(width):
        if sum(img[r][c])>500: # brightness R+G+B goes up to 3*255=765
            img[r][c]=[255,0,255] # R + B = magenta
"""     
#for the sky
widthx = len(img[0])
for rx in range(155):
    for cx in range(widthx):
        if sum(img[rx][cx])>500: # brightness R+G+B goes up to 3*255=765
            img[rx][cx]=[255,255,0] # R +g

height = len(img)
width = len(img[0])
for row in range(400, 487):
    for column in range(100, 170):
        img[row][column] = [255, 0, 0]#green, red


fig.savefig('women2')
print(img)
print(type(img))

print(len(img))
print(len(img[0]))


'''4.Arrays and lists are similar by both doing
the same thing, they are different by arrays 
containing a single data type, unlike lists 
which contain multiple data types.
'''
"""
5. 	the image height = the number of rows of pixels = 1000
	the image width = the number of columns = 5
	the green intensity at (5,9) = 95
    the red intensity at (4,10) = 83
	the red intensity of the 25th pixel in the 50th row = 104
"""
"""
7.
    a. In lines 28-31 of this code the algorithm used is that
    the code checks to see how many rows of pixels are in range
    of 155. The code than checkks the brightness of the pixels. 
    Then if the brightness is more than 500, the color will 
    appear to be sky.
"""
'''
8.
'''

"""CONCLUSION QUESTIONS
    1. Digital Images contain data called pixels 
    2. 
    3. 

"""
