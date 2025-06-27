from vision.screen_capture import ScreenCapture
from vision.block_detector import is_grass_detected
from ai.rule_based import decide_action
from actions.movement import move_forward, stop
from config import SCAN_INTERVAL
import time

def main():
    screen = ScreenCapture()
    print("Starting Minecraft AI Bot... Press Ctrl+C to stop.")

    try:
        while True:
            frame = screen.grab_screen()
            grass_detected = is_grass_detected(frame)
            action = decide_action(grass_detected)

            if action == "move_forward":
                move_forward()
            elif action == "stop":
                stop()

            time.sleep(SCAN_INTERVAL)

    except KeyboardInterrupt:
        print("Bot stopped.")

if __name__ == "__main__":
    main()
