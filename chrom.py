#!/usr/bin/env python
# Author: cptx032
# Mail-me: cptx032@gmail.com
from Tkinter import *
top = Tk()
SEC = 0
HOUR = 0
MIN = 0
PAUSED = True
MINIMIZED = False
top.withdraw()
top.config(bg="#333")
top.overrideredirect(1)
top.attributes("-alpha",0.9, "-topmost",1)
top.geometry("%dx%d+%d+0" % (200, top.winfo_screenheight(), top.winfo_screenwidth()-200))
top.deiconify()
top.focus_force()
la = Label(top, font=("TkDefaultFont",18),text="test",justify=RIGHT,fg="white",bg="#333")
la.pack(pady=5, padx=5,anchor=E, expand=YES,fill=Y)
top.bind("<Escape>", lambda e:top.destroy(), "+")

def _update_time(*args):
	top.after(1000, _update_time)
	if not PAUSED:
		return
	global HOUR, MIN, SEC
	SEC += 1
	if SEC == 60:
		SEC = 0
		MIN += 1
	if MIN == 60:
		HOUR += 1
		MIN = 0
	la["text"] = ":chrom\n%02d:%02d:%02d" % (HOUR, MIN, SEC)
_update_time()

def _fix_win_bar_problem(*arg):
	top.after(1, _fix_win_bar_problem)
	top.attributes("-top",1)
_fix_win_bar_problem()

def _handler_pause(*args):
	global PAUSED
	PAUSED = not PAUSED
top.bind("<1>", _handler_pause, "+")

def _handler_clear(*args):
	global HOUR, MIN, SEC
	HOUR, MIN, SEC = 0,0,0
	la["text"] = ":chrom\n00:00:00"
top.bind("<3>", _handler_clear, "+")

def _handler_quit(*args):
	top.destroy()
# top.bind("<2>", _handler_quit, "+")

def _handler_minimize(*args):
	global MINIMIZED
	if not MINIMIZED:
		MINIMIZED = True
		top.geometry("%dx%d+%d+0" % (20, top.winfo_screenheight(), top.winfo_screenwidth()-20))
	else:
		MINIMIZED = False
		top.geometry("%dx%d+%d+0" % (200, top.winfo_screenheight(), top.winfo_screenwidth()-200))

top.bind("<MouseWheel>", _handler_minimize, "+")

def _h_focus_in(*args):
	top["bg"] = "#333"
	la["bg"] = "#333"
#top.bind("<FocusIn>", _h_focus_in, "+")

def _h_focus_out(*args):
	top["bg"] = "#ddd"
	la["bg"] = "#ddd"
#top.bind("<FocusOut>", _h_focus_out, "+")

top.mainloop()