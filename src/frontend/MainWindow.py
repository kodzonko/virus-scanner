from tkinter import Tk, filedialog, Button, Label
from src.ApiHandler import ApiHandler


def center_window(width=400, height=300) -> None:
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    # calculate position x and y coordinates
    x = int((screen_width / 2) - (width / 2))
    y = int((screen_height / 2) - (height / 2))
    root.geometry(f'{width}x{height}+{x}+{y}')


def select_files(title: str = "Select file(s)") -> list:
    """
    Opens minimal GUI to navigate and select file(s) of choice
    :return:
    None
    """
    return filedialog.askopenfilenames(initialdir="C:", title=title)


def select_api_file() -> str:
    """
    Opens minimal GUI to navigate and select file(s) of choice
    :return:
    None
    """
    return filedialog.askopenfilename(initialdir="C:", title="Select a file containing your API key")


def save_file(content_to_save: str):
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
                save_file(content_to_save)
            else:
                file.write(content_to_save)


def show_results():
    # TODO implement this method
    pass


def save_results():
    # TODO implement this method
    pass




root = Tk()
center_window(500, 400)
root.title("Multiengine Virus Scanner")

is_api = Label(root, text="Missing API key!")
is_api.grid()
if ApiHandler.get_API_key() is not None:
    is_api.configure(text="Found API key, we are good to go!")

button_api_file = Button(root, text="Select API file", fg="red", command=select_api_file)
button_save_api = Button(root, text="Save your API to file", fg="red", command=save_file)
button_files_to_scan = Button(root, text="Select files to scan", fg="red", command=select_files)

button_show_results = Button(root, text="Show scan results", fg="red", command=show_results)
button_save_results = Button(root, text="Show scan results", fg="red", command=save_results)

button_api_file.grid(column=0, row=0)
button_save_api.grid(column=1, row=0)
button_files_to_scan.grid(column=0, row=1)

button_show_results.grid(column=0, row=2)
button_save_results.grid(column=1, row=2)

root.mainloop()
