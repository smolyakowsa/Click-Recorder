import customtkinter
from additional_windows import create_window

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title("Click Recorder")
        self.geometry("700x500")

        self.create = customtkinter.CTkButton(self, text='Create', command=self.create)
        self.create.place(relx=0.1, rely= 0.1)

        self.play = customtkinter.CTkButton(self, text='Play', command=self.play)
        self.play.place(relx=0.5, rely= 0.1)

    def create(self):
        create_window.CreateWindow()

    def play(self):
        print('Кнопка 2')

if __name__ == "__main__":
    app = App()
    app.mainloop()