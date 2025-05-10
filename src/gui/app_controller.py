import tkinter as tk
from gui.login_window import LoginWindow
from gui.dashboard_window import DashboardWindow

class AppController:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Assistant Agricole")
        self.root.geometry("400x300")
        self.current_frame = None

    def start(self):
        self.show_login()
        self.root.mainloop()

    def show_login(self):
        self._clear_frame()
        self.current_frame = LoginWindow(self.root, self)

    def show_dashboard(self, username):
        self._clear_frame()
        self.current_frame = DashboardWindow(self.root, self, username)

    def _clear_frame(self):
        if self.current_frame is not None:
            self.current_frame.destroy()
