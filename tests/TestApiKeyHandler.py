import os
import unittest

from src.exceptions.ApiKeyExceptions import ApiKeyFileExists
from src.logic.ApiKeyHandler import ApiKeyHandler


class TestApiKeyHandler(unittest.TestCase):
    def test_add_api_from_missing_file(self) -> None:
        self.assertEqual(
            ApiKeyHandler.get_api_key_from_file(rf"/missing_file"), False)
        self.assertIsNone(ApiKeyHandler.get_api_key())

    def test_add_api_from_existing_file(self) -> None:
        api_key_file = os.path.realpath("../API-key.txt")
        self.assertEqual(
            ApiKeyHandler.get_api_key_from_file(rf"{api_key_file}"), True)
        self.assertIsNotNone(ApiKeyHandler.get_api_key())

    def test_add_api_from_pdf(self) -> None:
        api_key_file = os.path.realpath(
            "D:\\Documents\\wood-joints-in-classical-japanese-architecture.pdf"
        )
        self.assertEqual(
            ApiKeyHandler.get_api_key_from_file(rf"{api_key_file}"), False)
        self.assertIsNone(ApiKeyHandler.get_api_key())

    def test_overwrite_api_key_file(self) -> None:
        ApiKeyHandler.set_api_key("aaaa")
        self.assertRaises(ApiKeyFileExists, ApiKeyHandler.save_api_key_file)

    def tearDown(self) -> None:
        ApiKeyHandler.set_api_key(None)


if __name__ == '__main__':
    unittest.main()
