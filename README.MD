# AutoClicker Script

This Python script automates the process of clicking on specific buttons on the screen at regular intervals. It uses image recognition to locate the buttons and performs a mouse click on them. After clicking, it restores the mouse to its previous position, allowing you to continue working while the script runs. The script also supports termination by pressing the `Esc` key.

## Requirements

- Python 3.6+
- [`pyautogui`](https://pypi.org/project/pyautogui/)
- [`pillow`](https://pypi.org/project/Pillow/)
- [`keyboard`](https://pypi.org/project/keyboard/)

## Installation

1. Clone the repository or download the script.
2. Install the required Python packages:

    ```bash
    pip install pyautogui pillow keyboard
    ```

## Usage

1. **Prepare the Images**:
   - Capture images of the buttons you want the script to click on (e.g., `autoclick_target.png` and `autoclick_target_2.png`).
   - Place these images in the same directory as the script.

2. **Run the Script**:
   - Execute the script from the terminal or command prompt:

     ```bash
     python autoclicker.py
     ```

3. **Script Behavior**:
   - The script will search for the specified images on the screen continously.
   - If the button is found, it will click it and restore the mouse position.
   - Press `Esc` to stop the script or use `Ctrl+C` in the terminal.

## Parameters

  - `locateImage`: Path to the image of the button.
  - `withinRegion` (optional): x,y,width,height region of the screen to search within for faster / more efficient targeting (default is the whole screen).

```python
def LocateAndClickButton(locateImage, withinRegion=None):
    ...
