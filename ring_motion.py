# Author: Willie Lawrence
# E-mail: cptx032 arroba gmail dot com
import math
from Tkinter import *
color = "#555"

def get_c_point(x, y, radius, angle):
	return [(math.cos(angle)*radius)+x, (math.sin(angle)*radius)+y]

class Circle:
	def __init__(self, x, y, radius, fill):
		self.x, self.y, self.radius, self.fill = x, y, radius, fill
		self.index=ca.create_oval(self.x-self.radius, self.y-self.radius,
		self.x+self.radius, self.y+self.radius, outline=color, fill=color if self.fill else None)
		self.draw()
	def draw(self):
		ca.coords(self.index, self.x-self.radius, self.y-self.radius,
		self.x+self.radius, self.y+self.radius)

top = Tk()
ca = Canvas(top, bd=0, highlightthickness=0, bg="#ddd", width=640/2,height=480/2)
ca.grid()
top.bind('<Escape>', lambda e : top.quit(), '+')
t = Circle(50, 50, 1, True)
t2 = Circle(90,50,40,False)
ang = 0.0
inc = 0.01
def up():
	global ang, inc
	ang += inc
	t.radius += 0.01
	if ang >= 360:
		ang = 0
	x, y = get_c_point(t.x, t.y, 40-t.radius, ang)
	t2.x, t2.y = x, y
	t2.draw()
	t.draw()
	top.after(1, up)
up()
top.mainloop()
