from datetime import datetime
from config import LOG_FILE

def log_action(message):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"[{timestamp}] {message}\n"
    print(log_entry.strip())

    with open(LOG_FILE, 'a') as file:
        file.write(log_entry)
