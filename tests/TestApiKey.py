import os
import unittest

from src.data.ApiKey import ApiKey


class TestApiKeyHandler(unittest.TestCase):
    api_from_missing_file = ApiKey(rf"/missing_file")
    api_from_existing_file = ApiKey(rf"../API-key.txt")

    def test_add_api_from_missing_file(self) -> None:
        self.assertIsNone(TestApiKeyHandler.api_from_missing_file.api_key)

    def test_add_api_from_existing_file(self) -> None:
        self.assertIsNotNone(TestApiKeyHandler.api_from_existing_file.api_key)

    def test_overwrite_api_key_file(self) -> None:
        TestApiKeyHandler.api_from_missing_file.api_key = 'qwerty'
        self.assertIsNotNone(TestApiKeyHandler.api_from_missing_file.api_key)


if __name__ == '__main__':
    unittest.main()
