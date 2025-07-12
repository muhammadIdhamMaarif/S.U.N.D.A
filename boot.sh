#!/bin/bash
# boot.sh
# Script startup untuk menjalankan sistem helm pintar saat boot

echo "Memulai sistem helm pintar AI..."

# Aktifkan virtual environment (jika ada)
# source /home/pi/venv/bin/activate

# Jalankan semua service dalam background

echo "Menjalankan sistem utama..."
python3 core/main.py &

# Jalankan WebSocket server (opsional jika tidak digabung ke FastAPI)
# echo "Menjalankan WebSocket server..."
# python3 mobile_interface/websocket_handler.py &

# Tambahkan log sistem
echo "$(date) - Smart Helmet System Started" >> /home/pi/helmet_system.log
