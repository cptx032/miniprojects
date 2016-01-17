# Author: Willie Lawrence - cptx032 arroba gmail dot com
print "Spriter - An sprite tool"
print "This script takes a lot of images and join it together in a horizontal image"

import glob
import Image
files = glob.glob("*.png")
print "Files to join:", "\n".join(files), "\n"
answer = raw_input("Confirms? (Y/n) ").lower()

if answer == "" or answer == "y":
	images = [Image.open(i) for i in files]
	width, height = images[0].size
	final_image = Image.new(
			"RGBA",
			(
				width*len(files),
				height
			)
		)
	for i in range(len(files)):
		final_image.paste(images[i],
				(
					i*width,
					0
				)
			)
	final_image.save(raw_input("Enter destiny name: "), "PNG")
