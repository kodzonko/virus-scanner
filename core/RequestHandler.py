import json

import requests

from core.FileHandler import FileHandler
from core.APIHandler import APIHandler


class RequestHandler:
    @classmethod
    def scan_file(cls):
        """
        Function requesting scans and reports for each file in FileHandler.files_to_scan (list)
        :return:
        json file with scan ID of each file chosen to scan
        """
        url = 'https://www.virustotal.com/vtapi/v2/file/scan'
        params = {'apikey': APIHandler.get_API_key()}
        scan_ids = []

        # As far as I know you cannot post request with multiple files. It requires dictionary with key value = 'file'
        # (which has to be unique obviously) - so it limits dictionary size to 1.
        for file in FileHandler.files_to_scan:
            tmp_file = {'file': (file, open(file), 'rb')}
            scan_response = requests.post(url, files=tmp_file, params=params)
            scan_ids.append(scan_response.json()['md5'])
        return scan_ids

    @classmethod
    def get_report(cls):
        reports = []
        url = 'https://www.virustotal.com/vtapi/v2/file/report'
        for scan_id in cls.scan_file():
            params = {'apikey': APIHandler.get_API_key(), 'resource': scan_id, 'allinfo': True}
            reports.append(requests.get(url, params=params))
        return reports
