# coding: utf-8
from Tkinter import *

class MaterialEntry(Frame):
	def __init__(self, *args, **kws):
		self.placeholder = kws.pop('placeholder', '')
		self.placeholder_color = kws.get('phcolor', '#999')
		self.fg_color = kws.get('bg', '#000')
		Frame.__init__(self, *args, **kws)
		self.entry = Entry(self)
		self.entry.configure(
			insertwidth=kws.get('insertwidth', 1),
			border=kws.get('border', 0),
			highlightthickness=kws.get('highlightthickness', 5),
		)
		self.entry.update_idletasks()
		self.canvas = Canvas(self, bd=0, highlightthickness=0, height=2, bg='#ddd', width=self.entry.winfo_width())
		_parent_color = self.master['bg']
		self.entry.configure(
			bg=_parent_color,
			highlightcolor=_parent_color
		)
		self.update_placeholder()
		self.entry.bind('<Any-KeyPress>', self._kb_handler, '+')
		self.entry.bind('<FocusOut>', lambda e : self.update_placeholder(), "+")
		self.entry.bind('<FocusIn>', lambda e : self.update_placeholder(), "+")
		self.entry.bind('<1>', lambda e : self.update_placeholder(), "+")

		self.entry.bind('<FocusIn>', self._focus_in, '+')
		self.entry.bind('<FocusOut>', self._focus_out, '+')

		self.entry.grid(pady=0, padx=5, row=0, column=0)
		self.canvas.grid(row=1, column=0, sticky=W+E)

	def _focus_in(self, event):
		self.canvas['bg'] = '#00aacc'

	def _focus_out(self, event):
		self.canvas['bg'] = '#ddd'

	def update_placeholder(self):
		print "enter"
		if self.entry.get() == '':
			self.entry.configure(foreground=self.placeholder_color)
			self.entry.insert(0, self.placeholder)
		if self.entry.get() == self.placeholder and self.entry['fg'] == self.placeholder_color:
			self.entry.icursor(0)

	def _kb_handler(self, event):
		# if event.keysym is visible key
		if self.entry.get() == self.placeholder and self.entry['fg'] == self.placeholder_color:
			self.entry['fg'] = self.fg_color
			self.entry.delete(0,END)

top = Tk()
Label(top, text="Login", bg=top['bg'], font=('TkDefaultFont',10,'bold')).grid(row=0,column=0,pady=5, padx=5)
e = MaterialEntry(placeholder="Username")
e.grid(row=1, column=0,padx=5, pady=5)
e.entry.focus_force()

f = MaterialEntry(placeholder="Password")
f.grid(row=2, column=0,padx=5, pady=5)
f.focus_force()

Button(top, relief=FLAT, bg='#ddd', text="Ok", width=20,bd=0,highlightthickness=5).grid(row=3, column=0, pady=5, padx=5)

top.bind('<Escape>', lambda e : top.quit(), "+")
top.mainloop()
