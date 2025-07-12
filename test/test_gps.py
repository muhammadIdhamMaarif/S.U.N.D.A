# test/test_gps.py
import time
import random
from core.logger import log

def simulate_gps():
    print("Simulasi GPS data...")
    while True:
        lat = random.uniform(-6.3, -6.1)
        lon = random.uniform(106.7, 106.9)
        log("GPS", f"Simulated GPS Lat: {lat:.6f}, Lon: {lon:.6f}")
        time.sleep(2)

if __name__ == "__main__":
    simulate_gps()
