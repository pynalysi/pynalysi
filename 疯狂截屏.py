import os


for i in range(33):
    os.system('adb shell screencap -p > ' + str(i) + '.png')
