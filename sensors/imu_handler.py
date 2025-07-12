# sensors/imu_handler.py
# Deteksi crash/jatuh menggunakan data dari IMU (MPU6050 atau BNO055)

import random
import time
from core.logger import log

def check_impact():
    # Simulasi g-force tiba-tiba (real: gunakan smbus2/i2cdev dengan IMU)
    g_force = random.uniform(0, 10)
    if g_force > 6.0:
        log("IMU", f"Impact detected! G-force: {g_force:.2f}g")
        return True
    return False

def monitor_imu():
    log("IMU", "Monitoring gerakan helm...")
    while True:
        check_impact()
        time.sleep(0.5)
