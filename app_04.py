#Formulario de inscrição - Sorteio de Natal
#Dados: Nome, Endereço, CPF, Telefone
'''CREATE TABLE pessoa (
    numero INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    endereco TEXT NOT NULL,
    cpf TEXT NOT NULL UNIQUE,
    telefone TEXT NOT NULL
);'''
import sqlite3
import tkinter as tk
from tkinter import messagebox
from random import randint

def noClique_Inscrever():
    nome = txtNome.get()
    endereco = txtEndereco.get()
    telefone = txtTelefone.get()
    cpf = txtCpf.get()

    if nome == '' or endereco == '' or telefone == '' or cpf == '':
        messagebox.showwarning("ERRO!", "Todos os campos são obrigatórios!")
    else:
        #Insere dados no Banco
        sql = f"INSERT INTO pessoa (nome, endereco, telefone, cpf) VALUES ('{nome}', '{endereco}', '{telefone}', '{cpf}')"
        cur.execute(sql)
        con.commit()

        #Apaga Entrada de Texto
        txtNome.delete(0, tk.END)
        txtEndereco.delete(0, tk.END)
        txtTelefone.delete(0, tk.END)
        txtCpf.delete(0, tk.END)

        #Mensagem de Texto Indicando o Cadastro
        messagebox.showinfo("Dados Cadastrados", "Candidato inscrito com sucesso!")

def noClique_Visualizar():
    cur.execute("SELECT * FROM pessoa")
    d = cur.fetchall()
    inscritos = ''

    for dados in d:
        dados = str(dados)
        dados = dados.split(',')
        aux = " | ".join(dados)
        inscritos += f'{aux}\n'

    lblInscritos.config(text="Inscritos: \n" + inscritos)

def noClique_Sortear():
    sql = f"select * from pessoa"
    cur.execute(sql)
    d = cur.fetchall()
    print(len(d))
    sortear = randint(1, len(d))
    sql = f"select * from pessoa where numero = {sortear}"
    cur.execute(sql)
    d = cur.fetchall()
    messagebox.showinfo("Sorteado", d)

janela = tk.Tk()
janela.title("App 04")
janela.geometry("400x500")

#Cria o banco de dados se ele não existir ou conecta-se nele
con = sqlite3.connect("forms.db")
cur = con.cursor()

#comando sql para criar a tabela. Executar primeiro
#cur.execute("CREATE TABLE pessoa(nome, enderco, cpf, telefone)")

lblInfo = tk.Label(janela, text="Formulário de Inscrição - Sorteio de Natal")
lblInfo.grid(column=0, row=0, columnspan=2)

lblNome = tk.Label(janela, text="*Nome: ")
lblNome.grid(column=0, row=1)
txtNome = tk.Entry(janela)
txtNome.grid(column=1, row=1, columnspan=2)

lblEndereco = tk.Label(janela, text="*Endereco: ")
lblEndereco.grid(column=0, row=2)
txtEndereco = tk.Entry(janela)
txtEndereco.grid(column=1, row=2, columnspan=2)

lblCpf = tk.Label(janela, text="*CPF: ")
lblCpf.grid(column=0, row=3)
txtCpf = tk.Entry(janela)
txtCpf.grid(column=1, row=3, columnspan=2)

lblTelefone = tk.Label(janela, text="*Telefone: ")
lblTelefone.grid(column=0, row=4)
txtTelefone = tk.Entry(janela)
txtTelefone.grid(column=1, row=4, columnspan=2)

btnInscrever = tk.Button(janela, text="Inscrever!", command=noClique_Inscrever)
btnInscrever.grid(column=0, row=5, columnspan=1)

btnVisualizarInscritos = tk.Button(janela, text="Verificar Inscritos!", command=noClique_Visualizar)
btnVisualizarInscritos.grid(column=1, row=5, columnspan=1)

lblInscritos = tk.Label(janela, text="Inscritos: \n")
lblInscritos.grid(column=0, row=6, columnspan=20)

btnSortear = tk.Button(janela, text="Sortear!", command=noClique_Sortear)
btnSortear.grid(column=2, row=5, columnspan=1)

janela.mainloop()