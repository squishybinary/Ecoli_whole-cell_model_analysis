# This doesn't work as I would want
# Need to implement using magick cmd line:
# for root, dirs, files in os.walk(".", topdown=True):
#    for name in files:
#        print(name)

from wand.image import Image, COMPOSITE_OPERATORS
from wand.drawing import Drawing
from wand.display import display
from wand.color import Color


### Overlay all png files in folder
import os

#make sure to duplicate one of the files and rename as tmp.png first
#works as starting image

for root, dirs, files in os.walk(".", topdown=True):
    for name in files:
        if name == 'background_wand.py':
            pass
        else:
            nextimage = Image(filename=name)
            with Image(filename='tmp.png') as img:
                img.composite(nextimage)
                img.save(filename='tmp.png')
    
with Image(filename='tmp.png') as img:
    img.save(filename='backgroundWT.png')