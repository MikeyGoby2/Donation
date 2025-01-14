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
##############################################################################################

    
print("#### WHILE DONATION ####")
print("")
print("START donation")

def click_element(image_path, region, click_delay=0.2, confidence=0.9):
    element = pt.locateCenterOnScreen(image_path, grayscale=False, region=region, confidence=confidence)
    if element is not None:
        print(f"Found {image_path}")
        pt.moveTo(element)
        sleep(click_delay)
        pt.click()
        return True
    return False

# Main loop
while not keyboard.is_pressed('q'):
    
    sleep(0.5)
    
    # Check for refresh
    refresh_region = (928, 675, 59, 20)
    if click_element("imgs/refresh.png", refresh_region):
        print("Clicked refresh")
        
        sleep(0.2)
        
        # Check for gold 2
        no_gold_region = (915, 684, 90, 21)
        if click_element("imgs/no_more_gold.png", no_gold_region):
            print("    no more gold")
            sleep(0.4)
            
            # click screen away
            pt.press("esc")
            sleep(0.2)
            pt.press("esc")
            
            print("    EXIT script")
            exit()
            
        else:
            print("Did not find no more gold")
        
    else:
        print("Did not find refresh")
    
        # Check for gold 2
        gold2_region = (1247, 772, 157, 48)
        if click_element("imgs/gold2.png", gold2_region):
            print("Clicked gold 2")
            sleep(0.4)
        else:
            print("Did not find gold 2")
            
            # Check for gold 1
            gold1_region = (1055, 771, 155, 48)
            if click_element("imgs/gold1.png", gold1_region):
                print("Clicked gold 1")
                sleep(0.4)
            else:
                print("Did not find gold 1")
                
                # Click on green
                pt.moveTo(1228, 696)
                sleep(0.2)
                pt.click()
                print("Clicked green")

