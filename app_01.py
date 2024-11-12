import tkinter as tk
from tkinter import messagebox

def on_button_click():
    messagebox.showinfo("Mensagem", "Olá, mundo!")


janela = tk.Tk()
janela.title("App 01")
janela.geometry("300x200")


label = tk.Label(janela, text="Introdução - GUI!")
label.pack(pady=10)


button = tk.Button(janela, text="Clique em mim!", command=on_button_click)
button.pack(pady=10)

janela.mainloop()
