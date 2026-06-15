# VoiceNote - FastAPI WebSocket Chat with Audio Support

VoiceNote is a simple chat application built with FastAPI that supports both text and audio messages. It uses WebSockets for real-time communication and provides a seamless way to exchange voice notes and text messages in real-time.

## Requirements

To run this project, you need the following:

- **Python 3.8+**
- **FastAPI** and related dependencies (see [Installation](#installation) below)

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/ctaljaard/VoiceNote.git
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

### 4. Open the Application

Visit `http://localhost:8000` in your browser to use the chat application. You can open multiple tabs or windows to chat between different users.

## Features

- **Real-time Text Chat**: Send and receive messages instantly via WebSocket
- **Audio Support**: Record and share audio messages with other users
- **Multi-user Chat**: Multiple users can join the same chat room
- **Dynamic WebSocket Connection**: Automatically connects to the current server without configuration

## Notes

- **Audio Uploads**: Uploaded audio files are saved in the `static` directory
- **Development**: The application is suitable for local development and testing
- **Production**: For production deployment, ensure proper CORS configuration, authentication, and security measures are implemented

## Project Structure

```
VoiceNote/
├── audio.py          # Handles audio file saving and URL generation
├── index.html        # Frontend HTML file
├── server.py         # FastAPI backend server
├── static/           # Directory for uploaded audio files
└── README.md         # Project documentation
```

## Security Considerations

This is a development project. Before deploying to production, consider implementing:

- User authentication and authorization
- Input validation and sanitization
- File upload restrictions (type and size limits)
- Rate limiting
- CORS configuration
- HTTPS/WSS enforcement

## License

This project is licensed under the MIT License. See the LICENSE file for details.
