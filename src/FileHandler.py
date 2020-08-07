from tkinter import Tk, filedialog


class FileHandler:
    files_to_scan = []

    @classmethod
    def select_files_to_scan(cls):
        """
        Opens minimal GUI to navigate and select file(s) of choice
        :return:
        None
        """
        root = Tk()
        root.withdraw()
        selected_files = filedialog.askopenfilenames(parent=root, initialdir="C:", title='Select file(s) to scan')
        for file in selected_files:
            cls.files_to_scan.append(file)

    @classmethod
    def select_API_file(cls):
        """
        Opens minimal GUI to navigate and select file(s) of choice
        :return:
        None
        """
        root = Tk()
        root.withdraw()
        selected_file = filedialog.askopenfilename(parent=root, initialdir="C:", title="Select a file containing your API key")
        return selected_file

    @classmethod
    def save_API_file(cls, api: str):
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
