#!/usr/bin/env python3
import pyscreenshot as screen
from PIL import ImageFilter, Image
import os

# Path to temporary lockscreen picture
path = "/tmp/screen.png"

def __init__ ():

    # make screenshot and save it to temporary location
    image = screen.grab()
    image.save(path)

    # set blur filter over lock picture
    blurred_image = Image.open(path)
    blurred_image = blurred_image.filter(ImageFilter.GaussianBlur(6))
    blurred_image.save(path)

    # start i3lock with blurred picture (-i parameter + picture file)
    os.system("i3lock -i " + path)


if __name__ == "__main__":
    __init__()