import tkinter
import tkinter.filedialog
import os
import sys
from utility import get_exe_path

folder_selected = None


def app():
    def select_folder():
        global folder_selected
        folder_selected = tkinter.filedialog.askdirectory()
        if folder_selected:
            label_2.config(text = "Folder Selected")
            confirm_btn.config(state = "normal")
            unselect_btn.config(state = "normal")
        else:
            label_2.config(text = "No Folder Selected")
            confirm_btn.config(state = "disabled")
            unselect_btn.config(state = "disabled")


    def unselect_folder():
        global folder_selected
        folder_selected = None
        label_2.config(text = "No Folder Selected")
        confirm_btn.config(state = "disabled")
        unselect_btn.config(state = "disabled")


    window = tkinter.Tk()

    window.title("EchoSort")
    window.geometry("375x150")
    try:
        window.iconbitmap(os.path.join(get_exe_path(), "assets/icon.ico"))
    except Exception as e:
        print(f"Warning: Could not set icon — {e}")

    label_1 = tkinter.Label(window, text = "Select Folder")
    label_1.grid(row = 0, padx = 20, pady = 10, columnspan = 3)
    label_2 = tkinter.Label(window, text = "No Folder Selected")
    label_2.grid(row = 1, padx = 10, pady = 5, columnspan = 3)

    select_btn = tkinter.Button(window, text = "Browse Folder", command = select_folder)
    select_btn.grid(column = 0, row = 2, padx = 20, pady = 10)

    confirm_btn = tkinter.Button(window, text = "Start Sorting", command = window.quit, state = "disabled")
    confirm_btn.grid(column = 1, row = 2, padx = 20, pady = 10)

    unselect_btn = tkinter.Button(window, text = "Unselect Folder", command = unselect_folder, state = "disabled")
    unselect_btn.grid(column = 2, row = 2, padx = 20, pady = 10)

    window.resizable(False, False)
    window.mainloop()

    return folder_selected