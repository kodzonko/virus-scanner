import os
import time
import requests


def api_timeout(function, wait_code: int):
    def inner(*args, **kwargs):
        processed_successfully = False
        while not processed_successfully:
            result = function()
            if result.status_code == wait_code:
                time.sleep(30)
                print("sleeping 30")
            else:
                return function(*args, **kwargs)
    # TODO
    return inner


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

        small_file_url = 'https://www.virustotal.com/vtapi/v2/file/scan'
        big_file_url = 'https://www.virustotal.com/api/v3/files/upload_url'
        params = {'x-apikey': ApiHandler.get_api_key()}

        def scan_small_file(file: str):
            file_request = {'file': (file, open(file), 'rb')}
            status_code = -1
            while status_code != 200:
                file_response = requests.post(small_file_url,
                                              files=file_request,
                                              headers=params)
                status_code = file_response.status_code
                if file_response.status_code == 200:
                    return file_response
                elif file_response.status_code == 204:
                    print("204 waiting 30")
                    time.sleep(30)
                else:
                    print(f"other error: {file_response.status_code}")

        def scan_big_file(file: str):
            url_request = requests.get(big_file_url,
                                       params=params).json()['upload_url']
            file_request = {'file': (file, open(file), 'rb')}
            status_code = -1
            while status_code != 200:
                file_response = requests.get

        for file in FileHandler.files_to_scan:
            if os.path.getsize(file) * 0.000001 > 32:
                pass
            if os.path.getsize(file) * 0.000001 > 200:
                return
            md5 = scan_small_file(file).json()['md5']
            cls.scan_ids.append(md5)

    @classmethod
    def get_reports(cls):
        url = 'https://www.virustotal.com/vtapi/v2/file/report'
        params = {'apikey': ApiHandler.get_api_key()}

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
