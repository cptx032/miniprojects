#!/usr/bin/env python
# coding: utf-8
# Author: Willie Lawrence
# Date: 12 09 2015
# Email: cptx032 arroba gmail dot com
import Tkinter as tk
import tkMessageBox

def center_window(window):
	'''
	Center the window on the screen
	'''
	window.update_idletasks()
	w_w = window.winfo_width()
	w_h = window.winfo_height()
	s_w = window.winfo_screenwidth()
	s_h = window.winfo_screenheight()
	window.geometry("+%d+%d" % ( (s_w/2)-(w_w/2), (s_h/2)-(w_h/2) ))

top = tk.Tk()
top.title("::magic::")
top.resizable(0, 0)
top.bind("<Escape>", lambda e : top.quit(), "+")
top.configure(background="#ffffff", border=0)
center_window(top)

top_frame = tk.Frame(top, border=0, highlightthickness=0, bg="white")
bottom_frame = tk.Frame(top, border=0, highlightthickness=0, bg="white")

top_frame.grid(row=0, column=0, pady=5, padx=5)
bottom_frame.grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)

tk.Label(bottom_frame,
	text="Enter with Nth magic square:",
	background="#ffffff").grid(row=0,
	column=0, sticky=tk.W)
Nth_quare = tk.Entry(bottom_frame,
	background="#ffffff", bd=2,
	highlightthickness=1, relief=tk.FLAT,
	insertwidth=1, insertbackground="#999999",
	fg="#999999",width=3,
	highlightcolor="#00aacc")
Nth_quare.grid(row=0,column=1, pady=5, padx=5)
Nth_quare.focus_force()

status_label = tk.Label(bottom_frame,
	text="",
	background="#ffffff", font=("TkDefaultFont",7))
status_label.grid(row=1,column=0, sticky=tk.NW, columnspan=2)

about_button = tk.Button(bottom_frame, text="About",relief=tk.FLAT)
about_button.grid(row=0,column=3)

ABOUT_MSG = """Developed by Willie Lawrence
cptx032 arroba gmail dot com
Solving Jones challenge"""

def _about_handler(*args):
	tkMessageBox.showinfo(title="About", message=ABOUT_MSG)
about_button["command"] = _about_handler

# list of labels with numbers
graphics_mat_widgets = []

def show_matrix(mat):
	'''
	Show in the window the matrix
	'''
	for i in graphics_mat_widgets:
		i.grid_forget()
	for line_i in range(len(mat)):
		for column_i in range(len(mat[line_i])):
			value = mat[line_i][column_i]
			widget = tk.Label(top_frame,text=str(value),
			background="white",
			bd=0,relief=tk.FLAT)
			graphics_mat_widgets.append(widget)
			widget.grid(row=line_i,column=column_i, pady=5, padx=5, sticky=tk.N+tk.W+tk.E+tk.S)
			top.update_idletasks()

def odd(number):
	'''
	Returns true if number is odd
	'''
	return (int(number) % 2) <> 0

def double_even(nth):
	'''
	Returns True if nth is divisible by 4 (double even)
	'''
	return (nth % 4) == 0

def get_Nth_number():
	'''
	Returns the number entered
	'''
	text = Nth_quare.get()
	try:
		n = int(text)
		if n != 2:
			return n
		else:
			return None
	except ValueError:
		return None

Nth_quare.insert(0,"8")

def generate_matrix(Nth):
	'''
	Returns a zeroed matrix
	'''
	mat = []
	for i in range(Nth):
		line = []
		for j in range(Nth):
			line.append(0)
		mat.append(line)
	return mat

SIAMESE = 'S'
EDOUARD = 'E'

def generate_edouard_matrix():
	'''
	Returns a 3x3 (Lo Shu) magic square using Lucas method
	'''
	mat = generate_matrix(3)
	a=5
	b=-1
	c=-3
	mat[0][0] = a+b
	mat[0][1] = a-b-c
	mat[0][2] = a+c

	mat[1][0] = a-b+c
	mat[1][1] = a
	mat[1][2] = a+b-c

	mat[2][0] = a-c
	mat[2][1] = a+b+c
	mat[2][2] = a-b
	return mat

def generate_odd_matrix_with_siamese_method(nth):
	'''
	Returns a matrix using siamese method
	'''
	mat = generate_matrix(nth)
	actual_pos = [0, int(nth/2)]
	last_pos = [0, int(nth/2)]
	actual = 1

	def valid_pos():
		x = (actual_pos[0] >= 0) and (actual_pos[0] <= (nth-1))
		y = (actual_pos[1] >= 0) and (actual_pos[1] <= (nth-1))
		return x and y
	def correct_pos():
		if actual_pos[0] < 0:
			actual_pos[0] = nth-1
		if actual_pos[1] >= nth:
			actual_pos[1] = 0
	def valid_cell():
		return mat[actual_pos[0]][actual_pos[1]] == 0
	def up():
		actual_pos[0] -= 1
		actual_pos[1] += 1
		correct_pos()
	mat[0][nth/2] = actual

	while actual != nth**2:
		actual += 1
		# changing pos
		# up
		up()
		if not valid_cell():
			actual_pos = [last_pos[0]+1, last_pos[1]] # the value below
		##############
		last_pos = [actual_pos[0], actual_pos[1]]
		mat[actual_pos[0]][actual_pos[1]] = actual

	return mat

def make_copy(mat):
	'''
	Returns a copy of a matrix
	'''
	rmat = generate_matrix(len(mat))
	for line_i in range(len(mat)):
		for column_i in range(len(mat)):
			rmat[line_i][column_i] = mat[line_i][column_i]
	return rmat

def make_offset(mat, value):
	'''
	Returns a matrix A plus a value
	'''
	rmat = make_copy(mat)
	for line_i in range(len(mat)):
		for column_i in range(len(mat)):
			rmat[line_i][column_i] = mat[line_i][column_i] + value
	return rmat

def generate_odd_matrix(nth):
	'''
	Returns a Nth matrix with odd methods
	'''
	method = SIAMESE
	if nth == 3: # Lo Shu
		answer = tkMessageBox.askquestion("", "You want use Édouard Lucas's Method?")
		if answer == 'yes':
			method = EDOUARD
	if method == EDOUARD:
		status_label["text"] = "Lo Shu using Édouard Lucas's method (a=5,b=-1,c=-3)"
		return generate_edouard_matrix()
	else:
		if nth == 3:
			status_label["text"] = "Lo Shu using Siamese Method"
		else:
			status_label["text"] = "Odd Magic Square using Siamese Method"
		# [fixme] > Ainda existe uma outra forma de resolucao (Piramide), mas nao irei
		# implementar porque as que estao aqui ja resolvem a proposta de Jones
		return generate_odd_matrix_with_siamese_method(nth)

def generate_simple_even_matrix(nth):
	'''
	Returns a matrix where nth is simply even
	@fixme:  uma refatoração aqui seria uma boa :)
	'''
	mat = generate_matrix(nth)
	sub_square_nth = nth / 2
	nw_square = generate_odd_matrix_with_siamese_method(sub_square_nth)
	se_square = make_offset(nw_square, sub_square_nth**2)
	ne_square = make_offset(nw_square, (sub_square_nth**2)*2)
	sw_square = make_offset(nw_square, (sub_square_nth**2)*3)
	# Pasting  subsquares in main square
	for i in range(sub_square_nth):
		for j in range(sub_square_nth):
			mat[i][j] = nw_square[i][j]
	for i in range(sub_square_nth):
		for j in range(nth-sub_square_nth, nth):
			mat[i][j] = ne_square[i][j-sub_square_nth]
	for i in range(nth-sub_square_nth, nth):
		for j in range(sub_square_nth):
			mat[i][j] = sw_square[i-sub_square_nth][j]
	for i in range(nth-sub_square_nth, nth):
		for j in range(nth-sub_square_nth, nth):
			mat[i][j] = se_square[i-sub_square_nth][j-sub_square_nth]
	marker_number = sub_square_nth / 2
	top_marker = [] # positions of the top sub-sub-square
	for i in range(marker_number):
		for j in range(marker_number):
			top_marker.append([i,j])
	bottom_marker = []
	for i in range(sub_square_nth-marker_number, sub_square_nth):
		for j in range(marker_number):
			bottom_marker.append([i,j])
	center_marker = []
	for i in range(marker_number):
		center_marker.append([sub_square_nth/2,i+1])
	# Right columns switch
	# Switching left markers
	bottom_value_backup = {} # to save old bottom values > top, bottom and center
	for i in top_marker:
		bottom_value_backup[ str(i) ] = mat[i[0]+sub_square_nth][i[1]]
	for i in bottom_marker:
		bottom_value_backup[ str(i) ] = mat[i[0]+sub_square_nth][i[1]]
	for i in center_marker:
		bottom_value_backup[ str(i) ] = mat[i[0]+sub_square_nth][i[1]]
	####### Switching
	# Pasting top to bottom
	for i in top_marker:
		mat[i[0]+sub_square_nth][i[1]] = mat[i[0]][i[1]]
	for i in bottom_marker:
		mat[i[0]+sub_square_nth][i[1]] = mat[i[0]][i[1]]
	for i in center_marker:
		mat[i[0]+sub_square_nth][i[1]] = mat[i[0]][i[1]]
	# Pasting bottom in top
	for key in bottom_value_backup:
		pos = eval(key)
		mat[pos[0]][pos[1]] = bottom_value_backup[key]
	# Switching right side
	right_side_backup = {}
	right_marker = []
	dimension = marker_number - 1
	for line_i in range(sub_square_nth):
		for column_i in range(nth-dimension, nth):
			right_marker.append([line_i, column_i])
	for i in right_marker:
		right_side_backup[ str(i) ] = mat[i[0]+sub_square_nth][i[1]]
	# Top to down
	for i in right_marker:
		mat[i[0]+sub_square_nth][i[1]] = mat[i[0]][i[1]]
	# Down to top
	for key in right_side_backup:
		pos = eval(key)
		mat[pos[0]][pos[1]] = right_side_backup[key]
	status_label["text"] = "Simple even magic square (Strachey Method)"
	return mat

def generate_doubly_even_matrix(nth):
	'''
	Returns a matrix where nth is double even
	'''
	mat = generate_matrix(nth)
	truth_highlight_corners = nth / 4
	# generating truth table
	# NW CORNER
	for line_i in range(truth_highlight_corners):
		for column_i in range(truth_highlight_corners):
			mat[line_i][column_i] = 1
	# SW CORNER
	for line_i in range(nth-truth_highlight_corners, nth):
		for column_i in range(truth_highlight_corners):
			mat[line_i][column_i] = 1
	# NE CORNER
	for line_i in range(truth_highlight_corners):
		for column_i in range(nth-truth_highlight_corners, nth):
			mat[line_i][column_i] = 1
	# SE CORNER
	for line_i in range(nth-truth_highlight_corners, nth):
		for column_i in range(nth-truth_highlight_corners, nth):
			mat[line_i][column_i] = 1
	# Center of Square
	for line_i in range(truth_highlight_corners, nth-truth_highlight_corners):
		for column_i in range(truth_highlight_corners, nth-truth_highlight_corners):
			mat[line_i][column_i] = 1
	# Filling normal and inverse orders cell (1s and 0s respectively)
	count = 0
	for i in range(nth):
		for j in range(nth):
			number = ((i*nth) + j)+1
			if mat[i][j] == 1:
				mat[i][j] = number
			else:
				mat[i][j] = (nth**2)-number+1
	status_label["text"] = "Doubly even magic square (Truth Table Method)"
	return mat

def _entry_enter(event):
	'''
	Event handler
	'''
	number = get_Nth_number()
	if number:
		if odd(number):
			mat = generate_odd_matrix(number)
			show_matrix(mat)
		else:
			if not double_even(number):
				mat = generate_simple_even_matrix(number)
				show_matrix(mat)
			else:
				mat = generate_doubly_even_matrix(number)
				show_matrix(mat)
	else:
		tkMessageBox.showinfo(title="Ops", message="The number must be valid!")
Nth_quare.bind("<Return>", _entry_enter, "+")
top.mainloop()
