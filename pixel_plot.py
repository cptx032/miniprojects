from Tkinter import *
import random
top = Tk()
WIDTH, HEIGHT = 40, 30
ZOOM = 16

screen = []
for i in range(HEIGHT):
	line = []
	for i in range(WIDTH):
		line.append(0)
	screen.append(line)

ph = PhotoImage(width=WIDTH, height=HEIGHT)

def _plot_screen(event=None):
	global ph
	final_string = ''
	for line in screen:
		line = '{' + ' '.join(['#' + hex(pixel).replace('0x', '').zfill(6) for pixel in line]) + '} '
		final_string += line
	ph.put(final_string[:-1])

ca = Canvas(top, width=WIDTH*ZOOM, height=HEIGHT*ZOOM, bd=0, highlightthickness=0)
ca.grid()

def _process():
	global screen
	for i in range(50):
		screen[random.randint(0, HEIGHT-1)][random.randint(0, WIDTH-1)] = random.randint(0, 0xffffff)

TICKER = 10
def _loop(event=None):
	_plot_screen()
	_process()
	raster = ph.zoom(ZOOM)
	ca.img = raster
	ca.create_image(0, 0, image=raster, anchor='nw')
	top.after(TICKER, _loop)
_loop()
top.mainloop()
