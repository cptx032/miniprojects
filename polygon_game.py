# Author: Willie
# Date: 05/04/2015 - 02:41
WIDTH, HEIGHT = 320,240
from Tkinter import *
from random import randint
top = Tk()
top.configure(width=WIDTH, height=HEIGHT)
top.bind("<Escape>", lambda e:top.destroy(), "+")
ca = Canvas(top,bd=0,bg="white",highlightthickness=0,
width=WIDTH, height=HEIGHT)
ca.pack(expand=YES,fill=BOTH)

class Body:
	def __init__(self, **kws):
		self.pos = kws.get('pos', [5,5])
		self.vel = kws.get('vel', [0,0])
	def update(self):
		self.pos[0] += self.vel[0]
		self.pos[1] += self.vel[1]
		if (self.pos[0] >= WIDTH) or (self.pos[0]<=0):
			self.vel[0] *= -1
		if (self.pos[1] >= HEIGHT) or (self.pos[1]<=0):
			self.vel[1] *= -1

class Ball(Body):
	def __init__(self, **kws):
		Body.__init__(self,**kws)
		self.canvas = kws.get('canvas')
		self.index = self.canvas.create_oval(self.pos[0]-5,
		self.pos[1]-5, self.pos[0]+5, self.pos[1]+5)
	def draw(self):
		self.canvas.coords(self.index,self.pos[0],self.pos[1],
			self.pos[0]+10, self.pos[1]+10)

def rand():
	return randint(0,10) / 10.0

NUM_POINTS = 100

points = [
	Body(
		canvas=ca,
		vel=[rand(),rand()],
		pos=[rand(),rand()]
	) for i in range(0,NUM_POINTS)
]

class Polygon:
	def __init__(self, **kws):
		self.points = kws.get('points',[])
		self.canvas = kws.get('canvas')
		self.index = self.canvas.create_polygon(*self.get_coords())
	def get_coords(self):
		_r = []
		for i in self.points:
			_r.append(i.pos[0])
			_r.append(i.pos[1])
			i.update()
		return _r
	def draw(self):
		self.canvas.coords(self.index, *self.get_coords())
		self.canvas.itemconfig(self.index,fill="#%02x%02x%02x" % (rand()*255, rand()*255, rand()*255))

b = Polygon(canvas=ca,points=points)

def _main(*args):
	b.draw()
	top.after(1,_main)
_main()

top.mainloop()
