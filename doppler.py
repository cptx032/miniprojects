# Author: cptx032 arroba gmail ponto com
# Date: domingo vinte e seis de abril de 2015

TICKER = 1
WAVE_VELOCITY = 10

from Tkinter import *
top = Tk()
top.title('Doppler effect')

ca = Canvas(bd=0,highlightthickness=0,bg="white")
ca.pack(expand=YES,fill=BOTH)
ca.config(width=640,height=480)

class Wave:
	def __init__(self, ca, vel, x, y):
		self.life = 0
		self.canvas = ca
		self.vel = vel
		self.pos = [x,y]
		self.__radius = 0
		self.__index = self.__get_index()
		self.update()
	def __get_index(self):
		return self.canvas.create_oval(*self.get_coords(),outline="#00aacc")
	def get_coords(self):
		return [
			self.pos[0]-self.__radius, # x1
			self.pos[1]-self.__radius, # y1
			self.pos[0]+self.__radius, # x2
			self.pos[1]+self.__radius
		]
	def update(self):
		self.canvas.coords(self.__index, *self.get_coords())
		self.__radius += self.vel
		self.life += 1
		if self.life <= 100:
			self.canvas.after(TICKER,self.update)
		else:
			self.canvas.delete(self.__index)

class Particle:
	def __init__(self, **kws):
		self.canvas = kws.get('canvas')
		self.kick = True
		self.pos = kws.get('pos',[])
		self.freq = kws.get('freq', 0)
		self.vel = kws.get('vel',[0,0])
		self.__radius = 5
		self.__index = self.__get_index()
		self.update()
	def get_coords(self):
		return [
			self.pos[0]-self.__radius,
			self.pos[1]-self.__radius,
			self.pos[0]+self.__radius,
			self.pos[1]+self.__radius
		]
	def __get_index(self):
		return self.canvas.create_oval(*self.get_coords(),fill='red')
	def update(self):
		self.canvas.update_idletasks()
		self.pos[0] += self.vel[0]
		self.pos[1] += self.vel[1]
		self.canvas.coords(self.__index, *self.get_coords())
		self.canvas.after(TICKER, self.update)
		Wave(self.canvas, WAVE_VELOCITY, self.pos[0], self.pos[1])
		if not self.kick:
			if self.pos[0] >= self.canvas.winfo_width():
				self.pos[0] = 0
			if self.pos[0] < 0:
				self.pos[0] = self.canvas.winfo_width()
			if self.pos[1] >= self.canvas.winfo_height():
				self.pos[1] = 0
			if self.pos[1] < 0:
				self.pos[1] = self.canvas.winfo_height()
		else:
			if self.pos[0] >= self.canvas.winfo_width():
				self.vel[0] *= -1
			if self.pos[0] < 0:
				self.vel[0] *= -1
			if self.pos[1] >= self.canvas.winfo_height():
				self.vel[1] *= -1
			if self.pos[1] < 0:
				self.vel[1] *= -1

Particle(pos=[100,240],canvas=ca,vel=[5,5])

top.bind('<Escape>', lambda e : top.destroy(), '+')
top.mainloop()