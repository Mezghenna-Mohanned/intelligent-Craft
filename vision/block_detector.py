import cv2
import numpy as np
from config import GREEN_THRESHOLD
from utils.image_utils import log_action

def is_grass_detected(frame):
    """Detect large amounts of green pixels (grass) for now brk"""
    lower_green = np.array([25, 40, 20])
    upper_green = np.array([90, 255, 90])

    mask = cv2.inRange(frame, lower_green, upper_green)
    green_pixels = cv2.countNonZero(mask)

    log_action(f"Green pixels detected: {green_pixels}")

    return green_pixels > GREEN_THRESHOLD
