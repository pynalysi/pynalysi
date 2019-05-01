import random
import os
import time
from time import sleep
import shortuuid
import random

t_start = int(time.time())

t_end = 3600 * 3 + t_start





#restart()

z = True


while z :

    x = t_end - int(time.time())
    print(x)
    if x < 0:
        z = False


    a = random.randrange(1,9)
    b = random.randrange(7,13)

    c = 639 + a
    d = 953 + b

    #print(c,' ',d)

    os.system('adb shell input tap ' + str(c) + ' ' + str(d))
    #os.system('adb shell input tap 1188 1141')
