import pyautogui
import time
import os
import keyboard

# Set the current working directory to the script's directory
script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)

print(f"Current working directory: {os.getcwd()}")

def LocateAndClickButton(locateImage, withinRegion=None):
    try:
        currentMousePos = pyautogui.position()
        location = pyautogui.locateCenterOnScreen(locateImage, region=withinRegion)
        if location is not None:
            pyautogui.click(location)
            print(f"Clicked on the button at {location}.")
            time.sleep(0.2)

            # Restore mouse position
            pyautogui.moveTo(currentMousePos)

            return True
        else:
            print("Button not found on the screen.")
        
    except Exception as e:
        print(f"Warning: {str(e)} with current mouse pos {currentMousePos}")
    
    return False

try:
    while True:
        if keyboard.is_pressed('esc'):
            print("\nScript terminated by user.")
            break

        region = None
        #region = (500, 600, 1000, 400) # Too slow? Uncomment this to look for the buttons from mouse pos x 500 y 600 in a rectangular region of width 1000 and height 400
        
        res = LocateAndClickButton(locateImage='autoclick_target.png', withinRegion=region)
        if not res: 
            LocateAndClickButton(locateImage='autoclick_target_2.png', withinRegion=region)
        time.sleep(0.5)

except KeyboardInterrupt:
    print("\nScript terminated by user.")
