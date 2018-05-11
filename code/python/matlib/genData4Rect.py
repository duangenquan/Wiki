#!/usr/bin/env python

# --------------------------------------------------------
# Matplot Rectangle Examples
# Licensed under The MIT License [see LICENSE for details]
# Written by Genquan (Stone) Duan
# --------------------------------------------------------

"""
This example shows how to use matplot draw rectangles with

"""
import matplotlib.patches as patches

def generateData():

    patterns = ['-', '+', 'x', 'o', 'O', '.', '*']

    rects = []

    # Add a non filling rectangle
    rects.append(
        patches.Rectangle(
            (0.1, 0.8),   # (x,y)
            0.2,          # width
            0.15,         # height
            fill = True   # by default is None
        )
    )

    # Add a filling rectangle
    rects.append(
        patches.Rectangle(
            (0.5, 0.8),
            0.2,
            0.1,
            fill=False      # remove background
        )
    )

    # Add more examples
    rects.append(
        patches.Rectangle(
            (0.03, 0.1), 0.2, 0.6,
            alpha=None,
            facecolor=None,
            edgecolor=None,
            linewidth=None,
            linestyle='solid',
            hatch=patterns[0],
            fill=False
        )
    )

    rects.append(
        patches.Rectangle(
            (0.26, 0.1), 0.2, 0.6,
            alpha=1.0,
            facecolor="none",
            linewidth=2,
            linestyle='dashed',
            hatch=patterns[1],
            fill=False
        )
    )

    rects.append(
        patches.Rectangle(
            (0.49, 0.1), 0.2, 0.6,
            alpha=0.6,
            facecolor="red",
            edgecolor="black",
            linestyle='dashdot',
            hatch=patterns[2],
            fill=False
        ),
    )
    rects.append(
        patches.Rectangle(
            (0.72, 0.1), 0.2, 0.6,
            alpha=0.1,
            facecolor="#00ffff",
            linewidth=4,
            linestyle='dotted',
            hatch=patterns[4],
            fill=False
        )
    )

    return rects
