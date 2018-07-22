#!/usr/bin/python3

import math
import random
import time

from graphics import *


# Configuration

# Window size
width = 1000
height = 800
# Initial position of centre of body
x1 = 0
y1 = 500
x2 = 200
y2 = 700
# Initial body velocities
v1_mag = 50
v1_dir = math.pi / 4
v2_mag = 75
v2_dir = math.pi / 4
# Body masses
m1 = 2 * 10 ** 30
m2 = 3 * 10 ** 30
# Body colours
outline1  = "#0066ff"
interior1 = "#00ff99"
outline2  = "#ff0000"
interior2 = "#ff9999"
# Background colour
bg = "#000000"


# Initial setup

# Create the main objects

win = GraphWin("Katie's Stuff", width, height)
win.setBackground(bg)
# Create background stars
for i in range(0, 100):	
	rand_no = random.randint(0, 3)
	if rand_no == 0:
		colour = "#ffffff"
	elif rand_no == 1:
		colour = "#ff7777"
	else:
		colour = "#7777ff"
	win.plot(random.randint(0, width), random.randint(0, height), colour)

cir1 = Circle(Point(x1, y1), 10)
cir1.setOutline(outline1)
cir1.setFill(interior1)
cir1.draw(win)
cir2 = Circle(Point(x2, y2), 10)
cir2.setOutline(outline2)
cir2.setFill(interior2)
cir2.draw(win)

# Initial body accelerations
a1_mag = 0
a1_dir = 0
a2_mag = 0
a2_dir = 0

# Resolve vectors into x and y
v1x = v1_mag * math.sin(v1_dir)
v1y = v1_mag * math.cos(v1_dir)
v2x = v2_mag * math.sin(v2_dir)
v2y = v2_mag * math.cos(v2_dir)

a1x = a1_mag * math.sin(a1_dir)
a1y = a1_mag * math.cos(a1_dir)
a2x = a2_mag * math.sin(a2_dir)
a2y = a2_mag * math.cos(a2_dir)

# Newton's Gravitational Constant
G = 6.7 * 10 ** -11


# Main control loop

clicked = None
start_time = time.time()
while x1 < width and x1 >= 0 and y1 < height and y1 >= 0 and x2 < width and x2 >= 0 and y2 < height and y2 >= 0:
	# Calculate interval since last iteration
	old_start_time = start_time
	start_time = time.time()
	interval = start_time - old_start_time

	# Calculate distance between bodies
	r = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

	# Calculate how far to move the bodies
	# -1 in the y calculations is to account for origin starting top left, not bottom left
	x1_diff = (v1x * interval) + (1/2 * a1x * interval ** 2)
	y1_diff = ((v1y * interval) + (1/2 * a1y * interval ** 2)) * -1
	x2_diff = (v2x * interval) + (1/2 * a2x * interval ** 2)
	y2_diff = ((v2y * interval) + (1/2 * a2y * interval ** 2)) * -1

	# Move the bodies
	cir1.move(x1_diff, y1_diff)
	cir2.move(x2_diff, y2_diff)

	# Get the new x and y coordinates
	centre = cir1.getCenter()
	x1 = centre.getX()
	y1 = centre.getY()
	centre = cir2.getCenter()
	x2 = centre.getX()
	y2 = centre.getY()

	# Update the velocities
	v1x = v1x + a1x * interval
	v1y = v1y + a1y * interval
	v2x = v2x + a2x * interval
	v2y = v2y + a2y * interval


# pause for click in window before exiting
win.getMouse()
win.close()

