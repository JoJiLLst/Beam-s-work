from PIL import Image

im = Image.open(r"D:\jillzaza\Coding_area\Main project work\Code\Beam's work\test image.png")

print(im.size)
print(type(im.size))
# (400, 225)
# <class 'tuple'>

w, h = im.size
print('width: ', w)
print('height:', h)