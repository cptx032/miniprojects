#!/usr/bin/env python2
# coding: utf-8

u"""Mixer. Requires pyglet and numpy."""

import sys
import Tkinter as tk

import pyglet
import numpy


def lerp(a, b, x):
    u"""Linear interpolation."""
    return a + ((b - a) * x)


media = pyglet.media.load(sys.argv[1])
raw_data = media.get_audio_data(1).data
last_data = raw_data
while last_data:
    last_data = media.get_audio_data(255)
    if last_data:
        raw_data += last_data.data

if media.audio_format.sample_size == 16:
    data = numpy.fromstring(raw_data, 'Int16')
    MAX_Y_VALUE = 32767.0
else:
    raise ValueError(u'Wrong wave file')


class FrequencyView(object, tk.Canvas):
    def __init__(self, *args, **kwargs):
        self.data = kwargs.pop('data')
        self.color = kwargs.pop('color', '#00aacc')
        self.draw_index = None
        tk.Canvas.__init__(self, *args, **kwargs)
        self.bind('<Configure>', self.__configure, '+')

    def __configure(self, event=None):
        self.generate_graph()

    def generate_graph(self):
        width = int(self.winfo_width())
        height = int(self.winfo_height())
        len_samples = len(self.data)

        y_offset = height / 2

        # traveling the widget's width
        points = []
        for x in range(0, width):
            normalized = x / float(width)
            index = int(lerp(0, len_samples, normalized))

            y = ((self.data[index] * height) / MAX_Y_VALUE) + y_offset
            points.extend([x, y])

        if self.draw_index:
            self.coords(self.draw_index, *points)
        else:
            self.draw_index = self.create_line(*points, fill=self.color)

if __name__ == '__main__':
    top = tk.Tk()
    top['bg'] = '#333'
    ca = FrequencyView(top, bd=0, highlightthickness=0, bg='#333', data=data)
    ca.pack(expand='yes', fill='both')
    top.title(u'Mixer')
    top.bind('<Escape>', lambda e: top.destroy(), '+')
    top.mainloop()
