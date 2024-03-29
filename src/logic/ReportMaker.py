from pprint import pprint

import numpy as np
import pandas as pd
from pathlib import Path
from typing import List, Union

import json


def generate_report(json: dict) -> str:
    """
    Converts a VirusTotal scan report into custom Virus Scanner report
    :param json: json report returned by VirusTotal
    :type json: dict
    :return: A string representation of scan report for all antiviruses
    """
    df = pd.DataFrame(json['scans'])
    df = df.rename_axis('antivirus')
    df = df.transpose()
    df.drop(['version', 'update'], axis=1, inplace=True)
    df.sort_values(by=['detected'], ascending=False, inplace=True)
    return str(df)


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


with open(r'D:\Desktop\repo\virus-scanner\tests\Resources\report3-false-positive.json', 'rt') as f:
    json = json.load(f)
# print(type(json.get('scans').values()))
# pprint(json['scans'].keys())
print(generate_report(json))
