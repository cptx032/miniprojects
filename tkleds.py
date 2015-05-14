#!/usr/bin/env python
# Author: cptx032
# Mail-me: cptx032 arroba gmail dot com
# Also available here: http://pastebin.com/raw.php?i=mpi06NTu
import sys, os
from Tkinter import *

def centralize(_window):
	_window.update_idletasks()
	width, height = _window.winfo_width(), _window.winfo_height()
	sw,sh = _window.winfo_screenwidth(), _window.winfo_screenheight()
	_window.geometry("+%d+%d" % (sw/2-width/2, sh/2-height/2))

top = Tk()
top.title("tk-leds")
top.resizable(0,0)
centralize(top)
top.bind("<Escape>", lambda e:top.destroy())
e = Entry(top,bd=5,highlightcolor="white",relief=FLAT)
e.focus_force()
Label(top, text="tty").grid(pady=5,padx=5,row=0,column=0)
e.grid(pady=5,padx=5,row=0,column=1,columnspan=2,sticky=W+E)

if len(sys.argv) > 1:
	e.insert(0, sys.argv[1])

numbtn = Button(top,text="+num",width=10)
capsbtn = Button(top,text="+caps",width=10)
scrollbtn = Button(top,text="+scroll",width=10)

clearbtn = Button(top,text="reset")
clearbtn.grid(pady=0,padx=0,columnspan=3,row=2,column=0,sticky=W+E)

def set_status(status=None):
	if status == "error":
		e["bg"] = "red"
		e["fg"] = "white"
	else:
		e["bg"] = "white"
		e["fg"] = "black"

def _reset(*args):
	if e.get() == "":
		set_status("error")
		return
	__command = "setleds -num -caps -scroll < %s" % (e.get())
	if os.system(__command) != 0:
		set_status("error")
	else:
		set_status("success")
	numbtn["text"] = "+num"
	capsbtn["text"] = "+caps"
	scrollbtn["text"] = "+scroll"
clearbtn.bind("<Button-1>", _reset, "+")

numbtn.grid(row=1,column=0)
capsbtn.grid(row=1,column=1)
scrollbtn.grid(row=1,column=2)

# [fixme] > as tres funcoes seguem a mesma estrutura > refatorar!
def _num(*args):
	if e.get() == "":
		set_status("error")
		return
	if numbtn["text"][0] == "+":
		if os.system("setleds +num < %s" % (e.get())) != 0:
			set_status("error")
		numbtn["text"] = "-num"
	else:
		if os.system("setleds -num < %s" % (e.get())) != 0:
			set_status("error")
		numbtn["text"] = "+num"
numbtn.bind("<Button-1>", _num, "+")

def _caps(*args):
	if e.get() == "":
		set_status("error")
		return
	if capsbtn["text"][0] == "+":
		if os.system("setleds +caps < %s" % (e.get())) != 0:
			set_status("error")
		capsbtn["text"] = "-caps"
	else:
		if os.system("setleds -caps < %s" % (e.get())) != 0:
			set_status("error")
		capsbtn["text"] = "+caps"
capsbtn.bind("<Button-1>", _caps, "+")

def _scroll(*args):
	if e.get() == "":
		set_status("error")
		return
	if scrollbtn["text"][0] == "+":
		if os.system("setleds +scroll < %s" % (e.get())) != 0:
			set_status("error")
		scrollbtn["text"] = "-scroll"
	else:
		if os.system("setleds -scroll > %s" % (e.get())) != 0:
			set_status("error")
		scrollbtn["text"] = "+scroll"
scrollbtn.bind("<Button-1>", _scroll, "+")

top.mainloop()
