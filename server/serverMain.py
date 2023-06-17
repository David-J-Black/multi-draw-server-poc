from flask import Flask, render_template
from flask_socketio import SocketIO

app = Flask(__name__)
app.config['SECRET_KEY'] = 'sixtyNine'
socketio = SocketIO(app, cors_allowed_origins="*")

# So when that socket IO object we declared above recieves a message, it will execute the below function, thanks to that @ annotation
@socketio.on('message')
def handle_message(data):
    print('recieved message: ' + data)
    socketio.emit('response', 'Who\'s there?')

if __name__ == '__main__':
    socketio.run(app, debug=True)
