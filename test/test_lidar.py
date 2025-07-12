# test/test_lidar.py
import time
import random
from core.logger import log

def simulate_lidar():
    print("Simulasi sensor LiDAR (blind spot detection)...")
    while True:
        distance = random.uniform(0.1, 5.0)  # jarak meter
        angle = random.randint(0, 359)
        if distance < 2.0:
            log("LIDAR", f"Obstacle detected at {distance:.2f}m angle {angle}°")
        else:
            log("LIDAR", f"No obstacle nearby (distance: {distance:.2f}m)")
        time.sleep(1)

if __name__ == "__main__":
    simulate_lidar()
