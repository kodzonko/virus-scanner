import unittest

from src.ApiHandler import ApiHandler


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def test_add_api_from_missing_file(self):
        self.assertEqual(ApiHandler.get_api_from_file("/missing_file"), False)
        self.assertIsNone(ApiHandler.get_api_key())

    def test_add_api_from_existing_file(self):
        self.assertEqual(ApiHandler.get_api_from_file("/home/jwadolowski/Desktop/repo/virus-scanner/API-key.txt"), True)
        self.assertIsNotNone(ApiHandler.get_api_key())


if __name__ == '__main__':
    unittest.main()
