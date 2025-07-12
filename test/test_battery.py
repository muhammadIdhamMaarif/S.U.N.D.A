# test/test_battery.py
import time
from core.logger import log

def simulate_battery():
    print("Simulasi status baterai...")
    percent = 100
    while percent > 0:
        log("BATTERY", f"{percent}% remaining")
        percent -= 1
        time.sleep(3)

if __name__ == "__main__":
    simulate_battery()
