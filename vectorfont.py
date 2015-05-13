# Adapted by Willie Lawrence from http://wiki.tcl.tk/27638
_DEFAULT_FONT = {
	"a": [[4, 0, 1, 0, 0, 1, 0, 3, 1, 4, 4, 4, 4, 0]],
	"b" : [[0, 6, 0, 0, 3, 0, 4, 1, 4, 3, 3, 4, 0, 4]],
	"c" : [[4, 0, 1, 0, 0, 1, 0, 3, 1, 4, 4, 4]],
	"d" : [[4, 6, 4, 0, 1, 0, 0, 1, 0, 3, 1, 4, 4, 4]],
	"e" : [[4, 0, 1, 0, 0, 1, 0, 3, 1, 4, 3, 4, 4, 3, 4, 2, 0, 2]],
	"f" : [[2, 0, 2, 5, 3, 6, 4, 6], [0, 3, 4, 3]],
	"g" : [[0, 0, 3, 0, 4, 1, 4, 4, 3, 5, 1, 5, 0, 4, 0, 3, 1, 2, 4, 2]],
	"h" : [[0, 6, 0, 0], [0, 4, 3, 4, 4, 3, 4, 0]],
	"i" :  [[2, 0, 2, 4], [2, 5, 2, 6]],
	"j" : [[0, 0, 1, 0, 2, 1, 2, 4], [2, 5, 2, 6]],
	"k" : [[0, 0, 0, 6], [4, 0, 0, 2, 3, 5]],
	"l" : [[1, 6, 2, 6, 2, 0], [1, 0, 3, 0]],
	"m" : [[0, 0, 0, 4, 1, 4, 2, 3, 3, 4, 4, 4, 4, 0], [2, 0, 2, 3]],
	"n" : [[0, 4, 0, 0], [0, 3, 1, 4, 3, 4, 4, 3, 4, 0]],
	"o" : [[0, 1, 0, 3, 1, 4, 3, 4, 4, 3, 4, 1, 3, 0, 1, 0, 0, 1]],
	"p" : [[0, 0, 0, 5, 3, 5, 4, 4, 4, 3, 3, 2, 0, 2]],
	"q" : [[4, 0, 4, 5, 1, 5, 0, 4, 0, 3, 1, 2, 4, 2]],
	"r" : [[0, 0, 0, 4, 3, 4, 4, 3]],
	"s" : [[0, 0, 4, 0, 4, 2, 0, 2, 0, 4, 4, 4]],
	"t" : [[1, 6, 1, 1, 2, 0, 3, 0, 4, 1], [0, 5, 3, 5]],
	"u" : [[4, 4, 4, 0], [4, 1, 3, 0, 1, 0, 0, 1, 0, 4]],
	"v" : [[0, 4, 2, 0, 4, 4]],
	"w" : [[0, 4, 0, 0, 2, 2, 4, 0, 4, 4]],
	"x" : [[0, 0, 4, 4], [0, 4, 4, 0]],
	"y" : [[0, 5, 0, 3, 1, 2, 3, 2, 4, 3], [4, 5, 4, 1, 3, 0, 0, 0]],
	"z" : [[0, 4, 4, 4, 0, 0, 4, 0]],
	"A" : [[0, 0, 0, 4, 2, 6, 4, 4, 4, 0], [0, 2, 4, 2]],
	"B" : [[0, 0, 0, 6, 3, 6, 4, 5, 4, 4, 3, 3, 4, 2, 4, 1, 3, 0, 0, 0], [0, 3, 3, 3]],
	"C" : [[4, 0, 0, 0, 0, 6, 4, 6]],
	"D" : [[0, 0, 0, 6, 2, 6, 4, 4, 4, 2, 2, 0, 0, 0]],
	"E" : [[4, 0, 0, 0, 0, 6, 4, 6], [0, 3, 4, 3]],
	"F" : [[0, 0, 0, 6, 4, 6], [0, 3, 3, 3]],
	"G" : [[2, 2, 4, 2, 4, 0, 0, 0, 0, 6, 4, 6, 4, 4]],
	"H" : [[0, 0, 0, 6], [4, 0, 4, 6], [0, 3, 4, 3]],
	"I" : [[0, 0, 4, 0], [2, 0, 2, 6], [0, 6, 4, 6]],
	"J" : [[0, 2, 2, 0, 4, 0, 4, 6]],
	"K" : [[0, 0, 0, 6], [4, 6, 0, 3, 4, 0]],
	"L" : [[4, 0, 0, 0, 0, 6]],
	"M" : [[0, 0, 0, 6, 2, 4, 4, 6, 4, 0]],
	"N" : [[0, 0, 0, 6, 4, 0, 4, 6]],
	"O" : [[0, 0, 0, 6, 4, 6, 4, 0, 0, 0]],
	"P" : [[0, 0, 0, 6, 4, 6, 4, 3, 0, 3]],
	"Q" : [[0, 0, 0, 6, 4, 6, 4, 2, 2, 0, 0, 0], [2, 2, 4, 0]],
	"R" : [[0, 0, 0, 6, 4, 6, 4, 3, 0, 3], [1, 3, 4, 0]],
	"S" : [[0, 0, 3, 0, 4, 1, 4, 2, 3, 3, 1, 3, 0, 4, 0, 5, 1, 6, 4, 6]],
	"T" : [[2, 0, 2, 6], [0, 6, 4, 6]],
	"U" : [[0, 6, 0, 0, 4, 0, 4, 6]],
	"V" : [[0, 6, 2, 0, 4, 6]],
	"W" : [[0, 6, 0, 0, 2, 2, 4, 0, 4, 6]],
	"X" : [[0, 0, 4, 6], [0, 6, 4, 0]],
	"Y" : [[0, 6, 2, 4, 4, 6], [2, 0, 2, 4]],
	"Z" : [[0, 6, 4, 6, 0, 0, 4, 0], [1, 3, 3, 3]],
	"0" : [[0, 0, 0, 6, 4, 6, 4, 0, 0, 0], [0, 0, 4, 6]],
	"1" : [[2, 0, 2, 6, 0, 4], [0, 0, 4, 0]],
	"2" : [[0, 6, 4, 6, 4, 3, 0, 3, 0, 0, 4, 0]],
	"3" : [[0, 6, 4, 6, 4, 0, 0, 0], [0, 3, 4, 3]],	
	"4" : [[0, 6, 0, 3, 4, 3], [4, 6, 4, 0]],
	"5" : [[0, 0, 4, 0, 4, 3, 0, 3, 0, 6, 4, 6]],
	"6" : [[4, 6, 0, 6, 0, 0, 4, 0, 4, 3, 0, 3]],
	"7" : [[0, 6, 4, 6, 4, 0]],
	"8" : [[0, 0, 0, 6, 4, 6, 4, 0, 0, 0], [0, 3, 4, 3]],
	"9" : [[4, 0, 4, 6, 0, 6, 0, 3, 4, 3]],
	"~" : [[0, 4, 0, 5, 2, 5, 2, 4, 4, 4, 4, 5]],
	"`" : [[1, 6, 3, 4]],
	"!" : [[2, 0, 2, 1], [2, 2, 2, 6]],
	"@" : [[3, 2, 3, 4, 1, 4, 1, 2, 3, 2, 4, 1, 4, 6, 0, 6, 0, 0, 3, 0]],
	"#" : [[1, 0, 1, 6], [3, 0, 3, 6], [0, 2, 4, 2], [0, 4, 4, 4]],
	"$" : [[0, 2, 0, 1, 4, 1, 4, 3, 0, 3, 0, 5, 4, 5, 4, 4], [2, 0, 2, 6]],
	"%" : [[0, 6, 0, 4, 2, 4, 2, 6, 0, 6], [2, 0, 4, 0, 4, 2, 2, 2, 2, 0], [0, 0, 4, 6]],
	"^" : [[0, 4, 2, 6, 4, 4]],
	"&" : [[4, 0, 1, 0, 0, 1, 0, 2, 3, 5, 2, 6, 1, 6, 0, 5, 4, 0]],
	"*" : [[2, 0, 2, 6], [0, 3, 4, 3], [0, 1, 4, 5], [0, 5, 4, 1]],
	"(" : [[4, 0, 3, 0, 1, 2, 1, 4, 3, 6, 4, 6]],
	")" : [[0, 0, 1, 0, 3, 2, 3, 4, 1, 6, 0, 6]],
	"_" : [[0, 0, 4, 0]],
	"-" : [[0, 3, 4, 3]],
	"+" : [[0, 3, 4, 3], [2, 1, 2, 5]],
	"=" : [[0, 2, 4, 2], [0, 4, 4, 4]],
	"[" : [[4, 0, 2, 0, 2, 6, 4, 6]],
	"]" : [[0, 0, 2, 0, 2, 6, 0, 6]],
	"{" : [[4, 0, 2, 0, 2, 2, 1, 3, 2, 4, 2, 6, 4, 6]],
	"}" : [[0, 0, 2, 0, 2, 2, 3, 3, 2, 4, 2, 6, 0, 6]],
	"|" : [[2, 0, 2, 2], [2, 4, 2, 6]],
	"\\" : [[0, 6, 4, 0]],
	":" : [[2, 1, 2, 2], [2, 4, 2, 5]],
	";" : [[1, 0, 2, 1, 2, 2], [2, 4, 2, 5]],
	'"' : [[1, 6, 1, 4], [3, 6, 3, 4]],
	"'" : [[2, 6, 2, 4]],
	"," : [[1, 0, 2, 1, 2, 2]],
	"." : [[2, 0, 2, 1]],
	"/" : [[0, 0, 4, 6]],
	"?" : [[2, 0, 2, 1], [2, 2, 4, 4, 4, 6, 0, 6, 0, 4]],
	"<" : [[4, 6, 0, 3, 4, 0]],
	">" : [[0, 0, 4, 3, 0, 6]],
}
def draw_letter(c, basecoords, letter, scale, **args):
	"""
	Draws a given letter on canvas c, scaling the size of
	the letter according to scale.  Returns a list of
	handles of canvas objects (lines) that form the new
	object.
	"""
	fontarray = args.pop("font", _DEFAULT_FONT)
	xbase, ybase = basecoords
	retlist = []
	for coordset in fontarray[letter]:
		coords = []
		for coord in coordset:
			coords.append(scale * coord)
		newcoords = []
		for i in range(len(coords)):
			# set cvalue [lindex $coords $i]
			cvalue = coords[i]
			if i % 2:
				newcoords.append(ybase - cvalue)
			else:
				newcoords.append(cvalue + xbase)
		retlist.append(c.create_line(*newcoords, **args))
	return retlist

def draw_string(c, basecoords, string, scale, **args):
	"""
	Draws a string at the given basecoords on canvas c
	and at the given scale.  Args are passed to the canvas
	line object creation command.  Returns a list of all
	canvas object IDs corresponding to the vectors in
	the letters of the string.
	"""
	xbase, ybase = basecoords
	retlist = []
	xcoord, ycoord = xbase, ybase
	for i in range(len(string)):
		char = string[i]
		if char == " ":
			xcoord += 4*scale
		elif char == "\n" or char == "\r":
			xcoord = xbase
			ycoord += 8 * scale
		else:
			r = draw_letter(c, [xcoord, ycoord], char, scale, **args)
			retlist.extend(r)
			xcoord += 5.5 * scale
	return retlist

if __name__ == "__main__":
	# example
	from Tkinter import *
	top = Tk()
	top.title("VectorFont")
	top.state("zoom")
	ca = Canvas(top)
	top.bind("<Escape>", lambda e: top.destroy(), "+")
	ca.pack(expand=YES,fill=BOTH)
	# draw_letter(ca, [100,100], 'A', 5.0,width=5, tag="A")
	TEXT = "Vector Font a"
	draw_string(ca, [100,100], TEXT, 5, tag="my_text")
	G_SCALE = 5
	BASE_COORD = [100,100]
	def _g(*args):
		global G_SCALE
		evt = args[0]
		ca.delete("my_text")
		if evt.delta > 0:
			G_SCALE += 1.0
		if evt.delta < 0:
			G_SCALE -= 1.0
		draw_string(ca, BASE_COORD, TEXT, G_SCALE, tag="my_text")
	def reset_base(evt):
		global BASE_COORD
		BASE_COORD = [top.winfo_pointerx()-top.winfo_rootx(),
				top.winfo_pointery()-top.winfo_rooty()]
		ca.delete("my_text")
		draw_string(ca, BASE_COORD, TEXT, G_SCALE, tag="my_text")
	ca.bind("<Motion>", reset_base, "+")
	ca.focus_force()

	top.bind("<MouseWheel>", _g, "+")
	top.mainloop()