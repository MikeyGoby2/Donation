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

# screenshot
ImageGrab.grab().save("C:/Users/mikey/Desktop/Visual Studio Files/Mikey/donation/screenshot/donation.png")
ImageGrab.grab(bbox=(803, 251, 1121, 298)).save("C:/Users/mikey/Desktop/Visual Studio Files/Mikey/donation/screenshot/donation_region.png")

# search for donation
donation= pt.locateCenterOnScreen("imgs/donation.png", grayscale=False, region=(803, 251, 318, 47), confidence=0.9)

sleep(0.2)

if donation is not None:
    print("i see donation")
    print("END setting donation")   
    
else:
    print("    i NOT see donation")
    
    # check for mansion
    ##############################################################################################
    
    # screenshot mansion
    ImageGrab.grab().save("C:/Users/mikey/Desktop/Visual Studio Files/Mikey/donation/screenshot/mansion.png")
    ImageGrab.grab(bbox=(912, 943, 1013, 1023)).save("C:/Users/mikey/Desktop/Visual Studio Files/Mikey/donation/screenshot/mansion_region.png")
    
    # search for mansion
    clan= pt.locateCenterOnScreen("imgs/clan.png", grayscale=False, region=(1108, 952, 74, 71), confidence=0.9)
    
    if clan is None:
        print("        i NOT see mansion")
        
        pt.press("esc")
        
        # new screen
        sleep(2)
        
    else:
        # click clan
        ##############################################################################################
        
        # screenshot clan
        ImageGrab.grab().save("C:/Users/mikey/Desktop/Visual Studio Files/Mikey/donation/screenshot/clan.png")
        ImageGrab.grab(bbox=(1108, 952, 1182, 1023)).save("C:/Users/mikey/Desktop/Visual Studio Files/Mikey/donation/screenshot/clan_region.png")
        
        # search for clan
        clan= pt.locateCenterOnScreen("imgs/clan.png", grayscale=False, region=(1108, 952, 74, 71), confidence=0.9)
        
        pt.moveTo(clan)
        sleep(0.2)
        pt.click()
        print("clickt clan")
        
        # click clan_donation
        ##############################################################################################
        
        # screenshot clan_donation
        ImageGrab.grab().save("C:/Users/mikey/Desktop/Visual Studio Files/Mikey/donation/screenshot/clan_donation.png")
        ImageGrab.grab(bbox=(989, 300, 1456, 770)).save("C:/Users/mikey/Desktop/Visual Studio Files/Mikey/donation/screenshot/clan_donation_region.png")
        
        # search for clan_donation
        clan_donation= pt.locateCenterOnScreen("imgs/clan_donation.png", grayscale=False, region=(989, 300, 467, 470), confidence=0.9)
        
        pt.moveTo(clan_donation)
        sleep(0.2)
        pt.click()
        print("clickt clan_donation")
        print("END setting donation")
    
##############################################################################################
print("####    WHILE DONATION    ####") 
print("")
print("START donation")

# while donation
while keyboard.is_pressed('q') == False:
    
    # check for refresh
    ##############################################################################################

    # screenshot refresh
    ImageGrab.grab().save("C:/Users/mikey/Desktop/Visual Studio Files/Mikey/donation/screenshot/refresh.png")
    ImageGrab.grab(bbox=(747, 535, 1173, 578)).save("C:/Users/mikey/Desktop/Visual Studio Files/Mikey/donation/screenshot/refresh_region.png")
    
    # search for refresh
    refresh= pt.locateCenterOnScreen("imgs/refresh.png", grayscale=False, region=(744, 533, 432, 43), confidence=0.9)
    
    if refresh is not None:
        print("i see refresh")
       
        pt.click(957, 695)
        print("clickt refresh")

    else:
        print("    i NOT see refresh")
        
        # check for gold 2
        ##############################################################################################
        
        # screenshot gold2
        ImageGrab.grab().save("C:/Users/mikey/Desktop/Visual Studio Files/Mikey/donation/screenshot/gold2.png")
        ImageGrab.grab(bbox=(1247, 772, 1404, 820)).save("C:/Users/mikey/Desktop/Visual Studio Files/Mikey/donation/screenshot/gold2_region.png")
        
        # search for refresh
        gold2= pt.locateCenterOnScreen("imgs/gold2.png", grayscale=False, region=(1247, 772, 157, 48), confidence=0.9)
        
        if gold2 is not None:
            print("i see gold2")
            
            pt.click(gold2)
            print("clickt gold 2") 
            
        else:
            print("    i NOT see gold2")
            
            # check for gold 1
            ##############################################################################################
            
            # screenshot gold1
            ImageGrab.grab().save("C:/Users/mikey/Desktop/Visual Studio Files/Mikey/donation/screenshot/gold1.png")
            ImageGrab.grab(bbox=(1055, 771, 1209, 819)).save("C:/Users/mikey/Desktop/Visual Studio Files/Mikey/donation/screenshot/gold1_region.png")
            
            # search for refresh
            gold1= pt.locateCenterOnScreen("imgs/gold1.png", grayscale=False, region=(1055, 771, 155, 48), confidence=0.9)
            
            if gold1 is not None:
                print("i see gold1")
        
                pt.click(gold1)
                print("clickt gold 1") 
                
            else:
                print("    i NOT see gold1")
                        
                # click on green
                pt.moveTo(1228, 696)
                sleep(0.2)
                pt.click()
                print("clickt green") 
                
                pt.moveTo(1064, 685)
                sleep(0.1)
        
                
        
        
        
        
    
    
    
    
    