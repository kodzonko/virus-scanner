import requests

from core.FileHandler import FileHandler
from core.APIHandler import APIHandler


class RequestHandler:
    @classmethod
    def scan_file(cls):
        """
        Function requesting scans and reports for each file in FileHandler.files_to_scan (list)
        :return:
        json file with reports on each files chosen for scanning
        """
        scan_url = 'https://www.virustotal.com/vtapi/v2/file/scan'
        report_url = 'https://www.virustotal.com/vtapi/v2/file/report'
        scan_params = {'apikey': APIHandler.get_API_key()}
        scan_response = requests.post(scan_url, files=FileHandler.files_to_scan, params=scan_params)

        scan_id = scan_response.json()['md5']
        report_params = cls.scan_params.update({'resource': scan_id, 'allinfo': True})
        report_response = requests.get(report_url, params=report_params)

        return report_response.json()
