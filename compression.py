from PIL import Image
import PIL
import os
import glob

#dir(Image)
# im = Image.open("E:\systems\Python\Image-compression\my-passport-photo.jpg")
# print("The image size dimensions are:")
# print(im.size)
# #The image size dimensions are: (1920, 1280)

file_name = "italy-1-compressed.jpg"
picture = Image.open("italy-4256017.jpg")
dim = picture.size
print("This is the current width and height of the image:")
print(dim)

picture.save("Compressed1_" + file_name, optimize=True, quality=1)

newPicture = Image.open("Compressed1_italy-1-compressed.jpg")
dimPic = newPicture.size
print("This is the current width and height of the compressed-image:")
print(dimPic)
