# !/usr/bin/python3

import pprint


files = {'file': (test_file, open(test_file, 'rb'))}
scan_request = requests.post(scan_url, files=files, params=scan_params)

scan_id = scan_request.json().get('md5')
pprint.pprint(scan_request.json())

if scan_request.status_code != 200:
    print(f"Coś się popsuło, brak wyników. [{scan_request.status_code}]")
else:
    report_url = 'https://www.virustotal.com/vtapi/v2/file/report'
    report_params = {'apikey': f'{api - key}', 'resource': scan_id, 'allinfo': True}
    report_response = requests.get(report_url, params=report_params)
    pprint.pprint(report_response.json())
