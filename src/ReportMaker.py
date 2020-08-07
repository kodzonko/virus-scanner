import pprint

from core.RequestHandler import RequestHandler
from core.FileHandler import FileHandler
from core.APIHandler import APIHandler


class ReportMaker:
    @classmethod
    def print_to_console(cls):
        pprint.pprint(RequestHandler.scan_file())

    @classmethod
    def write_to_file(cls):
        FileHandler.save_file(APIHandler.get_API_key())
