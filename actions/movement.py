import pyautogui
import time
from config import MOVE_DURATION
from utils.image_utils import log_action

def sprint_forward():
    log_action("Sprinting Forward")
    pyautogui.press('w')        # Double tap
    time.sleep(0.05)
    pyautogui.press('w')
    pyautogui.keyDown('w')
    time.sleep(MOVE_DURATION)
    pyautogui.keyUp('w')

def jump_forward():
    log_action("Jumping While Moving Forward")
    pyautogui.keyDown('w')
    pyautogui.press('space')
    time.sleep(0.2)
    pyautogui.keyUp('w')

def move_forward():
    log_action("Moving Forward")
    pyautogui.keyDown('w')
    time.sleep(MOVE_DURATION)
    pyautogui.keyUp('w')

def stop():
    log_action("Stopping")
    pyautogui.keyUp('w')

def jump():
    log_action("Jumping")
    pyautogui.press('space')
