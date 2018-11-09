import os
from PIL import Image
from PIL import ImageOps

#list of file types to accept for now
acceptedFileTypes = [".bmp",".eps",".gif",".icns",".ico",".im",".jpg",".jpeg",".png",".tiff",".tif"]

#check if file input is valid
inFile = False
while (inFile == False):
    filepath = input("Please specify filepath for square cropping in quotes: ")
    if (os.path.splitext(filepath)[1] in acceptedFileTypes):
        inFile = True
    else:
        print ("Accepted File Types are: ")
        for i in acceptedFileTypes:
            print i

im = Image.open(filepath)

#get image dimensions in pixel
width, height = im.size

#determine the max size of a the square to be cropped
max_size = min(width, height)

#perform center crop
crop_im = ImageOps.fit(im, (max_size, max_size), centering=(0.5, 0.5))

crop_im.show()

#save file
crop_im.save("crop.png")