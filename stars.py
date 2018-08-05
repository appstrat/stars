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
y1 = 100000000
x2 = 900000000
y2 = 500000000
# Initial body velocities
v1_mag = 50
v1_dir = 3 * math.pi / 4
v2_mag = 75
v2_dir = 3 * math.pi / 4
# Body masses
m1 = 2 * 10 ** 30
m2 = 3 * 10 ** 30
# Scaling
s_scale = 1000000
t_scale = 1 * 60   # 1 second = 1 min
# Body colours
outline1  = "#0066ff"
interior1 = "#00ff99"
outline2  = "#ff0000"
interior2 = "#ff9999"
# Background colour
bg = "#000000"


# Initial setup

# Create the main objects

win = GraphWin("Star Simulation", width, height)
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

cir1 = Circle(Point(x1 / s_scale, y1 / s_scale), 10)
cir1.setOutline(outline1)
cir1.setFill(interior1)
cir1.draw(win)
cir2 = Circle(Point(x2 / s_scale, y2 / s_scale), 10)
cir2.setOutline(outline2)
cir2.setFill(interior2)
cir2.draw(win)

# Resolve vectors into x and y components
v1x = v1_mag * math.sin(v1_dir)
v1y = v1_mag * math.cos(v1_dir)
v2x = v2_mag * math.sin(v2_dir)
v2y = v2_mag * math.cos(v2_dir)

# Newton's Gravitational Constant
G = 6.7 * 10 ** -11


# Main control loop

clicked = None
start_time = time.time()
while x1 < width * s_scale and x1 >= 0 and y1 < height * s_scale and y1 >= 0 and x2 < width * s_scale and x2 >= 0 and y2 < height * s_scale and y2 >= 0:
	print(x1, y1, x2, y2)
	# Calculate interval since last iteration
	old_start_time = start_time
	start_time = time.time()
	interval = (start_time - old_start_time) * t_scale

	# Calculate distance between bodies
	r = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

	# Calculate the angle between bodies (which is the direction of the force vector)
	F_dir = math.atan((x2 - x1) / (y2 - y1))

	# Calculate the magnitude of the gravitational force between bodies
	F_mag = G * m1 * m2 / r ** 2

	# Resolve the gravitational force into x and y components
	Fx = F_mag * math.sin(F_dir)
	Fy = F_mag * math.cos(F_dir)
	
	# Calculate accelerations
	a1x = Fx / m1
	a1y = Fy / m1
	a2x = Fx / m2 * -1
	a2y = Fy / m2 * -1

	# Calculate how far to move the bodies
	# -1 in the y calculations is to account for origin starting top left, not bottom left
	x1_diff = (v1x * interval) + (1/2 * a1x * interval ** 2)
	y1_diff = (v1y * interval) + (1/2 * a1y * interval ** 2)
	x2_diff = (v2x * interval) + (1/2 * a2x * interval ** 2)
	y2_diff = (v2y * interval) + (1/2 * a2y * interval ** 2)

	# Move the bodies on screen
	cir1.move(x1_diff / s_scale, y1_diff / s_scale)
	cir2.move(x2_diff / s_scale, y2_diff / s_scale)

	# Calculate the new x and y coordinates
	x1 = x1 + x1_diff
	y1 = y1 + y1_diff
	x2 = x2 + x2_diff
	y2 = y2 + y2_diff
	print(x1, y1, x2, y2)

	# Update the velocities
	v1x = v1x + a1x * interval
	v1y = v1y + a1y * interval
	v2x = v2x + a2x * interval
	v2y = v2y + a2y * interval


# pause for click in window before exiting
win.getMouse()
win.close()
