# sensors/battery_monitor.py
# Membaca status baterai dari ESP32 melalui komunikasi serial

import serial
from core.config import ESP32_SERIAL_PORT
from core.logger import log

def monitor_battery():
    try:
        ser = serial.Serial(ESP32_SERIAL_PORT, 115200)
        while True:
            line = ser.readline().decode().strip()
            if line.startswith("BAT:"):
                percent = line.replace("BAT:", "")
                log("BATTERY", f"{percent}% remaining")
    except Exception as e:
        log("BATTERY", f"Serial error: {e}")
