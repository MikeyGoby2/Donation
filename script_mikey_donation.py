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
print("####    SETTING DONATION    ####") 
print("")
print("START setting donation")

if pt.pixel(532, 286)[0] == 84:
    print("i see donation")
    
else:
    print("    i NOT see donation")
    print("setup donation")

pt.press("c")
print("go to clan")

sleep(0.5)

#click on donation
pt.moveTo(1036, 660)
sleep(0.05)
pt.click()
print("clickt donation")
print("")
    
# Main loop
while not keyboard.is_pressed('q'):
    
    sleep(0.5)
        
    # check for reset
    if pt.pixel(908, 698)[0]== 209:
        print("i see reset")
        
        #click on reset
        pt.moveTo(908, 698)
        sleep(0.05)
        pt.click()
        print("clickt reset")
        print("")
        
        sleep(0.05)
      
    else:
        print("no reset")
            
        if pt.pixel(1276, 793)[0] == 207:
            print("i see 2th gold")
            
            #click on 2th gold
            pt.moveTo(1276, 793)
            sleep(0.05)
            pt.click()
            print("clickt 2th gold")
            print("")
            
            sleep(0.3)
        
        else:
            print("no 2th gold")
            
            # check for 1th gold
            if pt.pixel(1077, 790)[0] == 199:
                print("i see 1th gold")
                
                #click on 1st gold
                pt.moveTo(1077, 790)
                sleep(0.05)
                pt.click()
                print("clickt 1th gold")
                print("")
                
                sleep(0.3)
                              
            else:
                print("no 1th gold")
                
                # click on green
                pt.moveTo(1174, 693)
                sleep(0.05)
                pt.click()
                print("clickt green")
                print("")
                
                sleep(0.05)
        
