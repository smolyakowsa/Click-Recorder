import customtkinter


class CreateWindow(customtkinter.CTkToplevel):
    def __init__(self):
        super().__init__()
        self.title("Creat new record")
        self.geometry("700x500")
        self.label = customtkinter.CTkLabel(self, text="Creat new record")
        self.label.pack(pady=20)
        self.close_button = customtkinter.CTkButton(self, text="Закрыть", command=self.destroy)
        self.close_button.pack(pady=10)
