# !/usr/bin/python3

from src.ApiHandler import ApiHandler
from src.FileHandler import FileHandler
from src.RequestHandler import RequestHandler
from src.ReportMaker import ReportMaker

example = {
 'response_code': 1,
 'verbose_msg': 'Scan finished, scan information embedded in this object',
 'resource': '99017f6eebbac24f351415dd410d522d',
 'scan_id': '52d3df0ed60c46f336c131bf2ca454f73bafdc4b04dfa2aea80746f5ba9e6d1c-1273894724',
 'md5': '99017f6eebbac24f351415dd410d522d',
 'sha1': '4d1740485713a2ab3a4f5822a01f645fe8387f92',
 'sha256': '52d3df0ed60c46f336c131bf2ca454f73bafdc4b04dfa2aea80746f5ba9e6d1c',
 'scan_date': '2010-05-15 03:38:44',
 'permalink': 'https://www.virustotal.com/file/52d3df0ed60c46f336c131bf2ca454f73bafdc4b04dfa2aea80746f5ba9e6d1c/analysis/1273894724/',
 'positives': 40,
 'total': 40,
 'scans': {
   'nProtect': {
     'detected': 'true',
     'version': '2010-05-14.01',
     'result': 'Trojan.Generic.3611249',
     'update': '20100514'
   },
   'CAT-QuickHeal': {
     'detected': 'true',
     'version': '10.00',
     'result': 'Trojan.VB.acgy',
     'update': '20100514'
   },
   'McAfee': {
     'detected': 'true',
     'version': '5.400.0.1158',
     'result': 'Generic.dx!rkx',
     'update': '20100515'
   },
   'TheHacker': {
     'detected': 'true',
     'version': '6.5.2.0.280',
     'result': 'Trojan/VB.gen',
     'update': '20100514'
   },
   'VirusBuster': {
    'detected': 'true',
     'version': '5.0.27.0',
     'result': 'Trojan.VB.JFDE',
     'update': '20100514'
   }
 }
}

wyniki_jednego_skanowania = example['scans']
for engine,details in wyniki_jednego_skanowania.items():
    print(engine + ": " + str(details['result']))



ApiHandler.get_API_from_file()
FileHandler.select_files_to_scan()
RequestHandler.scan_files()
RequestHandler.get_reports()
# print(RequestHandler.scan_ids)
# print(RequestHandler.reports)
ReportMaker.print_to_console()
# ReportMaker.write_to_file()



# import tkinter as tk
#
# from .FileHandler import FileHandler

# window = tk.Tk()
#
# greeting = tk.Label(text="Welcome in virus scanner")
# greeting.pack()
#
# if FileHandler.api_file is None:
#     instruction = tk.Label(text="You need obtain a free VirusTotal API key to be able to use this program")
#     instruction.pack()
#
#     register_VirusTotal = tk.Button()
#     register_VirusTotal.pack()
#     api_field = tk.Entry()
#     api_field.pack()
#
#
# window.mainloop()

# store_API = input('Do you want to store your API key in file for further scans [yes|no]: ')
# if store_API.lower() == 'yes' or store_API.lower() == 'y':
#     if FileHandler.api_file is not None:
#         warnings.warn(f"There already is an API key stored in your config file:\n{FileHandler.api_file}",
#                       ResourceWarning)
#     with open('api_key.txt', 'a') as file:
#         try:
#             file.write(api)
#         except IOError:
#             print('Unable to create file in that location. Try again.')
#             cls.get_API_from_user(api)
#         else:
#             file.write(api)
