from tkinter import Tk, filedialog


def select_paths():
    """
    Opens minimal GUI to navigate and select file(s) of choice
    :return:
    None
    """
    root = Tk()
    root.withdraw()
    return filedialog.askopenfilenames(parent=root, initialdir="C:", title='Select file(s) to scan')