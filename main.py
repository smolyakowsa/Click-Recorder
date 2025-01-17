import customtkinter
from create_project import CreateProject
from open_project import OpenProject

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title("Click Recorder")
        self.geometry("700x500")

        self.create = customtkinter.CTkButton(self, text='Create', command=self.create_project)
        self.create.place(relx=0.1, rely= 0.1)

        self.play = customtkinter.CTkButton(self, text='Play', command=self.open_project)
        self.play.place(relx=0.5, rely= 0.1)

        self.close = customtkinter.CTkButton(self, text='Close', command=self.destroy)
        self.close.place(relx=0.4, rely=0.9)

    def create_project(self):
        self.withdraw()
        CreateProject(self)


    def open_project(self):
        self.withdraw()
        OpenProject(self)

if __name__ == "__main__":
    app = App()
    app.mainloop()