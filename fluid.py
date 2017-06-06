#!/usr/bin/env python
# coding: utf-8
# Author: Willie Lawrence
from Tkinter import *
top = Tk()
size = 32
WIDTH, HEIGHT = size * 5, size * 5
ca = Canvas(
	top,
	bd=0,
	highlightthickness=0,
	bg="white",
	width=WIDTH,
	height=HEIGHT
)
ca.grid()
top.bind("<Escape>", lambda e : top.quit(), "+")

rows = size
columns = size
# stores the values of "intensity"
grid = []

# stores the canvas index of rectangles
graphical_grid = []
# the size of a graphical rectangle
rec_size_width = WIDTH / columns
rec_size_height = HEIGHT / rows

def lerp(a, b, x):
	return a + ((b-a)*x)

class Rectangle:
	def __init__(self, x, y):
		x1 = rec_size_width * x
		y1 = rec_size_height * y
		self.index = ca.create_rectangle(x1, y1, x1+rec_size_width, y1+rec_size_height, fill="red", outline="black")
		self.intensity = 0.0
		ca.tag_bind(self.index, "<1>", self.on_click, "+")

	def on_click(self, event):
		self.intensity = 1.0
		self.update()

	def update(self):
		gray = lerp(0, 255, self.intensity)
		g = '#%02x0000'
		# if gray > 100:
		# 	g = '#0000%02x'
		# if gray > 200:
		# 	g = '#00%02x00'
		ca.itemconfig(
			self.index,
			fill=g % (gray),
			outline=""
		)

for line in range(rows):
	l = []
	for col in range(columns):
		l.append( Rectangle( col, line ) )
	grid.append( l )

TICKER = 1

diffuse_factor = 0.518

def get(x, y):
	if (x < 0) or (x >= columns) or (y < 0) or (y >= rows):
		return 0.3
	return float(grid[y][x].intensity)


def update(*args):
	# making diffusion
	for row_i in range(rows):
		for col_i in range(columns):
			rect = grid[row_i][col_i]
			up = get(col_i, row_i-1)
			bottom = get(col_i, row_i+1)
			left = get(col_i-1, row_i)
			right = get(col_i+1, row_i)
			# nw = get(col_i-1, row_i-1)
			# ne = get(col_i+1, row_i-1)
			# sw = get(col_i-1, row_i+1)
			# se = get(col_i+1, row_i+1)

			tobesum = (up*diffuse_factor) + (bottom*diffuse_factor) + (left*diffuse_factor) + (right*diffuse_factor)
			# tobesum += (nw * diffuse_factor) + (ne+diffuse_factor) + (sw*diffuse_factor) + (se*diffuse_factor)
			# tobesum *= 1.0
			# vc "doa" sua intensidade 4 vezes porque as quatro celulas do lado vao absorver
			# a sua intensidade. e ao mesmo tempo vc recebe a doação das quatro celulas vizinhas
			rect.intensity -= rect.intensity * diffuse_factor * 4
			rect.intensity += tobesum

			if (rect.intensity > 0.4):
				rect.intensity = 0.4
			if (rect.intensity < 0):
				rect.intensity = 0
			
			rect.update()
	top.after(TICKER, update)
update()

top.mainloop()
