# camera/imu_trigger.py
# Menyimpan video penting saat tabrakan terdeteksi (butuh buffer + flag)

from sensors.imu_handler import check_impact
from core.logger import log
import time

def monitor_impact():
    while True:
        if check_impact():
            log("CAM", "Impact detected! Marking critical clip.")
            save_critical_event()
        time.sleep(0.2)

def save_critical_event():
    # Simulasikan logika penyimpanan pre/post-event
    log("CAM", "Saving 10s before and after impact (simulasi)")
