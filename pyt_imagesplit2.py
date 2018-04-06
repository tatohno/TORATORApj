#!/usr.bin/python
# codeing UTF-8

from PIL import Image
import os

infiles = os.listdir('c:\Users\InfoDeliver\python')

im = Image.open('testjpg.jpg')

aftsz = int(im.size[1] / 2)
outim1 = im.crop((1, 1, im.size[0], aftsz))

outim1.save('testout1.jpg')
