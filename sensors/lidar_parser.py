# sensors/lidar_parser.py
# Membaca data LiDAR untuk mendeteksi blind spot atau obstacle

from core.logger import log
import time


def start_lidar():
    log("LIDAR", "Inisialisasi sensor LiDAR...")

    while True:
        # Simulasi deteksi objek
        # Replace dengan pembacaan real dari sensor (pyLidar3 / RPLIDAR SDK)
        distance = 1.2  # dalam meter
        angle = 45  # derajat
        if distance < 2.0:
            log("LIDAR", f"Obstacle detected! {distance} m at {angle}°")
        time.sleep(1)
