import requests

from src.FileHandler import FileHandler
from src.APIHandler import APIHandler


class RequestHandler:
    scan_ids = []
    reports = []

    @classmethod
    def scan_file(cls):
        """
        Function requesting scans and reports for each file in FileHandler.files_to_scan (list)
        :return:
        json file with scan ID of each file chosen to scan
        """
        url = 'https://www.virustotal.com/vtapi/v2/file/scan'
        params = {'apikey': APIHandler.get_API_key()}

        # As far as I know you cannot post request with multiple files. It requires dictionary with key value = 'file'
        # (which has to be unique obviously) - so it limits dictionary size to 1.
        for file in FileHandler.files_to_scan:
            tmp_file = {'file': (file, open(file), 'rb')}
            scan_response = requests.post(url, files=tmp_file, params=params)
            cls.scan_ids.append(scan_response.json()['md5'])

    @classmethod
    def get_report(cls):
        url = 'https://www.virustotal.com/vtapi/v2/file/report'
        params = {'apikey': APIHandler.get_API_key()}
        for scan_id in cls.scan_ids:
            params.update({'resource': scan_id})
            report_response = requests.get(url, params=params).json()
            cls.reports.append(report_response)
