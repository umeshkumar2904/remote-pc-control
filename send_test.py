import asyncio
import websockets
import json

async def send():
    uri = "ws://127.0.0.1:8000/ws/send/MY_LAPTOP"
    async with websockets.connect(uri) as ws:
        await ws.send(json.dumps({
            "action": "open_url",
            "value": "https://youtube.com"
        }))
        response = await ws.recv()
        print(response)

asyncio.run(send())
