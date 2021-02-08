import os
from tkinter import filedialog


class FileHandler:
    files_to_scan = []

    @classmethod
    def add_files_to_scan(cls, paths: list) -> None:
        """
        Opens minimal GUI to navigate and select file(s) of choice
        :return:
        None
        """
        for path in paths:
            if os.path.isfile(path):
                cls.files_to_scan.append(path)

    @classmethod
    def select_api_file(cls) -> str:
        """
        Opens minimal GUI to navigate and select file(s) of choice
        :return:
        None
        """
        selected_file = filedialog.askopenfilename(
            title="Select a file containing your API key",
            defaultextension=".txt")
        return selected_file

    @classmethod
    def save_file(cls, content_to_save) -> None:
        """
        Opens minimal GUI to navigate to a directory of choice to save a file with your API key or scan report.
        :param content_to_save: API-key or scan reports to  save in file
        :type content_to_save: str
        :return:
        None
        """
        file = filedialog.asksaveasfilename(mode='w', defaultextension=".txt")
        if file is not None:  # asksaveasfile returns None if dialog closed with "cancel".
            with open(file, 'w', encoding="utf8") as file:
                try:
                    file.write(content_to_save)
                except IOError:
                    print('Unable to create file in that location. Try again.')
                    cls.save_file(content_to_save)
                else:
                    file.write(content_to_save)
