#!/usr/bin/env python3

# ------------------------ LIBRARIES -----------------
import random
from itertools import count
import pandas as pd
import matplotlib.pyplot as plt
import bubble_sort
import numpy as np

# Necessary for animation purposes
import matplotlib.animation as animation
from matplotlib.animation import FuncAnimation


# ------------------------ PALETTES ------------------

plt.style.use('dark_background') # General palette
palette={"highlighted":"#fcfa83", "others":"#83d6fc"} # Used or vertical bars



# =====================================================
# ======================= CODE ========================
# =====================================================


# ~~~~~~~~~~~~~ Setting up the variables ~~~~~~~~~~~~~~
x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15] # bars coordinates on xaxis
y = [12, 4, 3, 15, 2, 1, 11, 5, 14, 9, 6, 13, 8, 7, 10] # bars coordinates on yaxis

recipe = bubble_sort.bubble_sort_registerV2(y) # Returns a recipe of the bubble sorting algorithm

colors=[palette["highlighted"], palette["others"], palette["others"],
        palette["others"], palette["others"], palette["others"],
        palette["others"], palette["others"], palette["others"],
        palette["others"], palette["others"], palette["others"],
        palette["others"], palette["others"], palette["others"]] # One color per bar, ordered

counter = 0 # See bubble_sort.py, bubble_sort function... There are two for loops one imbricated
            # into the other. Counter reproduces the imbricated one (for j in range(...)).
counter2 = 0 # Counter2 reproduces the containing one (for i in range(...))

ax = plt.gca() # Initializing Axes object (cf. difference btw axes and axis...)


# ~~~~~~~~~~~~~ Setting up the axis style ~~~~~~~~~~~~~

# Removing the spines as they aren't useful:
ax.spines['left'].set_color('none')
ax.spines['right'].set_color('none')
ax.spines['bottom'].set_color('none')
ax.spines['top'].set_color('none')

# Removing the y ticks as they aren't useful either here:
plt.tick_params(
axis='y',          # changes apply to the y-axis
which='both',      # both major and minor ticks are affected
left=False,        # ticks along the left edge are off
labelleft=False)   # labels along the left edge are off


# ~~~~~~~~~ Defining the looped over function ~~~~~~~~~
# i is incremented after each FuncAnimation calls below

def animate(i):

    plt.cla() # Clearing the Axes object

    # One tick is associated to one bar, so that the bar with height 15
    # has tick 15 on the x axis. Thus if the bar 15 moves, tick 15 must
    # follow. This section of the code does just that...
    x_ticks_labels = []
    for l in recipe[i]:
        x_ticks_labels.append(str(l))
    plt.xticks(np.arange(1, len(y) + 1, 1), x_ticks_labels) # xticks(x_ticks_pos, x_labels)

    # Setting xticks colors and plotting (erased by cla() so current counter works):
    global counter
    global counter2

    ax.get_xticklabels()[counter].set_color(palette["highlighted"])
    ax.get_xticklabels()[counter].set_fontsize(16)

    plt.bar(x, recipe[i], color=colors)

    # Preparing next bar colors (global variable, first call of animate => preset):
    colors[counter] = palette["others"]
    colors[counter+1] = palette["highlighted"]
    counter += 1

    if counter >= (len(y) - 1 - counter2):
        colors[counter] = palette["others"]
        colors[0] = palette["highlighted"]
        counter = 0
        counter2 += 1

    if(counter2 > 14):
        counter2 = 0


# ~~~~~~ Calling the animation making function ~~~~~~~
# Loops over animate and rewinds according to frames kwarg below
# Interval kwarg defines looping through the frames speed

ani = FuncAnimation(plt.gcf(), animate, frames=len(recipe), interval=500)
# fargs=(9, ) => if animate() has several arguments as animate(i, arr_len), arr_len = 9
# ani = FuncAnimation(plt.gcf(), animate, frames=len(res), fargs=(9,), interval=500)


# ~~~~~~~~~~~~~~ Saving the animation ~~~~~~~~~~~~~~~~
# Comment if designing animation as it takes a while to make video
# Shortcut on emacs: Ctrl-x Ctr-;

# Set up formatting for the movie files
# fps = speed of the animation in the video!!
Writer = animation.writers['ffmpeg']
writer = Writer(fps=3, metadata=dict(artist='Me'), bitrate=1800)

# Does the saving...
ani.save("bubble_sort_animation.mp4", writer=writer)


# ~~~~~~~~~~~ Displaying animation result ~~~~~~~~~~~~
# Comment if recording video as it can be rather annoying to have
# a window popping up while we want to see only the video output

# plt.show()
