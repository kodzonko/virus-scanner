import pprint

from .FileHandler import FileHandler


class ReportMaker:
    def print_to_console():
        FileHandler.ask_for_path()

    def write_to_file(target_file):
        pass

    if print_output == True:
        pass

    if write_output == True:
        pass

    pprint.pprint(scan_request.json())

    if scan_request.status_code != 200:
        print(f"Coś się popsuło, brak wyników. [{scan_request.status_code}]")
    else:
        report_url = 'https://www.virustotal.com/vtapi/v2/file/report'
        report_params = {'apikey': f'{api - key}', 'resource': scan_id, 'allinfo': True}
        report_response = requests.get(report_url, params=report_params)
        pprint.pprint(report_response.json())
