import customtkinter
from create_project import CreateProject
from open_project import OpenProject

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title("Click Recorder")
        self.geometry("700x500")
        self._set_appearance_mode('light')

        self.create = customtkinter.CTkButton(self, text='Create', width=250, height=50,border_width = 0,
                                              corner_radius=10, command=self.create_project)
        self.create.place(relx=0.1, rely= 0.1)

        self.open_project = customtkinter.CTkButton(self, text='Open', width=250, height=50,border_width = 0,
                                              corner_radius=10,command=self.open_project)
        self.open_project.place(relx=0.55, rely= 0.1)

        self.close = customtkinter.CTkButton(self, text='Close', width=250, height=50,border_width = 0,
                                              corner_radius=10, command=self.destroy)
        self.close.place(relx=0.33, rely=0.8)

    def create_project(self):
        self.withdraw()
        CreateProject(self)


    def open_project(self):
        self.withdraw()
        OpenProject(self)

if __name__ == "__main__":
    app = App()
    app.mainloop()