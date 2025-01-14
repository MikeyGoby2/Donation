import pyautogui as pt
from time import sleep
import win32gui, win32con
import keyboard
from sys import exit
from PIL import ImageGrab

sleep(0.2)

hwnd = win32gui.GetForegroundWindow()
win32gui.ShowWindow(hwnd, win32con.SW_MINIMIZE)

sleep(0.2)

##############################################################################################

# Main loop
while not keyboard.is_pressed('q'):
    
    sleep(0.5)
    
    # Click on green
    pt.moveTo(843, 394)
    sleep(0.2)
    pt.click()
    
    sleep(0.5)
    
    # Click on gold
    pt.moveTo(958, 758)
    sleep(0.2)
    pt.click()
    
    # search for donation
    donation= pt.locateCenterOnScreen("imgs/donation.png", grayscale=False, region=(803, 251, 318, 47), confidence=0.9)

    sleep(0.2)

    if donation is not None:
        print("i see donation")
    
    