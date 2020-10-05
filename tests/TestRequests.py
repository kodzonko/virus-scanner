import unittest

from src.ApiHandler import ApiHandler
from src.FileHandler import FileHandler
from src.RequestHandler import RequestHandler


class TestRequests(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def test_scan_single_file(self):
        RequestHandler.scan_files()
        self.assertEqual(len(RequestHandler.scan_ids), len(FileHandler.files_to_scan))
        self.assertEqual()

    def test_file_above_32_mb(self):
        pass

    def test_file_above_200_mb(self):
        pass

    def test_multiple_files(self):
        pass


    # def test_reports_request_codes(self):
    #     for report in RequestHandler.reports:
    #         for key, value in report:
    #             if key ==
    #             request_codes = [RequestHandler.reports]
    #     self.assertEqual(True, False)


if __name__ == '__main__':
    unittest.main()
