<<<<<<< HEAD
# !/usr/bin/python3

from src.logic.ApiHandler import ApiHandler
from src.logic.FileHandler import FileHandler
from src.logic.RequestHandler import RequestHandler
from src.logic.ReportMaker import ReportMaker

ApiHandler.get_api_from_file()
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
#             cls.get_api_from_user(api)
#         else:
#             file.write(api)
=======
>>>>>>> b6e210b75420b7ea6ee6f217e7e16bf2ae35606a
