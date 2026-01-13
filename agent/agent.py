import asyncio
import websockets
import os
import json
import webbrowser

DEVICE_ID = "MY_LAPTOP"

async def listen():
    uri = f"ws://127.0.0.1:8000/ws/laptop/{DEVICE_ID}"

    async with websockets.connect(uri) as websocket:
        print("Laptop connected to server")

        while True:
            message = await websocket.recv()
            data = json.loads(message)

            if data["action"] == "shutdown":
                os.system("shutdown /s /t 1")

            elif data["action"] == "restart":
                os.system("shutdown /r /t 1")

            elif data["action"] == "open_url":
                webbrowser.open(data["value"])

asyncio.run(listen())
