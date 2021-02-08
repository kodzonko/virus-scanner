import os

from src.exceptions.ApiKeyExceptions import ApiKeyFileExists


class ApiKeyHandler:
    __api_key = None

    @classmethod
    def get_api_key_from_file(cls, api_file: str) -> bool:
        """
        Open file provided in function's argument, read API key from it and assign to appropriate variable.
        :param api_file: Path to text file containing your API key
        :return: True if successful, False if not.
        """
        try:
            with open(api_file, 'r', encoding="utf8") as file:
                cls.__api_key = file.read().strip('\n')
                return True
        except FileNotFoundError:
            return False
        except UnicodeDecodeError:
            return False

    @classmethod
    def get_api_key_from_user(cls, api_key: str) -> None:
        cls.__api_key = api_key.strip('\n\t,."\' ')

    @classmethod
    def save_api_key_file(cls) -> bool:
        path = os.path.abspath(
            fr"{os.path.dirname(__file__)}../../../Api-key.txt")
        if os.path.isfile(path):
            raise ApiKeyFileExists(
                fr"File Api-key.txt already exists in {path}. If want to change you API key for VirusTotal do so manually or delete the file"
            )
        else:
            try:
                with open(path, "w", encoding="utf8") as file:
                    file.write(cls.get_api_key())
                    return True
            except IOError(fr"I don't have permission to write in {path}"):
                return False
            finally:
                return False

    @classmethod
    def set_api_key(cls, api_key: str) -> None:
        cls.__api_key = api_key

    @classmethod
    def get_api_key(cls) -> str:
        return cls.__api_key
