import socketio

class ConnectionService(socketio.Client):

    def __init__(self, config):
        super().__init__()
         # Get the server ip and port from the config.yml
        server_location = config['server']['location']

        # Connect our functions to the ones from socketio.Client
        self.on('connect', self.on_connect)
        self.on('disconnect', self.on_disconnect)
        self.on('response', self.on_response)

        print(f'Going to connect to server: {server_location}')
        self.connect(server_location)

    def on_connect(self):
        print('I\'m connected motherfucker!')
        self.emit('message', "Knock knock")

    def on_disconnect(self):
        print(f'OOPS! I disconnected!')

    def on_response(self, data):
        print(f'We got a response: {data}')
