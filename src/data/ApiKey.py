from typing import Union, Optional


class ApiKey:
    __api_key = None

    @classmethod
    def get_api_key(cls) -> Optional[str]:
        return cls.__api_key

    @classmethod
    def set_api_key(cls, key: str) -> None:
        cls.__api_key = key

    @classmethod
    def is_api_key(cls) -> bool:
        return cls.__api_key is not None
