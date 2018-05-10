#!/usr/bin/env python

# --------------------------------------------------------
# Word Cloud Examples
# Licensed under The MIT License [see LICENSE for details]
# Written by Genquan (Stone) Duan
# --------------------------------------------------------

"""
This example includes:
    1. Initialize data with "a new hope.txt" and mask images
    2. Process text data using word cloud
    3. Visualize word cloud results with different settings
"""

import numpy as np
from PIL import Image
from os import path
import matplotlib.pyplot as plt
import random, copy
from utils import *

from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator

# 1. Initialize Data
# Load data, the movie script of "a new hope",
# downloaded from http://www.imsdb.com/scripts/Star-Wars-A-New-Hope.html
text = open('a_new_hope.txt').read()
# Reprocess similar words in text
dicts = {
    "HAN":"Han",
    "LUKE'S":"Luke"
}
text = reduce(lambda a, kv: a.replace(*kv), dicts.iteritems(), text)

# A mask image to place words
# All masks are in the same size for easy demoing
mask = np.array(Image.open("mask_stormtrooper_gray.png"))
maskColor = np.array(Image.open("mask_alice_color.png"))

# adding movie script specific stopwords
stopwords = set(STOPWORDS)
stopwords.update(["int", "ext"])

# 2. Process text using word cloud
# More descriptions for parameters could be found in 
# https://github.com/amueller/word_cloud/blob/master/wordcloud/wordcloud.py
wcnull = WordCloud().generate(text)
wc = WordCloud(background_color="white",
               max_words=200, 
               mask=mask, 
               stopwords=stopwords, 
               margin=10,
               random_state=1).generate(text)

# 3. Visualization word cloud results with different settings
# 3.0 A square form result
wcnull.to_file("demo_0_square.png")
plt.figure()
plt.title("Square form")
plt.imshow(wcnull, interpolation="bilinear")

# 3.1 A colorful result with gray masks and default settings
default_wc_image = copy.deepcopy(wc)
default_wc_image.to_file("demo_1_default_color.png")
plt.figure()
plt.title("Default color")
plt.imshow(default_wc_image, interpolation="bilinear")

# 3.2 A colorful result with color masks
custom_color_wc_image = copy.deepcopy(wc)
custom_color_wc_image.recolor(color_func = ImageColorGenerator(maskColor))
custom_color_wc_image.to_file("demo_2_custom_color.png")
plt.figure()
plt.title("Customr color")
plt.imshow(custom_color_wc_image, interpolation="bilinear")

# 3.3 A colorful result with coloring some special words
color_to_words = {
    # words below will be colored with a green single color function
    '#00ff00': ['Han', 'explicit', 'simple', 'sparse'],
    # will be colored with a red single color function
    'red': ['Luke', 'implicit', 'complex', 'complicated', 'nested']
}
grouped_color_func = GroupedColorFunc(color_to_words, "grey")
color_special_word_wc_image = copy.deepcopy(wc)
color_special_word_wc_image.recolor(color_func=grouped_color_func, random_state=3)
color_special_word_wc_image.to_file("demo_3_color_special_word.png")
plt.figure()
plt.title("Color special word")
plt.imshow(color_special_word_wc_image, interpolation="bilinear")

# 3.4 A gray result with gray masks 
custom_gray_wc_image = copy.deepcopy(wc)
custom_gray_wc_image.recolor(color_func=grey_color_func, random_state=3)
custom_gray_wc_image.to_file("demo_4_custom_gray.png")
plt.figure()
plt.title("Custom gray")
plt.imshow(custom_gray_wc_image, interpolation="bilinear")


#plt.show()
