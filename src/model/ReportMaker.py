from src.model.FileHandler import FileHandler
from src.model.RequestHandler import RequestHandler


class ReportMaker:
    @classmethod
    def print_to_console(cls):
        output = f""
        for report in RequestHandler.reports:
            report = report['scans']
            for engine, details in report.items():
                output += engine + ": " + details['result'] + "\n"
        print(output)

    @classmethod
    def write_to_file(cls):
        FileHandler.save_file(RequestHandler.reports)
