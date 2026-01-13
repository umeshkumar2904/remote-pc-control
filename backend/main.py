from fastapi import FastAPI, WebSocket, WebSocketDisconnect

app = FastAPI()

connected_laptops = {}

@app.get("/")
def home():
    return {"status": "Backend running with WebSockets"}

@app.websocket("/ws/laptop/{device_id}")
async def laptop_ws(websocket: WebSocket, device_id: str):
    await websocket.accept()
    connected_laptops[device_id] = websocket
    print(f"Laptop connected: {device_id}")

    try:
        while True:
            await websocket.receive_text()
    except WebSocketDisconnect:
        del connected_laptops[device_id]
        print(f"Laptop disconnected: {device_id}")

@app.websocket("/ws/send/{device_id}")
async def send_command(websocket: WebSocket, device_id: str):
    await websocket.accept()
    data = await websocket.receive_text()

    if device_id in connected_laptops:
        await connected_laptops[device_id].send_text(data)
        await websocket.send_text("Command sent to laptop")
    else:
        await websocket.send_text("Laptop offline")
