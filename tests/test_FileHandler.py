import unittest

import src.FileHandler


class MyTestCase(unittest.TestCase):
    def setUp(self):
        pass

    def test_something(self):
        self.assertEqual(True, False)


# allows us to run all the tests just by running the file
if __name__ == '__main__':
    unittest.main()
