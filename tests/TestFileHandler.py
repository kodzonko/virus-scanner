import unittest

from src.model.ApiKeyHandler import ApiHandler
from src.model.FileHandler import FileHandler


class TestFileHandler(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def test_add_api_from_missing_file(self):
        self.assertEqual(ApiHandler.get_api_key_from_file(rf"/missing_file"),
                         False)
        self.assertIsNone(ApiHandler.get_api_key())

    def test_add_api_from_existing_file(self):
        self.assertEqual(
            ApiHandler.get_api_key_from_file(
                "/home/jwadolowski/Desktop/repo/virus-scanner/API-key.txt"),
            True)
        self.assertIsNotNone(ApiHandler.get_api_key())

    def test_binary_file_scan(self):
        FileHandler.add_files_to_scan(rf"/usr/bin/bash")

    def test_pdf_file_scan(self):
        pass


if __name__ == '__main__':
    unittest.main()
