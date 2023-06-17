import yaml
import os
from service import ConnectionService, CanvasService

# This is us saving where clientMain.py is currently located.
# - When we load files, python is nitpicky about it's current directory, so i have to be specific
current_directory_location = os.path.dirname(os.path.realpath(__file__))

class Core():
    """
    The main program Class
    """

    # This will hold the config we retrieve from the yaml. It will be a dictionary.
    config = ''

    connectionService = None
    canvasService = None

    def __init__(self):

        # Let's get the configuration from the client-config.yml
        with open(f'{current_directory_location}/client-config.yml', 'r') as file:
            try:
                config = yaml.safe_load(file)
                print(f'Loaded config: {config}')
            except yaml.YAMLError as exception:
                print(exception)

        self.connectionService = ConnectionService(config)
        # When we create the canvasService, we give it the close function that ends the program
        self.canvasService = CanvasService(self.close)
   
    def close(self):
        self.connectionService.disconnect()
        exit()

# start the app by running main
if __name__ == '__main__':
    core = Core()