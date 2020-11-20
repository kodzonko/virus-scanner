from tkinter import filedialog

from src.frontend.MainWindow import root


def select_paths() -> filedialog:
    """
    Opens minimal GUI to navigate and select file(s) of choice
    :return:
    None
    """
    root.withdraw()
    return filedialog.askopenfilenames(parent=root,
                                       initialdir="C:",
                                       title='Select file(s) to scan')


def center_window(width=400, height=300) -> None:
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    # calculate position x and y coordinates
    x = int((screen_width / 2) - (width / 2))
    y = int((screen_height / 2) - (height / 2))
    root.geometry(f'{width}x{height}+{x}+{y}')


def select_files(title: str = "Select file(s)") -> filedialog:
    """
    Opens minimal GUI to navigate and select file(s) of choice
    :return:
    None
    """
    return filedialog.askopenfilenames(parent=root,
                                       initialdir="C:",
                                       title=title)


def select_api_file() -> filedialog:
    """
    Opens minimal GUI to navigate and select file(s) of choice
    :return:
    None
    """
    return filedialog.askopenfilename(
        parent=root,
        initialdir="C:",
        title="Select a file containing your API key")


def save_file(content_to_save: str) -> bool:
    """
    Opens minimal GUI to navigate to a directory of choice to save a file with your API key or scan report.

    :param content_to_save: API-key or scan reports to  save in file
    :type content_to_save: str

    :return:
    None
    """
    file = filedialog.asksaveasfilename(mode='w', defaultextension=".txt")
    if file is not None:  # asksaveasfile returns `None` if dialog closed with "cancel".
        with open(file, 'w') as file:
            try:
                file.write(content_to_save)
            except IOError:
                print('Unable to create file in that location. Try again.')
                return False
            else:
                file.write(content_to_save)
                return True


def show_results() -> None:
    # TODO implement this method
    pass


def save_results() -> bool:
    # TODO implement this method
    pass
