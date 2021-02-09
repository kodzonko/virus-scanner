class ApiFile:

    def __init__(self, path: str = 'API-key.txt'):
        try:
            with open(path, 'r') as file:
                self.__api_key = file.read().strip('\n')
        except OSError:
            pass
