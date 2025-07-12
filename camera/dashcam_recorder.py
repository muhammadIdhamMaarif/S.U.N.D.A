# camera/dashcam_recorder.py
# Merekam video dalam loop menggunakan ffmpeg atau opencv-python

import os
import time
import subprocess
from core.logger import log
from core.config import VIDEO_DIR

def start_recorder():
    os.makedirs(VIDEO_DIR, exist_ok=True)
    log("CAM", "Starting dashcam recording...")

    while True:
        filename = time.strftime("%Y-%m-%d_%H-%M-%S") + ".mp4"
        filepath = os.path.join(VIDEO_DIR, filename)

        cmd = [
            "ffmpeg",
            "-f", "v4l2",
            "-i", "/dev/video0",
            "-t", "00:03:00",  # rekam 3 menit
            "-vcodec", "libx264",
            "-preset", "ultrafast",
            filepath
        ]

        log("CAM", f"Recording: {filename}")
        subprocess.run(cmd)

        cleanup_old_videos(max_files=20)

def cleanup_old_videos(max_files=20):
    files = sorted(os.listdir(VIDEO_DIR))
    while len(files) > max_files:
        oldest = files.pop(0)
        os.remove(os.path.join(VIDEO_DIR, oldest))
        log("CAM", f"Deleted old video: {oldest}")
