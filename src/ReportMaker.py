import pprint

from src.RequestHandler import RequestHandler
from src.FileHandler import FileHandler


class ReportMaker:
    @classmethod
    def print_to_console(cls):
        output = f""
        for report in RequestHandler.reports:
            for engine in report.values():
                print(f"report values {engine}")
                for key, value in engine.items():
                    output += key + ": " + str(value['detected'])
                    if value['detected'] == 'true':
                        output += ": " + value['result']
                    output += "\n"
        print(output)

    @classmethod
    def write_to_file(cls):
        FileHandler.save_file(RequestHandler.reports)
