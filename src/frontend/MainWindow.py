from tkinter import Tk, filedialog, Button, Label

from src.frontend import Buttons
from src.model.ApiHandler import ApiHandler

root = Tk()
Buttons.center_window(500, 400)
root.title("Multiengine Virus Scanner")

is_api = Label(root, text="Missing API key!")
is_api.grid()
if ApiHandler.get_api_key() is not None:
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
