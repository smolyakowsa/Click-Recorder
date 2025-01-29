import customtkinter
from modules.recorder import EventRecorder

class CreateProject(customtkinter.CTkToplevel):
    def __init__(self, main_app):
        super().__init__()
        self.main_app = main_app
        self.title("Creat new record")
        self.geometry("700x500")
        self.recorder = EventRecorder()

        self.label = customtkinter.CTkLabel(self, text="Creat new record")
        self.label.pack(pady=20)

        self.close_button = customtkinter.CTkButton(self, text="Close",width=250, height=50,border_width = 0,
                                              corner_radius=10, command=self.close_window)
        self.close_button.place(relx=0.33, rely=0.8)

        self.record_button = customtkinter.CTkButton(self, text="Record", width=250, height=50, border_width=0,
                                                    corner_radius=10, command=self.record)
        self.record_button.place(relx=0.5, rely=0.3)

        self.swincher =customtkinter.CTkSwitch(self, text='1', width=250, height=50, border_width=0,
                                                    corner_radius=10)
        self.swincher.place(relx=0.2, rely=0.3)


    def close_window(self):
        self.destroy()
        self.main_app.deiconify()

    def record(self):
        self.withdraw()
        self.recorder.start_recording()
        self.deiconify()