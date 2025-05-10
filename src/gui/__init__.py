import tkinter as tk
from tkinter import messagebox

def start_app():
    window = tk.Tk()
    window.title("Assistant Agricole")
    window.geometry("400x300")

    tk.Label(window, text="Bienvenue !", font=("Arial", 16)).pack(pady=10)

    def on_click():
        messagebox.showinfo("Info", "Bonjour cultivateur 👨‍🌾")

    tk.Button(window, text="Clique ici", command=on_click).pack(pady=10)

    window.mainloop()
