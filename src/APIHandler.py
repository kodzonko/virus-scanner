from src.FileHandler import FileHandler


class APIHandler:
    __API_key = None

    @classmethod
    def get_API_from_file(cls):
        """
        Parses API stored in non-encrypted file on your computer and stores it in the class.
        :return:
        None
        """
        with open(FileHandler.select_API_file(), 'r') as file:
            cls.__API_key = file.read().strip('\n')

    @classmethod
    def get_API_from_user(cls):
        api = input('Paste your VirusTotal API key: ')
        cls.__API_key = api.strip('\n\t,."\' ')

    @classmethod
    def get_API_key(cls):
        return cls.__API_key

    @classmethod
    def save_API_key(cls):
        FileHandler.save_file(cls.__API_key)
