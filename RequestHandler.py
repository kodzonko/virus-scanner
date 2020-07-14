import requests


class RequestHandler:
    files = {'file': (, open(test_file, 'rb'))}
    scan_request = requests.post(scan_url, files=files, params=scan_params)

    scan_id = scan_request.json().get('md5')
