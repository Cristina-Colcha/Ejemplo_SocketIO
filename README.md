# Socket.IO Real Time Chat
This project is a real-time chat application based on **Socket.IO**, using **Flask** for the backend and **HTML/JavaScript** for the frontend. 
---
## Features
- Real-time communication between client and server.
- Support for multiple connected users.
- Automatic chat update for all connected clients.
- Based on modern technologies such as **WebSockets** and **Socket.IO**.

## Technologies Used
- **Python** with **Flask** and **Flask-SocketIO**.
- **Socket.IO** for real-time bidirectional communication.
- **HTML** and **JavaScript** for the frontend.

## 📂 Project Structure.
    ├── server.py # # Flask server with Socket.IO integration.
    ├─── templates/
    │ └└─── index.html # Client interface (frontend).
    └└─── README.md # Project documentation.
📋 Requirements.
Python 3.8+
Pip to install dependencies
⚙️ Installation
Follow the steps below to run this project on your local machine:
### Clone this repository:
https://github.com/Cristina-Colcha/Ejemplo_SocketIO.git 
cd socketio-chat
### Install the dependencies:
pip install flask flask-socketio
Run the server:
python server.py
Open your browser and access to:
http://localhost:5000
### How it works
Client-Server Connection:
When the client accesses the server URL, a WebSocket connection is established using the Socket.IO library.
Message Exchange:
The client sends messages to the server, and the server relays them to all connected clients.
Real-Time Update:
Messages are dynamically updated on the page without the need to reload the page.
### Author
Created by Tu Cristina Colcha
