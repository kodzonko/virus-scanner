from tkinter import Tk, filedialog


class FileHandler:

    files_to_scan = []
    @classmethod
    def select_files_to_scan(cls):
        """
        Opens minimal GUI to navigate and select file(s) of choice
        :return:
        Path (str) to the chosen file(s)
        """
        selected_files = Tk().withdraw()  # we don't want a full GUI, so keep the root window from appearing
        selected_files.lift()
        selected_files.focus_force()

        selected_files.file_name = filedialog.askopenfilenames(initialdir="C:", title="Select file(s) to scan")
        cls.files_to_scan.extend(selected_files)

    def select_API_file(cls):
        """
        Opens minimal GUI to navigate and select file(s) of choice
        :return:
        Path (str) to the chosen file(s)
        """
        selected_files = Tk().withdraw()  # we don't want a full GUI, so keep the root window from appearing
        selected_files.lift()
        selected_files.focus_force()

        selected_files.file_name = filedialog.askopenfilenames(initialdir="C:", title="Select a file containing your API key")
        cls.files_to_scan.extend(selected_files)