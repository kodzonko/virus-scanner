import os
import time
import requests
from pathlib import Path
from typing import List, Any, Union

from ..data.ApiKey import ApiKey


def api_timeout(function, wait_code: int = 429, sleep_seconds: int = 15) -> Any:
    """
    Decorator function for repeating function in loop until response code is not wait code.

    :param function: 
    :param wait_code: This is  a TooManyRequestsError code returned by the provider.
    :param sleep_seconds: How long to wait between iterations. Calculate it based on the documentation.
    """

    def inner():
        processed_successfully = False
        while not processed_successfully:
            result = function()
            if result.status_code == wait_code:
                time.sleep(sleep_seconds)
            else:
                return function()

    return inner


def request_scans(scan_queue: List[Path, str]) -> List[str]:
    """
    Function requesting scans for files in a scan queue list.

    :param scan_queue: A list of file paths to scan
    :type scan_queue: List[Path, str]
    :return: dictionary, where keys are file paths and values are scan ids
    """
    # As far as I know you cannot post request with multiple files. The API requires a dictionary with key value = 'file'
    # (which has to be unique obviously) - so it limits dictionary size to 1.

    small_file_url = 'https://www.virustotal.com/vtapi/v2/file/scan'
    big_file_url = 'https://www.virustotal.com/api/v3/files/upload_url'
    api_key = {'apikey': ApiKey.get_api_key()}

    scan_ids = []

    def get_upload_url() -> str:
        upload_url_json = api_timeout(requests.get(
            url=big_file_url,
            params=api_key
        )).json()
        return upload_url_json['upload_url']

    def get_scan_id(url: str, file_to_scan: Union[Path, str]) -> str:
        response = api_timeout(
            requests.post(
                url=url,
                files={'file': (file_to_scan, open(file_to_scan, 'rb'))},
                params=api_key)
        )
        return response.json()['md5']

    bytes_in_mb = 1_000_000

    for file in scan_queue:
        if (os.path.getsize(file) / bytes_in_mb) > 32:
            upload_url = get_upload_url()
        elif (os.path.getsize(file) / bytes_in_mb) > 200:
            # TODO test if accepted else raise exception
            pass
        else:
            upload_url = small_file_url
        scan_ids.append(get_scan_id(url=upload_url, file_to_scan=file))

    return scan_ids


def get_reports(scan_ids: list) -> List[dict]:
    url = 'https://www.virustotal.com/vtapi/v2/file/report'
    params = {'apikey': ApiKey.get_api_key()}
    reports = []

    def get_report(scan_id: str) -> dict:
        params['resource'] = scan_id
        response = api_timeout(requests.get(url=url, params=params))
        return response.json()

    for scan_id in scan_ids:
        reports.append(get_report(scan_id))

    return reports


def estimate_time():
    """
    Estimates to to finish processing the queue based on number of files and knowledge about max daily resource quota
    :return: time in minutes(?)
    """
    # TODO maybe later
    pass
