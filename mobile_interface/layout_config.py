# mobile_interface/layout_config.py
# Menyimpan konfigurasi layout HUD dari HP dalam file JSON

import json
from core.logger import log
from core.config import HUD_LAYOUT_FILE
import os

def apply_layout_config(layout: dict):
    os.makedirs(os.path.dirname(HUD_LAYOUT_FILE), exist_ok=True)
    with open(HUD_LAYOUT_FILE, "w") as f:
        json.dump(layout, f, indent=4)
    log("LAYOUT", "Layout HUD diperbarui")
