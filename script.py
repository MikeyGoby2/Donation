import pyautogui as pt
from time import sleep
import keyboard
import win32api, win32con, win32gui


sleep(0.2)

hwnd = win32gui.GetForegroundWindow()
win32gui.ShowWindow(hwnd, win32con.SW_MINIMIZE)

sleep(0.2)

pt.FAILSAFE = True 

s = pt.screenshot("imgs/screenshot.png", region=(850,636,594,277))

#for x in range(44):
while 1:  
    if pt.pixel(1186,700)[0] == 75:
        while pt.pixel(1186,700)[0] == 75:
            sleep(0.05)
            pt.click(1186,700)
            
        print("green")
        sleep(0.7)
        
    if pt.pixel(1177,691)[0] == 117:
        while pt.pixel(1177,691)[0] == 117:
            sleep(0.05)
            pt.click(1177,691)
            
        print("green light")
        sleep(0.7)
        
    if pt.pixel(1078,789)[0] == 189:
        while pt.pixel(1078,789)[0] == 189:
            sleep(0.05)
            pt.click(1078,789)
            
        print("orange1")
        sleep(0.5)
        
        if pt.pixel(1283,790)[0] == 188:
            while pt.pixel(1283,790)[0] == 188:
                sleep(0.05)
                pt.click(1283,790)
                
            print("orange2")
            sleep(0.5)
            
        if pt.pixel(1277,789)[0] == 202:
            while pt.pixel(1277,789)[0] == 202:
                sleep(0.05)
                pt.click(1277,789)
                
            print("orange2 light")
            sleep(0.5)
        
    if pt.pixel(1080,789)[0] == 202:
        while pt.pixel(1080,789)[0] == 202:
            sleep(0.05)
            pt.click(1080,789)
            
        print("orange1 light")
        sleep(0.5)
        
        if pt.pixel(1283,790)[0] == 188:
            while pt.pixel(1283,790)[0] == 188:
                sleep(0.05)
                pt.click(1283,790)
                
            print("orange2")
            sleep(0.5)
            
        if pt.pixel(1277,789)[0] == 202:
            while pt.pixel(1277,789)[0] == 202:
                sleep(0.05)
                pt.click(1277,789)
                
            print("orange2 light")
            sleep(0.5)
        
    if pt.pixel(1283,790)[0] == 188:
        while pt.pixel(1283,790)[0] == 188:
            sleep(0.05)
            pt.click(1283,790)
            
        print("orange2")
        sleep(0.5)
        
    if pt.pixel(1277,789)[0] == 202:
        while pt.pixel(1277,789)[0] == 202:
            sleep(0.05)
            pt.click(1277,789)
            
        print("orange2 light")
        sleep(0.5)
        
    if pt.pixel(1020,696)[0] == 205:
        while pt.pixel(1020,696)[0] == 205:
            sleep(0.05)
            pt.click(1020,696)
            
        print("reset")
        sleep(0.5)
