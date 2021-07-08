import unittest

from src.data.ApiKey import ApiKey
from src.data.FilesToScan import FilesToScan


class TestFileHandler(unittest.TestCase):
    def test_add_multiple_files(self):
        FilesToScan.add_files_to_scan_queue([fr"D:\Documents\Christiane F - My Dzieci z Dworca Zoo.pdf",
                                       fr"D:\Pictures\Secesja\4b0f6fae57930_k2.jpg",
                                       fr"D:\MEGAsync\Arrival.pur",
                                       fr"Z:\nonexistent_file.jpg"])
        self.assertEqual(3, len(FilesToScan.files_to_scan))


if __name__ == '__main__':
    unittest.main()
