import tkinter as tk

def on_buttonCliick():
    nome = entrada_de_texto.get()
    mensagem = "Seja Bem-Vindo " + nome
    frase.config(text = mensagem)


janela = tk.Tk()
janela.title("App 02")
janela.geometry("300x300")


label = tk.Label(janela, text="Escreva o seu nome: ")
label.pack(pady=10)

entrada_de_texto = tk.Entry(janela)
entrada_de_texto.pack(pady=10)

button = tk.Button(janela, text="Clique em mim", command=on_buttonCliick)
button.pack(pady = 10)

mensagem = ""

frase = tk.Label(janela)
frase.pack(pady = 10)

janela.mainloop()