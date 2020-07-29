from FileHandler import FileHandler


class APIHandler:
    __API_key = None

    @classmethod
    def get_API_from_file(cls):
        """
        Parses API stored in non-encrypted file on your computer and stores it in the class.
        :return:
        None
        """
        file = FileHandler.ask_for_path()
        with open(FileHandler.api_file, 'r') as file:
            cls.__API_key = file.read()

    @classmethod
    def get_API_from_user(cls):
        api = input('Paste your VirusTotal API key: ')
        cls.__API_key = api.strip('\n\t,. ')

    @classmethod
    def set_API_key(cls):
        return cls.__API_key

    @classmethod
    def get_API_key(cls):
        return cls.__API_key
