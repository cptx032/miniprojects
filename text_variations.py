# Author: Willie Lawrence
import sys
from Tkinter import *
top = Tk()
width, height = 480, 480
ca = Canvas(top, bd=0, highlightthickness=0, bg='black',
	width=width, height=height)
ca.grid()
top.bind('<Escape>', lambda e : top.quit(), '+')
C_POS = [width /2, height / 2]
LAST_C = None

c = sys.argv[1]

scale = 2
sentido = 1
state = 'h' # horizontal|vertical

for i in c:
	number = ord(i)
	if LAST_C == None:
		LAST_C = ord(i)
	else:
		diff = number - LAST_C
		diff *= scale
		diff *= sentido
		sentido *= -1
		# print diff
		# draw line from c-POs to
		x, y = C_POS
		if state == 'h':
			ca.create_line(x, y, x + diff, y, fill='white')
			C_POS = [x+diff, y]
			state = 'v'
		elif state == 'v':
			ca.create_line(x, y, x, y + diff, fill='white')
			C_POS = [x, y+diff]
			state = 'h'
top.mainloop()