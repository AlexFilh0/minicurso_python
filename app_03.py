import tkinter as tk

def soma():
    num01 = int(entrada_numero01.get())
    num02 = int(entrada_numero02.get())
    soma = num01 + num02
    resultado.config(text=f"Resultado: {soma}")

def subt():
    num01 = int(entrada_numero01.get())
    num02 = int(entrada_numero02.get())
    subt = num01 - num02
    resultado.config(text=f"Resultado: {subt}")

def mult():
    num01 = int(entrada_numero01.get())
    num02 = int(entrada_numero02.get())
    mult = num01 * num02
    resultado.config(text=f"Resultado: {mult}")

def divs():
    num01 = int(entrada_numero01.get())
    num02 = int(entrada_numero02.get())
    divs = num01 / num02
    resultado.config(text=f"Resultado: {divs}")



janela = tk.Tk()
janela.title("App 03")
janela.geometry("200x200")



entrada_numero01 = tk.Entry(janela, width=6)
entrada_numero01.grid(row= 1, column= 1, pady = 1)

entrada_numero02 = tk.Entry(janela, width=6)
entrada_numero02.grid(row= 1, column= 2, pady = 1)


#Width é medida em largura de caracteres
#Height é medida em linhas de texto
button_soma = tk.Button(janela, text="+", width=6, height=2, command=soma)
button_soma.grid(row=3, column =1, columnspan= 1)

button_subtracao = tk.Button(janela, text="-", width=6, height=2, command=subt)
button_subtracao.grid(row=3, column= 2, columnspan = 1)

button_multiplicacao = tk.Button(janela, text="*", width=6, height=2, command=mult)
button_multiplicacao.grid(row=4, column= 1, columnspan = 1)

button_divisao = tk.Button(janela, text="/", width=6, height=2, command=divs)
button_divisao.grid(row=4, column= 2, columnspan= 1)

resultado = tk.Label(janela, text="Resultado: ")
resultado.grid(row= 5, column=1, columnspan= 20)


janela.mainloop()