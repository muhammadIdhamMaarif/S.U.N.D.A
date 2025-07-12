# test/test_imu.py
import time
import random
from core.logger import log

def simulate_imu():
    print("Simulasi sensor IMU (impact detection)...")
    while True:
        g_force = random.uniform(0, 10)
        if g_force > 6.0:
            log("IMU", f"Impact detected! G-force: {g_force:.2f}g")
        else:
            log("IMU", f"Normal movement: {g_force:.2f}g")
        time.sleep(1)

if __name__ == "__main__":
    simulate_imu()
