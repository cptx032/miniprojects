
<!-- saved from url=(0038)http://pastebin.com/raw.php?i=mpi06NTu -->
<html><head><meta http-equiv="Content-Type" content="text/html; charset=UTF-8"></head><body><pre style="word-wrap: break-word; white-space: pre-wrap;">#!/usr/bin/env python
# Author: cptx032
# Mail-me: cptx032@gmail.com
import sys, os
from Tkinter import *
top = Tk()
top.title("tk-leds")
top.bind("&lt;Escape&gt;", lambda e:top.destroy())
e = Entry(top,bd=5,highlightcolor="white",relief=FLAT)
e.focus_force()
Label(top, text="tty").grid(pady=5,padx=5,row=0,column=0)
e.grid(pady=5,padx=5,row=0,column=1,columnspan=2,sticky=W+E)

if len(sys.argv) &gt; 1:
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
	__command = "setleds -num -caps -scroll &lt; %s" % (e.get())
	if os.system(__command) != 0:
		set_status("error")
	else:
		set_status("success")
	numbtn["text"] = "+num"
	capsbtn["text"] = "+caps"
	scrollbtn["text"] = "+scroll"
clearbtn.bind("&lt;Button-1&gt;", _reset, "+")

numbtn.grid(row=1,column=0)
capsbtn.grid(row=1,column=1)
scrollbtn.grid(row=1,column=2)

def _num(*args):
	if e.get() == "":
		set_status("error")
		return
	if numbtn["text"][0] == "+":
		if os.system("setleds +num &lt; %s" % (e.get())) != 0:
			set_status("error")
		numbtn["text"] = "-num"
	else:
		if os.system("setleds -num &lt; %s" % (e.get())) != 0:
			set_status("error")
		numbtn["text"] = "+num"
numbtn.bind("&lt;Button-1&gt;", _num, "+")

def _caps(*args):
	if e.get() == "":
		set_status("error")
		return
	if capsbtn["text"][0] == "+":
		if os.system("setleds +caps &lt; %s" % (e.get())) != 0:
			set_status("error")
		capsbtn["text"] = "-caps"
	else:
		if os.system("setleds -caps&lt; %s" % (e.get())) != 0:
			set_status("error")
		capsbtn["text"] = "+caps"
capsbtn.bind("&lt;Button-1&gt;", _caps, "+")

def _scroll(*args):
	if e.get() == "":
		set_status("error")
		return
	if scrollbtn["text"][0] == "+":
		if os.system("setleds +scroll &lt; %s" % (e.get())) != 0:
			set_status("error")
		scrollbtn["text"] = "-scroll"
	else:
		if os.system("setleds -scroll &lt; %s" % (e.get())) != 0:
			set_status("error")
		scrollbtn["text"] = "+scroll"
scrollbtn.bind("&lt;Button-1&gt;", _scroll, "+")

top.mainloop()</pre></body></html>