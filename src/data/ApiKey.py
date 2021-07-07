from pathlib import Path
from typing import Union, Optional


class ApiKey:
    def __init__(self, api_key_file: Union[str, Path]):
        with open(api_key_file, 'rt') as file:
            self.__api_key = file.readline()

    @property
    def api_key(self) -> Optional[str]:
        return self.__api_key

    @property.setter
    def api_key(self, key: str) -> None:
        self.__api_key = key

    def is_api_key(self) -> bool:
        return self.api_key is not None
