import mss
import numpy as np
import cv2
from config import SCREEN_REGION

class ScreenCapture:
    def __init__(self):
        self.sct = mss.mss()
        self.monitor = SCREEN_REGION

    def grab_screen(self):
        screenshot = np.array(self.sct.grab(self.monitor))
        frame = cv2.cvtColor(screenshot, cv2.COLOR_BGRA2BGR)
        return frame
