from tkinter import Tk, filedialog


class FileHandler:
    files_to_scan = []
    api_file = None

    @classmethod
    def select_files_to_scan(cls):
        """
        Opens minimal GUI to navigate and select file(s) of choice
        :return:
        None
        """
        selected_files = Tk().withdraw()  # we don't want a full GUI, so keep the root window from appearing
        selected_files.lift()
        selected_files.focus_force()

        selected_files.file_name = filedialog.askopenfilenames(initialdir="C:", title="Select file(s) to scan")
        cls.files_to_scan.extend(selected_files)

    @classmethod
    def select_API_file(cls):
        """
        Opens minimal GUI to navigate and select file(s) of choice
        :return:
        None
        """
        selected_file = Tk().withdraw()  # we don't want a full GUI, so keep the root window from appearing
        selected_file.lift()
        selected_file.focus_force()

        selected_file.file_name = filedialog.askopenfilename(initialdir="C:",
                                                             title="Select a file containing your API key")
        cls.api_file = selected_file

    @classmethod
    def save_file(cls, api: str):
        """
        Opens minimal GUI to navigate to a directory of choice to save a file with your API key or scan report.

        :param api: API-key to save in a specified file
        :type api: str

        :return:
        None
        """

        file = filedialog.asksaveasfilename(mode='w', defaultextension=".txt")
        if file is not None:  # asksaveasfile returns `None` if dialog closed with "cancel".
            with open(file, 'w') as file:
                try:
                    file.write(api)
                except IOError:
                    print('Unable to create file in that location. Try again.')
                    cls.save_API_file(api)
                else:
                    file.write(api)
