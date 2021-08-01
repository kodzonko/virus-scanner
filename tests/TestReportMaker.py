import unittest

from src.data.ApiKey import ApiKey


class TestReportMaker(unittest.TestCase):
    api_key = ApiKey(rf"../API-key.txt")


if __name__ == '__main__':
    unittest.main()
