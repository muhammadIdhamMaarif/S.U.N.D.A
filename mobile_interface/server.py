# mobile_interface/server.py
# Server REST API untuk mengontrol HUD & fitur helm dari smartphone

from fastapi import FastAPI, Request
from pydantic import BaseModel
from core.logger import log
from core.config import API_PORT
import uvicorn

from mobile_interface.layout_config import apply_layout_config

app = FastAPI()

# Data model JSON yang dikirim dari HP
class LayoutConfig(BaseModel):
    layout_name: str
    show_clock: bool
    show_music: bool
    show_notifications: bool
    theme: str  # dark / light

@app.post("/set_layout")
async def set_layout(config: LayoutConfig):
    log("API", f"Received layout config: {config.layout_name}")
    apply_layout_config(config.dict())
    return {"status": "ok", "message": "Layout updated"}

@app.get("/get_status")
async def get_status():
    return {
        "battery": "85%",
        "wifi": "Connected",
        "gps": "Active",
        "lidar": "No obstacle",
        "cam": "Recording"
    }

@app.post("/toggle_feature")
async def toggle_feature(req: Request):
    data = await req.json()
    feature = data.get("feature")
    status = data.get("status")
    log("API", f"Toggle {feature} → {'ON' if status else 'OFF'}")
    return {"status": "ok", "feature": feature, "enabled": status}

def run_api_server():
    uvicorn.run(app, host="0.0.0.0", port=API_PORT)
