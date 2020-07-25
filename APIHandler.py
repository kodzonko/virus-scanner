from FileHandler import FileHandler


class APIHandler:
    __API_key = None

    @classmethod
    def get_API_from_file(cls):
        """
        Parses API stored in non-encprypted file on your computer and stores it in the class.
        :return:
        None
        """
        file = FileHandler.ask_for_path()
        with open('api_key.txt', 'r') as file:
            cls.__API_key = file.read()

    @classmethod
    def get_API_from_user(self):
        api = input('Paste your VirusTotal API key: ')
        self.__API_key = api.strip('\n\t,. ')
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

    @classmethod
    def get_API_key(cls):
        return cls.__API_key
