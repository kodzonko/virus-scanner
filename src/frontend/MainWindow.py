import os
from tkinter import Tk, Button, Label, filedialog, simpledialog, DISABLED, NORMAL
from typing import Optional, List, Union

from src.data.ApiKey import ApiKey


def select_files() -> Optional[List[str]]:
    """
    Opens a dialogue to navigate and select file(s) to scan.

    :return: A list of file paths or None if the dialogue has been cancelled.
    """
    return filedialog.askopenfilenames(title='Select file(s) to scan',
                                       parent=root)


def save_to_file(content: str) -> None:
    """
    Opens a dialogue to navigate to a directory of choice to save a file with scan report.

    :param content: content to save in a file
    :type content: str
    :return: None
    """
    file = filedialog.asksaveasfilename(mode='w', defaultextension=".txt")
    if file is not None:  # asksaveasfile returns None if dialog closed with "cancel".
        with open(file, 'w', encoding="utf8") as file:
            try:
                file.write(content)
            except IOError:
                print('Unable to create file in that location. Try again.')


def ask_user_for_api_key() -> None:
    api_key = simpledialog.askstring("Input", "What is your first name?",
                                     parent=root)
    if os.path.isfile('./API-api_key.txt'):
        raise RuntimeError("API-api_key.txt already exists")
    else:
        with open('./API-api_key.txt', 'w') as file:
            file.write(api_key)


def center_window(width=400, height=300) -> None:
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    # calculate position x and y coordinates
    x = int((screen_width / 2) - (width / 2))
    y = int((screen_height / 2) - (height / 2))
    root.geometry(f'{width}x{height}+{x}+{y}')


def show_results() -> None:
    # TODO implement this method
    pass


def save_results() -> bool:
    # TODO implement this method
    pass


def button_state() -> Union[NORMAL, DISABLED]:
    if ApiKey.is_api_key:
        return NORMAL
    else:
        return DISABLED


button_view_scheme = {
    'bg': 'DodgerBlue4',
    'fg': 'slate gray',
    'highlightcolor': 'DodgerBlue2',
    'justify': 'center',
    'width': 20,
    'height': 5,
}

root = Tk()

center_window(500, 400)
root.title("Multi engine Virus Scanner")

# TODO this button only visible if API api_key is missing
label_api_key = Label(root,
                      text='Missing API api_key!',
                      fg='red'
                      )

button_get_api_from_user = Button(root,
                                  text="Select API api_key file",
                                  command=ask_user_for_api_key,
                                  **button_view_scheme
                                  )

button_add_files_to_scan_queue = Button(root,
                                        text="Files to scan",
                                        command=select_files,
                                        state=button_state(),
                                        **button_view_scheme
                                        )

button_show_scan_queue = Button(root,
                                text='Show scan results',
                                **button_view_scheme)

button_show_results = Button(root,
                             text="Show scan results",
                             command=show_results,
                             **button_view_scheme
                             )
button_save_results = Button(root,
                             text="Save scan results",
                             command=save_results,
                             **button_view_scheme
                             )

if not ApiKey.is_api_key:
    label_api_key.grid(row=0, column=2)
    button_get_api_from_user.grid(row=1, column=2)

button_add_files_to_scan_queue.grid(column=0, row=1)

button_show_scan_queue.grid(row=1, column=3)
button_show_results.grid(row=3, column=4)
button_save_results.grid(row=4, column=4)

root.mainloop()
