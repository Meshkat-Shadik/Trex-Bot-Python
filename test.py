import time

from PIL import ImageGrab,ImageOps
import pyautogui
from numpy import *
setx=0
class Coordinates():
    replayBtn= (340,390)
    dino = (160,395)
    # 272,225
# 243 = half
def restartgame():
    pyautogui.click(Coordinates.replayBtn)


# restartgame()
def spacepress():
    pyautogui.keyDown('space')
    time.sleep(0.05)
    print('jump')
    pyautogui.keyUp('space')

restartgame()
time.sleep(1)
spacepress()
# if(spacepress()==True):
#     print("second")
def imagegrab():
    box = (Coordinates.dino[0]+64,Coordinates.dino[1],Coordinates.dino[0]+104,Coordinates.dino[1]+30)
    # print(1)
    image = ImageGrab.grab(box)
    grayImage = ImageOps.grayscale(image)
    a = array(grayImage.getcolors())
    # print("x")
    print (a.sum())
    return (a.sum())

def main():
    restartgame()
# spacepress()
    while True:
         imagegrab()
         if(imagegrab()!=1455):
            time.sleep(0.12)
            print("Hi")
            spacepress()


             # spacepress()


main()

# while True:
#     imagegrab()
#     #     if(imagegrab() == )




#
# clicking()
# time.sleep(1)
# spacepress()