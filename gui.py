import tkinter
import tkinter.filedialog

folder_selected = None


def app():
    def select_folder():
        global folder_selected
        folder_selected = tkinter.filedialog.askdirectory()
        if folder_selected:
            label_2.config(text = "Folder Selected")
            confirm_btn.config(state = "normal")
        else:
            label_2.config(text = "No Folder Selected")
            confirm_btn.config(state = "disabled")
    window = tkinter.Tk()

    window.title("EchoSort")
    window.geometry("250x150")

    label_1 = tkinter.Label(window, text = "Select Folder")
    label_1.grid(row = 0, padx = 20, pady = 10, columnspan = 2)

    label_2 = tkinter.Label(window, text = "No Folder Selected")
    label_2.grid(row = 1, padx = 10, pady = 5, columnspan = 2)

    select_btn = tkinter.Button(window, text = "Browse Folder", command = select_folder)
    select_btn.grid(column = 0, row = 2, padx = 20, pady = 10)

    confirm_btn = tkinter.Button(window, text = "Start Sorting", command = window.quit, state = "disabled")
    confirm_btn.grid(column = 1, row = 2, padx = 20, pady = 10)

    window.mainloop()

    return folder_selected