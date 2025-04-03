from fastapi import FastAPI, WebSocket, WebSocketDisconnect, UploadFile, File
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
import json
from audio import save_audio_file, get_audio_url

app = FastAPI()

AUDIO_DIR = "static"
app.mount("/static", StaticFiles(directory=AUDIO_DIR), name="static")

connections = {}

@app.get("/", response_class=HTMLResponse)
def serve_home():
    with open("index.html", "r") as file:
        content = file.read()
    return HTMLResponse(content.replace("{name}", "Home"))

@app.get("/{name}", response_class=HTMLResponse)
def get_name_page(name: str):
    with open("index.html", "r") as file:
        content = file.read()
    capitalized_name = name.capitalize()
    return HTMLResponse(content.replace("{name}", capitalized_name))

@app.websocket("/ws/{name}")
async def websocket_endpoint(websocket: WebSocket, name: str):
    capitalized_name = name.capitalize()
    await websocket.accept()
    connections[capitalized_name] = websocket
    try:
        while True:
            data = await websocket.receive_text()
            message = json.loads(data)
            for conn in connections.values():
                await conn.send_text(json.dumps({
                    "name": capitalized_name,
                    "message": message["message"],
                    "type": message["type"]
                }))
    except WebSocketDisconnect:
        del connections[capitalized_name]

@app.post("/upload_audio/")
async def upload_audio(file: UploadFile = File(...)):
    filename = save_audio_file(file)
    audio_url = get_audio_url(filename)
    return {"audio_url": audio_url}
