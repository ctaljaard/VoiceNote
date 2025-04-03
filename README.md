```markdown
# VoiceNote - FastAPI WebSocket Chat with Audio Support

VoiceNote is a simple chat application built with FastAPI that supports both text and audio messages. It uses WebSockets for real-time communication and provides a seamless way to exchange voice notes in a chat environment.

## Requirements

To run this project, you need the following:

- **Python 3.8+**
- **FastAPI** and related dependencies (see [Installation](#installation) below)
- **ngrok** to expose your localhost server to the internet

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/VoiceNote.git
cd VoiceNote
```

### 2. Install Dependencies

```bash
pip install fastapi uvicorn python-multipart
```

### 3. Start the FastAPI Server

Run the FastAPI server locally:

```bash
uvicorn server:app --reload
```

The server will start at `http://127.0.0.1:8000`.

### 4. Expose the Server Using ngrok

To allow external access to your WebSocket server, use ngrok. Follow these steps:

1. Sign up for an [ngrok account](https://ngrok.com/).
2. Install ngrok on your system.
3. Authenticate ngrok with your account:

```bash
ngrok authtoken YOUR_AUTH_TOKEN
```

4. Start ngrok to expose your localhost server:

```bash
ngrok http 8000
```

This will generate a public URL (e.g., `https://your-ngrok-url.ngrok-free.app`).

### 5. Update the WebSocket URL in `index.html`

Replace the placeholder WebSocket URL in `index.html` with your ngrok URL. For example:

```javascript
const ws = new WebSocket(`wss://your-ngrok-url.ngrok-free.app/ws/${rawName}`);
```

### 6. Open the Application

Visit the ngrok URL in your browser (e.g., `https://your-ngrok-url.ngrok-free.app`) to use the chat application.

## Notes

- **ngrok Free Tier**: The free tier of ngrok generates a new URL each time you start it. You will need to update the WebSocket URL in `index.html` every time you restart ngrok.
- **Audio Uploads**: Uploaded audio files are saved in the `static` directory.

## Project Structure

```
VoiceNote/
├── audio.py          # Handles audio file saving and URL generation
├── index.html        # Frontend HTML file
├── server.py         # FastAPI backend server
├── static/           # Directory for uploaded audio files
└── README.md         # Project documentation
```

## License

This project is licensed under the MIT License. See the LICENSE file for details.
```

This version should now be properly formatted without issues, with all the instructions and details in a single markdown file.