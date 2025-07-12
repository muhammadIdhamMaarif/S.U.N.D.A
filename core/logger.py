# core/logger.py
# Logger sederhana untuk debugging sistem

import datetime

def log(tag, message):
    time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{tag}] {time} - {message}")
