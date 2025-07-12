# sensors/gps_reader.py
# Membaca data dari modul GPS (NEO-6M/NEO-M8N)

import serial
import pynmea2
from core.logger import log
from core.config import GPS_PORT

def read_gps():
    with serial.Serial(GPS_PORT, baudrate=9600, timeout=1) as ser:
        while True:
            try:
                line = ser.readline().decode('utf-8', errors='ignore')
                if line.startswith('$GPGGA'):
                    msg = pynmea2.parse(line)
                    log("GPS", f"Lat: {msg.latitude}, Lon: {msg.longitude}")
            except Exception as e:
                log("GPS", f"Error: {e}")
