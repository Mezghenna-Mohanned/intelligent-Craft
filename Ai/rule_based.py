from utils.image_utils import log_action

def decide_action(grass_detected):
    if grass_detected:
        log_action("Decision: Move Forward")
        return "move_forward"
    else:
        log_action("Decision: Stop")
        return "stop"
