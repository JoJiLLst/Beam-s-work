from PIL import Image
image = Image.open(r"D:\jillzaza\Coding_area\Main project work\Code\Beam's work\Human face\Humanface_1.jpg")
newsize = (256, 256)
susimage = image.resize(newsize)
susimage.show()