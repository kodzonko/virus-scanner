import os
import unittest

from src.data.ApiKey import ApiKey


class TestApiKeyHandler(unittest.TestCase):
    def test_add_api_from_missing_file(self) -> None:
        self.assertEqual(
            ApiKey.get_api_key_from_file(rf"/missing_file"), False)
        self.assertIsNone(ApiKey.get_api_key())

    def test_add_api_from_existing_file(self) -> None:
        api_key_file = os.path.realpath("../API-api_key.txt")
        self.assertEqual(
            ApiKey.get_api_key_from_file(rf"{api_key_file}"), True)
        self.assertIsNotNone(ApiKey.get_api_key())

    def test_add_api_from_pdf(self) -> None:
        api_key_file = os.path.realpath(
            "D:\\Documents\\wood-joints-in-classical-japanese-architecture.pdf"
        )
        self.assertEqual(
            ApiKey.get_api_key_from_file(rf"{api_key_file}"), False)
        self.assertIsNone(ApiKey.get_api_key())

    def test_overwrite_api_key_file(self) -> None:
        ApiKey.set_api_key("aaaa")
        self.assertRaises(ApiKey, ApiKey.save_api_key_file)

    def tearDown(self) -> None:
        ApiKey.set_api_key(None)


if __name__ == '__main__':
    unittest.main()
