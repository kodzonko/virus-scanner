from pathlib import Path
from typing import Union, Optional


class ApiKey:
    def __init__(self, api_key_file: Union[str, Path]):
        with open(api_key_file, 'rt') as file:
            self.__api_key = file.readline()

    @property
    def api_key(self) -> str:
        return self.__api_key

    @api_key.setter
    def api_key(self, key: str) -> None:
        self.__api_key = key
