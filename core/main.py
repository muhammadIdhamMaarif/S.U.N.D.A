# core/main.py
# Entry point utama yang menginisialisasi semua service helm pintar

from hud.hud_renderer import start_hud
from sensors.lidar_parser import start_lidar
from voice_assistant.assistant_engine import start_assistant
from camera.dashcam_recorder import start_recorder
from connectivity.wifi_manager import ensure_connection
from mobile_interface.server import run_api_server

import threading
import time

def main():
    print("[SYSTEM] Starting Smart Helmet System...")

    # Jalankan HUD Display
    threading.Thread(target=start_hud, daemon=True).start()

    # Jalankan LiDAR untuk deteksi blind spot
    threading.Thread(target=start_lidar, daemon=True).start()

    # Jalankan Asisten Suara
    threading.Thread(target=start_assistant, daemon=True).start()

    # Jalankan Kamera Dashcam
    threading.Thread(target=start_recorder, daemon=True).start()

    # Pastikan Wi-Fi tersambung atau jadi AP
    ensure_connection()

    # Jalankan API Server untuk integrasi HP
    run_api_server()

    while True:
        time.sleep(1)

if __name__ == "__main__":
    main()
