# -*- coding: utf-8 -*-
'''
JMurphy_1_4_2: Read and show an image.
'''
import matplotlib.pyplot as plt 
import os.path
import numpy as np      # “as” lets us use standard abbreviations

i = 0

'''Read the image data'''
# Get the directory of this python script
directory = os.path.dirname(os.path.abspath(__file__)) #instantiating(creating) a directory
# Build an absolute filename from directory + filename
filename = os.path.join(directory, 'woman.jpg') #building the filepath to the image
# Read the image data into an array
img = plt.imread(filename) #using plt library to take a picture file and putting it into a plot (prerendering)

'''Show the image data'''
# Create figure with 1 subplot
fig, ax = plt.subplots(1, 2) #instantiating fig and ax as subplots
# Show the image data in a subplot
ax[0].imshow(img)
ax[1].imshow(img, interpolation='none') # Override the default
ax[0].set_xlim(135, 165)
ax[0].set_ylim(470, 420)
ax[1].set_xlim(135, 165)
ax[1].set_ylim(470, 420)
# Show the figure on the screen
fig.show() #showing the picture