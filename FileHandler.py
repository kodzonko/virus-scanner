from tkinter import Tk
from tkinter.filedialog import askopenfilename

from .APIHandler import APIHandler


class FileHandler:
    files = []

    @classmethod
    def ask_for_path(cls):
        """
        Opens minimal GUI to navigate and select a file of choice
        :return:
        Path to the chosen file
        """
        Tk().withdraw()
        file = askopenfilename()  # show an "Open" dialog box and return the path to the selected file
        cls.files.append(file)

    scan_url = 'https://www.virustotal.com/vtapi/v2/file/scan'
    scan_params = {'apikey': f'{APIHandler.API_key}'}
