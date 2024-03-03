import logging, json
from flask import Flask, render_template
from flask_socketio import SocketIO, emit
app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

socketio = SocketIO(app)

@socketio.on('connect')
def handle_connect():
    logging.info('Client connected')

@socketio.on('disconnect')
def handle_disconnect():
    logging.info('Client disconnected')

@socketio.on('message')
def handle_message(data):
    logging.info('Received message: %s', data)
    start_time = data.get('start_time')
    end_time = data.get('end_time')
    narfcn = data.get('narfcn')
    pci = data.get('pci')
    band = data.get('band')

    # Call the parse function with the received parameters
    result = parse(start_time, end_time, narfcn, pci, band)

    # Convert the dictionary to JSON and send it back to the frontend
    emit('response', json.dumps(result))

def parse(start_time, end_time, narfcn=None, pci=None, band=None):
    # Your parse function implementation here
    # Return the dictionary structure
    return {
        'start_time': start_time,
        'end_time': end_time,
        'narfcn': narfcn,
        'pci': pci,
        'band': band
    }

if __name__ == '__main__':
    host = '127.0.0.1' if app.debug else '172.17.14.52'
    port = 8787
    socketio.run(app, host=host, port=port)