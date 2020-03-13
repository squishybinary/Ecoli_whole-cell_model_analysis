from wand.image import Image, COMPOSITE_OPERATORS
from wand.drawing import Drawing
from wand.display import display
from wand.color import Color


### Make all png files in folder transparent
import os
import re

slash = re.compile(r'\\')
dot = re.compile(r'^.')

for root, dirs, files in os.walk(".", topdown=True):
    for name in files:
        nameending = name[-3:]
        directory = root
        copyofroot = root
        if nameending != 'png':
            pass
        else:
            originalname = os.path.join(root, name)
            copyofroot = slash.sub('_', copyofroot)
            copyofroot = dot.sub('', copyofroot)
      
            if len(name) == 15:
                #replication.png
                newname = copyofroot + '_oric.png'
            if len(name) == 23:
                #massFractionSummary.png
                newname = copyofroot + '_summary.png'
            if len(name) == 25:
                #histogramdoublingtime.png
                newname = copyofroot + '_doubling.png'

            with Image(filename=originalname) as img:
                with Color('#FFFFFF') as white:
                    img.transparent_color(white, alpha=0.0)
                
                    # Use for comparison
                    # version saves new file in directory location
                    img.save(filename=os.path.join(directory, newname))
                    
                    # Use for background
                    # version saves all new files in top folder
                    #img.save(filename=newname)
        
            namesplit = newname.split('_')
            if namesplit[7] == 'summary.png':
                with Image(filename=os.path.join(directory, 'backgroundWT.png')) as img:
                    overlay = Image(filename=newname)
                    img.composite(overlay)
                    comparisonname = 'comparison_' + newname
                    img.save(filename=comparisonname)
            else:
                pass
 