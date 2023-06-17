import socketio

# Creating the object we will use to talk to server
socketClient = socketio.Client()

# I should do some research, but I think this annotation (The bit with the @ in front of it) tells Python/socketio library that this function plugs into the socketClient
@socketClient.event
def connect():
    print('I\'m connected motherfucker!')
    socketClient.emit('message', "Knock knock")

@socketClient.event
def disconnect():
    print(f'OOPS! I disconnected!')


@socketClient.on('response')
def onResponse(data):
    print(f'We got a response: {data}')


# I'm not going to write a main() function, let's just fuckin do it like this for simplicity's sake
socketClient.connect('http://127.0.0.1:5000')
socketClient.wait
