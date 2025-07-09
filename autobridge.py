#autobridge v0.1
#I tried to use ChatGPT but it was being a dumbo
import pyautogui
from pynput import keyboard, mouse
import threading
import time

# Settings
# The parameters have been tuned; please don't adjust them randomly!
backward_interval = 0.162 # walk delay
shift_interval = 0.08 # shift delay
hold_dot = keyboard.KeyCode(char='`') # hold down '`' to bridge
button = mouse.Button.right # right mouse button

# States
mouse_controller = mouse.Controller()
holding_dot = False

def bridge():
    while True:
        if holding_dot:
            pyautogui.keyDown('shift')
            pyautogui.keyDown('s')
            time.sleep(shift_interval)
            mouse_controller.click(button)
            pyautogui.keyUp('shift')
            time.sleep(backward_interval)
        else:
            time.sleep(0.01)

def on_press(key):
    global holding_dot
    if key == hold_dot:
        holding_dot = True        
        print("Holding Key!")

def on_release(key):
    global holding_dot
    if key == hold_dot:
        holding_dot = False
        pyautogui.keyUp('s')
        print("Key Released!")

# Start the threads
thread_bridge = threading.Thread(target=bridge)
thread_bridge.daemon = True
thread_bridge.start()

# Listen for key presses/releases
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()


    
            
