
import os
import time
import os
from time import sleep


def entry_challenge():
    tap_screen(500, 500)
    print('进入对战模式')
    tap_screen(1200, 700)
    print('进入冒险模式')
    tap_screen(900, 600)
    print('进入挑战')
    tap_screen(450, 300)
    print('选择陨落的废都')
    tap_screen(1050, 250)
    print('召唤师战场')
    tap_screen(1600, 1000)
    print('选择下一步')
    tap_screen(1500, 900)
    print('闯关')
    tap_screen(1200, 700)
    print('进入关卡')
    sleep(31)

    print('f:1')
    a = 10
    while a>1:
        asdfds = os.system('adb shell input tap 1736 920')
        print(a)
        a-=1
    sleep(3)

    print('f:2')
    b = 10
    while b>1:
        asdfds = os.system('adb shell input tap 1736 920')
        print(b)
        b-=1
    sleep(9)

    print('f:3')
    c = 15
    while c>1:
        asdfds = os.system('adb shell input tap 1736 920')

        c-=1
    sleep(3)

    print('f:4')
    c = 15
    while c>1:
        asdfds = os.system('adb shell input tap 1736 920')
        c-=1

    sleep(7)



def repeat_change():
    #sleep(5)
    print('跳过')
    tap_screen(950, 1000)
    sleep(7)

    print('点击屏幕继续')
    tap_screen(1000, 500)
    sleep(3)

    print('再次挑战')
    tap_screen(1500, 950)
    sleep(8)

    print('闯关')
    tap_screen(1500, 950)
    sleep(1)

    sleep(27)

    print('f:1')
    a = 10
    while a>1:
        asdfds = os.system('adb shell input tap 1736 920')
        print(a)
        a-=1
    sleep(3)

    print('f:2')
    b = 10
    while b>1:
        asdfds = os.system('adb shell input tap 1736 920')
        print(b)
        b-=1
    sleep(9)

    print('f:3')
    c = 15
    while c>1:
        asdfds = os.system('adb shell input tap 1736 920')

        c-=1
    sleep(3)

    print('f:4')
    c = 12
    while c>1:
        asdfds = os.system('adb shell input tap 1736 920')
        c-=1

    sleep(3)

    tap_screen(950, 900)

    repeat_change()


def tap_screen(x, y):
    os.system('adb shell input tap {} {}'.format(x, y))


if __name__ == '__main__':
    entry_challenge()
    #repeat_change()
