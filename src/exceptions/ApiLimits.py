import requests


class TooManyRequests(Exception):
    def __init__(self, value):
        self.value = requests.exceptions

    def __str__(self):
        return repr(self.value)
