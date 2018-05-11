#!/usr/bin/env python

# --------------------------------------------------------
# Matplot Rectangle Examples
# Licensed under The MIT License [see LICENSE for details]
# Written by Genquan (Stone) Duan
# --------------------------------------------------------

"""
This example shows how to use matplot draw rectangles with
    fill alpha/color/pattern
    border color/style/width/hatch
"""
import matplotlib.pyplot as plt
from genData4Rect import *

# fill patterns, alpha, background color, border color, border width, border style, 
fig = plt.figure()
ax = fig.add_subplot(111, aspect='equal')
rects = generateData()
for p in rects:
    ax.add_patch(p)
fig.savefig('rect.png', dpi=90, bbox_inches='tight')