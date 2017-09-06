import Tkinter as tk

def lerp(a,b,x):
	return a + ((b-a)*x)

def get_x(a,b,lerp_result):
	return (lerp_result-a) / (float(b)-a)

def get_rgb(r,g,b):
	return "#%02x%02x%02x" % (r,g,b)

def gradient(canvas, x, y, width, height, downcolor, upcolor, tag=None, outline=None):
	Dcolor = [i/256 for i in canvas.winfo_rgb(downcolor)]
	Ucolor = [i/256 for i in canvas.winfo_rgb(upcolor)]
	for ny in range(y,height+y):
		xlerp = get_x(y, y+height, ny)
		ncolor = [int(lerp(Ucolor[i], Dcolor[i], xlerp)) for i in range(3)]
		canvas.create_line(x,ny,x+width,ny, fill=get_rgb(*ncolor),tag=tag)
	if outline:
		canvas.create_rectangle(x,y,x+width, y+height, outline=outline, tag=[tag,tag+'outline'])

top = tk.Tk()
top.bind("<Escape>", lambda e : top.quit(), "+")
ca = tk.Canvas(top,width=640,height=480)
ca.grid()

# gradient(ca,100,50,100,50,"#ff0000","#00aacc",tag="heiman", outline="green")

def motion(evt):
	ca.delete("heiman")
	gradient(ca,100,50,evt.x,evt.y,"#ccc","#eee",tag="heiman")
ca.bind("<B1-Motion>", motion, "+")

top.update_idletasks()
top.mainloop()