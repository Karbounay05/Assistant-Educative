import tkinter as tk

class DashboardWindow(tk.Frame):
    def __init__(self, parent, controller, username):
        super().__init__(parent)
        self.controller = controller
        self.pack()

        tk.Label(self, text=f"Bienvenue {username} 👨‍🌾", font=("Arial", 14)).pack(pady=10)
        tk.Button(self, text="Déconnexion", command=self.logout).pack(pady=10)

    def logout(self):
        self.controller.show_login()
