import unittest

from src.ApiHandler import ApiHandler
from src.FileHandler import FileHandler
from src.RequestHandler import RequestHandler


class TestMultipleFiles(unittest.TestCase):
    def setUp(self):
        with open('/home/jwadolowski/Desktop/virus-scanner/API-key.txt', 'r') as file:
            ApiHandler.set_API_key(file.read())
        FileHandler.files_to_scan = ['/home/jwadolowski/Desktop/virus-scanner/tests/test_file_archive.zip',
                                     '/home/jwadolowski/Desktop/virus-scanner/tests/test_file_executable.exe',
                                     '/home/jwadolowski/Desktop/virus-scanner/tests/test_file_text.txt'
                                     ]

    def test_scan_files(self):
        RequestHandler.scan_files()
        self.assertEqual(len(RequestHandler.scan_ids), len(FileHandler.files_to_scan))
        self.assertEqual()

    # def test_reports_request_codes(self):
    #     for report in RequestHandler.reports:
    #         for key, value in report:
    #             if key ==
    #             request_codes = [RequestHandler.reports]
    #     self.assertEqual(True, False)


if __name__ == '__main__':
    unittest.main()
