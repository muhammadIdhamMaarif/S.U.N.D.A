# mobile_interface/websocket_handler.py
# WebSocket server untuk sinkronisasi status secara real-time

import asyncio
import websockets
import json
from core.logger import log

clients = set()

async def handler(websocket, path):
    log("WS", "Client connected")
    clients.add(websocket)
    try:
        while True:
            status = {
                "battery": "83%",
                "speed": "48 km/h",
                "gps": {"lat": -6.2, "lon": 106.8},
            }
            await websocket.send(json.dumps(status))
            await asyncio.sleep(2)
    except websockets.exceptions.ConnectionClosed:
        log("WS", "Client disconnected")
    finally:
        clients.remove(websocket)

def run_websocket_server():
    start_server = websockets.serve(handler, "0.0.0.0", 6789)
    asyncio.get_event_loop().run_until_complete(start_server)
    asyncio.get_event_loop().run_forever()
