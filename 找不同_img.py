import PIL
from PIL import Image
import os

#os.system('adb shell screencap -p > now.png')
im1 = Image.open("/home/xixi/f_live_me/1.png")
box = (543, 675, 995, 867)
region = im1.crop(box)
region.show()
from piltesseract import get_text_from_image
y = get_text_from_image(region)
if y[:5] == "Asian":
    print('000')
print(y[:5])

#os.system('adb shell input tap 700 1755')
