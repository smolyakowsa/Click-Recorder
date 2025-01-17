import customtkinter
from create_window import CreateProject

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title("Click Recorder")
        self.geometry("700x500")

        self.create = customtkinter.CTkButton(self, text='Create', command=self.create_project)
        self.create.place(relx=0.1, rely= 0.1)

        self.play = customtkinter.CTkButton(self, text='Play', command=self.open_project)
        self.play.place(relx=0.5, rely= 0.1)

    def create_project(self):
        self.withdraw()
        CreateProject(self)


    def open_project(self):
        print('Кнопка 2')

if __name__ == "__main__":
    app = App()
    app.mainloop()