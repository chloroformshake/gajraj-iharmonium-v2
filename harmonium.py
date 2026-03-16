import asyncio
import json
import threading
from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler

import websockets
from pybooklid import LidSensor

async def handler(websocket):
    print("\nWeb App connected!")
    with LidSensor() as sensor:
        for angle in sensor.monitor(interval=0.05):
            print(f"\rCurrent Lid Angle: {angle:.2f}°   ", end="", flush=True)
            
            try:
                await websocket.send(json.dumps({"angle": angle}))
            except websockets.ConnectionClosed:
                print("\nWeb App disconnected.")
                break

async def main():
    async with websockets.serve(handler, "localhost", 8765):
        print("Bridge active! Waiting for your web app on port 8765...")
        await asyncio.Future()

if __name__ == "__main__":
    try:
        httpd = ThreadingHTTPServer(("localhost", 8000), SimpleHTTPRequestHandler)
        http_thread = threading.Thread(target=httpd.serve_forever, daemon=True)
        http_thread.start()
        print("Serving web UI on http://localhost:8000/harmonium.html")
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\nStopping Bridge...")
    finally:
        try:
            httpd.shutdown()
        except Exception:
            pass
