# minecraft-vision-bot/main.py

from vision.screen_capture import ScreenCapture
from vision.block_detector import detect_environment
from ai.rule_based import decide_action
from actions.movement import move_forward, stop, jump, sprint_forward, jump_forward
from config import SCAN_INTERVAL
import time

def main():
    screen = ScreenCapture()
    print("[INFO] Starting Minecraft AI Bot - Phase 2")

    try:
        while True:
            frame = screen.grab_screen()
            env = detect_environment(frame)
            action = decide_action(env)

            if action == "sprint_forward":
                sprint_forward()
            elif action == "jump_forward":
                jump_forward()
            elif action == "jump":
                jump()
            elif action == "stop":
                stop()

            time.sleep(SCAN_INTERVAL)

    except KeyboardInterrupt:
        print("[INFO] Bot stopped by user.")
        stop()

if __name__ == '__main__':
    main()