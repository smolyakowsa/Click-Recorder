import os

import customtkinter

class OpenProject(customtkinter.CTkToplevel):
    def __init__(self, main_app):
        super().__init__()
        self.main_app = main_app
        self.title("Open project")
        self.geometry("700x500")

        self.close_button = customtkinter.CTkButton(self, text="Close",width=250, height=50,border_width = 0,
                                              corner_radius=10, command=self.close_window)
        self.close_button.place(relx=0.33, rely=0.85)

        self.play = customtkinter.CTkButton(self, text="Play", width=250, height=50, border_width=0,
                                                    corner_radius=10, command=self.play)
        self.play.place(relx=0.6, rely=0.1)

        self.delete = customtkinter.CTkButton(self, text="Delete", width=250, height=50, border_width=0,
                                            corner_radius=10, command=self.close_window)
        self.delete.place(relx=0.6, rely=0.25)

        self.delete_all = customtkinter.CTkButton(self, text="Delete all", width=250, height=50, border_width=0,
                                              corner_radius=10, command=self.close_window)
        self.delete_all.place(relx=0.6, rely=0.4)

        self.rename = customtkinter.CTkButton(self, text="Rename", width=250, height=50, border_width=0,
                                                  corner_radius=10, command=self.close_window)
        self.rename.place(relx=0.6, rely=0.55)

        self.choose = customtkinter.CTkComboBox(self, width=300, height=50, values=self.files_view())
        self.choose.place(relx=0.05, rely=0.1)

    def close_window(self):
        self.destroy()
        self.main_app.deiconify()

    def files_view(self):
        path = str(os.getcwd()) + '\\records\\'
        files_list = list(os.listdir(path))
        return files_list

    def play(self):
        file_to_play = self.choose.get()
        self.withdraw()
        os.system(file_to_play)
        self.deiconify