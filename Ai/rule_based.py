from config import GREEN_THRESHOLD, RED_THRESHOLD, BLUE_THRESHOLD, BROWN_THRESHOLD, BLOCK_THRESHOLD
from utils.image_utils import log_action

def decide_action(env):
    if env["lava"] > RED_THRESHOLD:
        log_action("Decision: STOP (Lava)")
        return "stop"
    
    elif env["water"] > BLUE_THRESHOLD:
        log_action("Decision: STOP (Water)")
        return "stop"
    
    elif env["tree"] > BROWN_THRESHOLD:
        log_action("Decision: STOP (Tree ahead)")
        return "stop"
    
    elif env["block"] > BLOCK_THRESHOLD:
        log_action("Decision: JUMP FORWARD (Block)")
        return "jump_forward"
    
    elif env["grass"] > GREEN_THRESHOLD:
        log_action("Decision: SPRINT FORWARD")
        return "sprint_forward"
    
    else:
        log_action("Decision: STOP (Unknown environment)")
        return "stop"
