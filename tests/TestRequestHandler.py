import unittest

from src.logic.ApiHandler import ApiHandler
from src.logic.FileHandler import FileHandler
from src.logic.RequestHandler import RequestHandler


class TestRequestsHandler(unittest.TestCase):
    def setUp(self) -> None:
        with open('/home/jwadolowski/Desktop/virus-scanner/API-key.txt', 'r') as file:
            ApiHandler.set_api_key(file.read())
        FileHandler.files_to_scan = [
            '/home/jwadolowski/Desktop/virus-scanner/tests/Files-to-scan/test_file_archive.zip',
            '/home/jwadolowski/Desktop/virus-scanner/tests/Files-to-scan/test_file_executable.exe',
            '/home/jwadolowski/Desktop/virus-scanner/tests/Files-to-scan/test_file_text.txt'
            ]

    def test_scan_single_file(self) -> None:
        RequestHandler.scan_files()
        self.assertEqual(len(RequestHandler.scan_ids), len(FileHandler.files_to_scan))
        self.assertEqual()

    def test_file_above_32_mb(self) -> None:
        pass

    def test_file_above_200_mb(self) -> None:
        pass

    def test_multiple_files(self) -> None:
        pass


    # def test_reports_request_codes(self):
    #     for report in RequestHandler.reports:
    #         for key, value in report:
    #             if key ==
    #             request_codes = [RequestHandler.reports]
    #     self.assertEqual(True, False)


if __name__ == '__main__':
    unittest.main()
