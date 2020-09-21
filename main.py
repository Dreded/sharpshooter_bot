from mss import mss
import cv2 as cv
from PIL import Image
import numpy as np
from time import time, sleep
import pyautogui


sct = mss()

#whats the resolution? and where to find image?
mon = {'top': 332,'left': 2560+560, 'width': 800,'height': 600}
#mon = sct.monitors[2]
ghost_img = cv.imread('ghost1.png',cv.IMREAD_UNCHANGED)
ghost_img = cv.cvtColor(ghost_img,cv.COLOR_RGB2BGR)

while 1:
    #mousePos = queryMousePosition()
    begin_time = time()
    sct_img = sct.grab(mon)
    screen = np.array(Image.frombytes('RGB', (sct_img.size.width, sct_img.size.height), sct_img.rgb))
    screen = cv.cvtColor(screen, cv.COLOR_RGB2BGR)
    ghostLoc = cv.matchTemplate(screen,ghost_img,cv.TM_CCOEFF_NORMED)
    print(ghostLoc)
    cv.imshow('Screen Cap', ghostLoc)
    print('This frame takes {} seconds.'.format(time()-begin_time))
    
    if cv.waitKey(25) & 0xFF == ord('q'):
        cv.destroyAllWindows()
        break