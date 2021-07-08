from pathlib import Path
from typing import List, Union

import src.logic.RequestHandler
import src.data.FilesToScan


def print_to_console(reports: List[dict]) -> None:
    """
    Prints to console a full scan report for all files

    :param reports: list of reports in JSON format (python dicts)
    :type reports: List[dict]
    """
    output = f""
    for report in reports:
        report = report['scans']
        for engine, details in report.items():
            output += engine + ": " + details.get('result') + "\n"
    print(output)
    # or:
    # for report in reports:
    #     pprint(report)


def write_to_file(reports: List[dict], path: Union[str, Path]) -> None:
    """
    Writes all reports to a text file

    :param path: A path to save the file with reports
    :type path: A string or a PurePath.Path object
    :param reports: list of reports in JSON format (python dicts)
    :type reports: List[dict]
    
    :return: None
    """
    with open(path, 'at') as file:
        for report in reports:
            file.write(report)
