from src.logic.FileHandler import FileHandler


class ApiHandler:
    __api_key = None

    @classmethod
    def get_api_from_file(cls, api_file: str) -> bool:
        """
        Open file provided in function's argument, read API key from it and assign to appropriate variable.
        :param api_file: Path to text file containing your API key
        :return: True if successful, False if not.
        """
        with open(FileHandler.select_api_file(), 'r') as file:
            cls.__api_key = file.read().strip('\n')
        try:
            with open(api_file, 'r') as file:
                cls.__api_key = file.read().strip('\n')
                return True
        except FileNotFoundError:
            return False

    @classmethod
    def get_api_from_user(cls) -> None:
        api = input('Paste your VirusTotal API key: ')
        cls.__api_key = api.strip('\n\t,."\' ')

    @classmethod
    def save_api_key_file(cls) -> None:
        FileHandler.save_file(cls.__api_key)

    @classmethod
    def set_api_key(cls, api: str) -> None:
        cls.__api_key = api

    @classmethod
    def get_api_key(cls) -> str:
        return cls.__api_key
