import glob
from PIL import Image
path="D:\\jillzaza\\Coding_area\\Main project work\\Code\\Beam's work\\Human face\\"
print('\nNamed with wildcard ranges:')
for files in glob.glob(path + '/*[1-50].*'):
    image = Image.open((files))
    newsize = (256, 256) #50*50
    susimage = image.resize(newsize)
    susimage.show()
    susimage.save((files), 'PNG')
    