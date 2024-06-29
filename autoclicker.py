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
        location = pyautogui.locateCenterOnScreen(locateImage, region=withinRegion)
        if location is not None:
            currentMousePos = pyautogui.position()
            pyautogui.click(location)
            print(f"Clicked on the button at {location}.")
            time.sleep(0.2)

            # Restore mouse position
            pyautogui.moveTo(currentMousePos)

            return True
        else:
            print("Button not found on the screen.")
        
    except Exception as e:
        print(f"Warning: {str(e)}")
    
    return False

try:
    while True:
        if keyboard.is_pressed('esc'):
            print("\nScript terminated by user.")
            break

        res = LocateAndClickButton(locateImage='autoclick_target.png', withinRegion=(700,700,500,500))
        if not res: 
            LocateAndClickButton(locateImage='autoclick_target_2.png', withinRegion=(700,700,500,500))
        time.sleep(0.5)

except KeyboardInterrupt:
    print("\nScript terminated by user.")
