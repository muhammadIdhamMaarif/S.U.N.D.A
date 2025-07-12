# camera/overlay_timestamp.py
# Tambahkan watermark timestamp menggunakan ffmpeg

import subprocess

def add_timestamp(input_file, output_file):
    cmd = [
        "ffmpeg",
        "-i", input_file,
        "-vf", "drawtext=text='%{localtime}':fontsize=20:fontcolor=white:x=10:y=10",
        "-codec:a", "copy",
        output_file
    ]
    subprocess.run(cmd)
