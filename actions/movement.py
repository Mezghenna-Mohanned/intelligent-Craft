import pyautogui
import time
from config import MOVE_DURATION
from utils.image_utils import log_action

def move_forward():
    log_action("Moving Forward")
    pyautogui.keyDown('w')
    time.sleep(MOVE_DURATION)
    pyautogui.keyUp('w')

def stop():
    log_action("Stopping")
    pyautogui.keyUp('w')
