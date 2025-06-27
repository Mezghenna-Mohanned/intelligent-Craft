import cv2
import numpy as np
from config import GREEN_THRESHOLD, RED_THRESHOLD, BLUE_THRESHOLD, BROWN_THRESHOLD, BLOCK_THRESHOLD
from utils.image_utils import log_action

def detect_environment(frame):
    env = {}

    green_mask = cv2.inRange(frame, (25, 40, 20), (90, 255, 90))
    env["grass"] = cv2.countNonZero(green_mask)

    brown_mask = cv2.inRange(frame, (50, 25, 0), (120, 80, 40))
    env["tree"] = cv2.countNonZero(brown_mask)

    red_mask = cv2.inRange(frame, (0, 0, 100), (70, 70, 255))
    env["lava"] = cv2.countNonZero(red_mask)

    blue_mask = cv2.inRange(frame, (0, 0, 100), (100, 100, 255))
    env["water"] = cv2.countNonZero(blue_mask)

    # Obstacle: general blocks
    gray_mask = cv2.inRange(frame, (90, 90, 90), (140, 140, 140))
    env["block"] = cv2.countNonZero(gray_mask)

    log_action(f"ENV: {env}")
    return env
