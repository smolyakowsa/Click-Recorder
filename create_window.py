import customtkinter


class CreateProject(customtkinter.CTkToplevel):
    def __init__(self, main_app):
        super().__init__()
        self.main_app = main_app
        self.title("Creat new record")
        self.geometry("700x500")
        self.label = customtkinter.CTkLabel(self, text="Creat new record")
        self.label.pack(pady=20)
        self.close_button = customtkinter.CTkButton(self, text="Закрыть", command=self.close_window)
        self.close_button.pack(pady=10)

    def close_window(self):
        self.destroy()
        self.main_app.deiconify()
