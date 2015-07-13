# Author: Willie Lawrence
from Tkinter import *
import math
import random
'''
F = ma
'''
SCREEN_SIZE = [1360,768]
WINDOW_SIZE = [500,500]
TICKER = 30
CIRCLE = 'circle'
RECTANGLE = 'rectangle'
MODE = RECTANGLE # circle | rectangle

def centralize():
	return '%dx%d+%d+%d' % (WINDOW_SIZE[0], WINDOW_SIZE[1],
				(SCREEN_SIZE[0]/2)-(WINDOW_SIZE[0]/2),
				(SCREEN_SIZE[1]/2)-(WINDOW_SIZE[1]/2))

def drawtext(canvas, text):
	canvas.create_text(5,5,anchor=NW,text=text,fill='dimgrey')

def clear(canvas):
	canvas.delete('all')

class VariableForce:
	def __init__(self, *args, **kws):
		self.value = kws.get('force', [0.0])

class Particle:
	def __init__(self, *args, **kws):
		self.mass = kws.get('mass', 1.0)
		self.pos = kws.get('pos', [0.0,0.0])
		self.vel = kws.get('vel', [0.0,0.0])
		self.restitution_coeficient = 0.7 # 1.0 = lossless

	def next(self):
		self.pos[0] = self.pos[0] + self.vel[0]
		self.pos[1] = self.pos[1] + self.vel[1]
	
	def applyforce(self, force):
		accel = [force[0]/self.mass, force[1]/self.mass]
		self.vel[0] += accel[0]
		self.vel[1] += accel[1]
	
	def applyimpulse(self, intensity, time=0.1):
		# i = ft
		forcex = intensity[0] / float(time)
		forcey = intensity[1] / float(time)
		self.applyforce([forcex, forcey])
	
	def getmomentum(self):
		return [self.vel[0]*self.mass, self.vel[1]*self.mass]
	
	x = property(lambda self : self.pos[0], None, None, 'x')
	y = property(lambda self : self.pos[1], None, None, 'y')

class Body(Particle):
	def __init__(self, *args, **kws):
		self.radius = kws.get('radius', 15.0)
		self.color = kws.get('color', '#00aacc')
		Particle.__init__(self, *args, **kws)
	
	def draw(self, canvas):
		if MODE == CIRCLE:
			self.__draw_circle(canvas)
		elif MODE == RECTANGLE:
			self.__draw_rectangle(canvas)
			
	def __draw_circle(self, canvas):
		canvas.create_oval(
			self.x-self.radius,	self.y-self.radius,
			self.x+self.radius, self.y+self.radius,
			fill=self.color,outline=self.color
		)
	
	def __draw_rectangle(self, canvas):
		canvas.create_rectangle(
			self.x-self.radius,	self.y-self.radius,
			self.x+self.radius, self.y+self.radius,
			fill=self.color,outline=self.color
		)
	
	def colliding(self, particle):
		return self.distance(particle) <= (self.radius + particle.radius)
	
	def distance(self, particle):
		'''
		Return the distance between this and another particle
		'''
		x = abs(self.x-particle.x)
		y = abs(self.y-particle.y)
		return math.sqrt(x**2 + y**2)
	
	def inverse(self):
		self.vel[0] *= -1
		self.vel[1] *= -1
	
	def next(self):
		Particle.next(self)
		n = False
		if (self.pos[0]-self.radius) < 0.0:
			self.vel[0] = self.vel[0] * -1 * self.restitution_coeficient
			n = True
		elif (self.pos[0]+self.radius) > WINDOW_SIZE[0]:
			self.vel[0] = self.vel[0] * -1 * self.restitution_coeficient
			n = True

		if (self.pos[1]-self.radius) < 0.0:
			self.vel[1] = self.vel[1] * -1 * self.restitution_coeficient
			n = True
		elif (self.pos[1]+self.radius) > WINDOW_SIZE[1]:
			self.vel[1] = self.vel[1] * -1 * self.restitution_coeficient
			n = True
		if n:
			Particle.next(self)
		# threshould
		if (self.pos[0]-self.radius) < 0.0:
			self.pos[0] = self.radius
		elif (self.pos[0]+self.radius) > WINDOW_SIZE[0]:
			self.pos[0] = WINDOW_SIZE[0] - self.radius
			
		if (self.pos[1]-self.radius) < 0.0:
			self.pos[1] = self.radius
		elif (self.pos[1]+self.radius) > WINDOW_SIZE[1]:
			self.pos[1] = WINDOW_SIZE[1] - self.radius

class Environment:
	def __init__(self, *args, **kws):
		self.particles = []
		self.forces = []
	
	def next(self):
		for particle in self.particles:
			for force in self.forces:
				if type(force) == VariableForce:
					particle.applyforce(force.value)
				else:
					particle.applyforce(force)
			particle.next()
	
	def add(self, particle):
		self.particles.append(particle)

env = Environment()

def colliding_with(particle):
	'''Returns the objects that are colliding with it'''
	for _p in env.particles:
		if particle != _p:
			if particle.colliding(_p):
				# esse inversao nao pode ser feita no dois eixos
				particle.inverse() # [fixme]
				_p.inverse()
				particle.next()
				_p.next()

window = Tk()
window.resizable(0,0)
window.bind('<Escape>', lambda e : window.destroy(), '+')
canvas = Canvas(window, bd=0,bg='white',highlightthickness=0,width=WINDOW_SIZE[0],height=WINDOW_SIZE[1])
canvas.grid()
window.geometry(centralize())

env.forces.append([0.0,10.0]) # gravity
env.forces.append([0.0,0.0]) # wind

NUM_PARTICLES = 6
for i in range(NUM_PARTICLES):
	kws = {
		'pos' : [random.randint(0,WINDOW_SIZE[0]), random.randint(0,WINDOW_SIZE[1])],
		'mass' : random.randint(1.0,10.0),
		'vel' : [random.randint(-5,5),0],
		# 'color' : '#%02x%02x%02x' % (random.randint(0,255),random.randint(0,255),random.randint(0,255))
	}
	env.add( Body(**kws) )

def _main(*args):
	clear(canvas)
	for p in env.particles:
		colliding_with(p)
		p.draw(canvas)
	env.next()
	
	txt = 'FORCES:\n'
	for force in env.forces:
		txt += '   ' + str(force) + '\n'
	drawtext(canvas, txt)
	'''
	if env.particles[0].colliding(env.particles[1]):
		print "ok"
		env.particles[1].inverse()
		env.particles[0].inverse()
		env.particles[1].next()
		env.particles[0].next()
	'''
	window.after(TICKER, _main)

_main()
window.mainloop()
