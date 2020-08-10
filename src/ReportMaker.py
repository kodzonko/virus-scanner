import pprint

from src.RequestHandler import RequestHandler
from src.FileHandler import FileHandler


class ReportMaker:
    @classmethod
    def print_to_console(cls):
        for report in RequestHandler.reports:
            pprint.pprint(report)

    @classmethod
    def write_to_file(cls):
        FileHandler.save_file(RequestHandler.reports)
