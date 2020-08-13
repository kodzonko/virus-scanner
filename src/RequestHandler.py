import time

import requests

from src.ApiHandler import ApiHandler
from src.FileHandler import FileHandler


class RequestHandler:
    scan_ids = []
    reports = []

    @classmethod
    def scan_files(cls):
        """
        Function requesting scans and reports for each file in FileHandler.files_to_scan (list)
        :return:
        json file with scan ID of each file chosen to scan
        """
        # As far as I know you cannot post request with multiple files. It requires dictionary with key value = 'file'
        # (which has to be unique obviously) - so it limits dictionary size to 1.

        url = 'https://www.virustotal.com/vtapi/v2/file/scan'
        params = {'apikey': ApiHandler.get_API_key()}

        def scan_request(file: str):
            file_request = {'file': (file, open(file), 'rb')}
            status_code = -1
            while status_code != 200:
                file_response = requests.post(url, files=file_request, params=params)
                status_code = file_response.status_code
                if file_response.status_code == 200:
                    return file_response
                elif file_response.status_code == 204:
                    print("204 waiting 30")
                    time.sleep(30)
                else:
                    print(f"other error: {file_response.status_code}")

        for file in FileHandler.files_to_scan:
            md5 = scan_request(file).json()['md5']
            cls.scan_ids.append(md5)

    @classmethod
    def get_reports(cls):
        url = 'https://www.virustotal.com/vtapi/v2/file/report'
        params = {'apikey': ApiHandler.get_API_key()}

        def report_request(scan_id: str):
            params.update({'resource': scan_id})
            status_code = -1
            while status_code != 200:
                report_response = requests.get(url, params=params)
                status_code = report_response.status_code
                print(f'status_code {status_code}')
                if report_response.status_code == 200:
                    print("success")
                    return report_response
                elif report_response.status_code == 204:
                    print("204 waiting 30")
                    time.sleep(30)
                else:
                    print(f"other error: {report_response.status_code}")

        for scan_id in cls.scan_ids:
            report_dict = report_request(scan_id).json()
            cls.reports.append(report_dict)

    @classmethod
    def project_time(cls):
        if len(FileHandler.files_to_scan) <= 2:
            return 0
        else:
            return len(FileHandler.files_to_scan) * 30
