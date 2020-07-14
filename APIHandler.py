class APIHandler:

    def __init__(self):
        self.API_key = None

    def get_API_from_file(self, path: str):
        with open('api_key.txt', 'r') as file:
            self.API_key = file.read()

    def get_API_from_user(self):
        api = input('Paste your VirusTotal API key: ')
        self.API_key = api.strip('\n\t,.')

        # if platform.system() == 'Windows':
        #
        # elif platform.system() == 'Linux':
        #
        # elif platform.system() == 'Darwin':
        #
        # else:
        #
        store_API = input('Do you want to store your API key in file for further scans [yes|no]: ')
        if store_API.lower() == 'yes' or store_API.lower() == 'y':
            with open('api_key.txt', 'a') as file:
                try:
                    file.write(api)
                except IOError:
                    print('Unable to create file in that location. Try again.')
                    self.get_API_from_user(api)
                else:
                    file.write(api)
