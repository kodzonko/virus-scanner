from tkinter import Tk, filedialog


class FileHandler:

    @classmethod
    def ask_for_path(cls):
        """
        Opens minimal GUI to navigate and select file(s) of choice
        :return:
        Path (str) to the chosen file(s)
        """
        file_picker_window = Tk().withdraw()  # we don't want a full GUI, so keep the root window from appearing
        file_picker_window.lift()
        file_picker_window.focus_force()

        file_picker_window.file_name = filedialog.askopenfilenames(initialdir="C:", title="Select file(s)")
        return [file_picker_window]
