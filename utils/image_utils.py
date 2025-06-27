from datetime import datetime
from config import LOG_FILE

def log_action(message):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log = f"[{timestamp}] {message}"
    print(log)
    with open(LOG_FILE, 'a') as f:
        f.write(log + "\n")
