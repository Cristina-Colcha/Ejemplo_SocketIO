import webbrowser
from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

# Ruta principal para servir el cliente
@app.route('/')
def index():
    return render_template('index.html')  # Asegúrate de tener este archivo en una carpeta 'templates'

# Evento para manejar mensajes del cliente
@socketio.on('message')
def handle_message(data):
    print(f"Mensaje recibido: {data}")
    emit('response', f"Servidor recibió: {data}", broadcast=True)

# Iniciar el servidor
if __name__ == '__main__':
    # Abre automáticamente el navegador en la URL local
    webbrowser.open('http://localhost:5000')

    # Inicia el servidor Flask
    socketio.run(app, debug=True)
