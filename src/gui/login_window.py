import tkinter as tk

class LoginWindow(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.pack()

        tk.Label(self, text="Connexion", font=("Arial", 16)).pack(pady=10)

        self.username_entry = tk.Entry(self)
        self.username_entry.pack(pady=5)
        self.username_entry.insert(0, "Nom d'utilisateur")

        tk.Button(self, text="Se connecter", command=self.login).pack(pady=10)

    def login(self):
        username = self.username_entry.get()
        if username:
            self.controller.show_dashboard(username)
