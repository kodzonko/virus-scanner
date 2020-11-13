from src.model.FileHandler import FileHandler


class ApiHandler:
    __api_key = None

    @classmethod
    def get_api_from_file(cls):
        """
        Parses API stored in non-encrypted file on your computer and stores it in the class.
        :return:
        None
        """
        with open(FileHandler.select_api_file(), 'r') as file:
            cls.__api_key = file.read().strip('\n')

    @classmethod
    def get_api_from_user(cls):
        api = input('Paste your VirusTotal API key: ')
        cls.__api_key = api.strip('\n\t,."\' ')

    @classmethod
    def get_api_key(cls):
        return cls.__api_key

    @classmethod
    def save_api_key_file(cls):
        FileHandler.save_file(cls.__api_key)

    @classmethod
    def set_api_key(cls, api: str):
        cls.__api_key = api
