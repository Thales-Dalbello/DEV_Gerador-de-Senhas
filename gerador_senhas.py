import tkinter as tk
from tkinter import messagebox
import string
import random
import re

def gerar_senha():
    tamanho = int(entry_tamanho.get())

    caracteres = ''
    if var_maiusculas.get():
        caracteres += string.ascii_uppercase
    if var_minusculas.get():
        caracteres += string.ascii_lowercase
    if var_numeros.get():
        caracteres += string.digits
    if var_simbolos.get():
        caracteres += string.punctuation

    if not caracteres:
        messagebox.showwarning("Atenção", "Selecione pelo menos um tipo de caractere.")
        return

    senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
    entry_resultado.delete(0, tk.END)
    entry_resultado.insert(0, senha)

    avaliacao = avaliar_forca(senha)
    label_forca.config(text=f"Força da senha: {avaliacao}")

    salvar_senha(senha)

def avaliar_forca(senha):
    criterios = [
        (r'[A-Z]', "Maiúscula"),
        (r'[a-z]', "Minúscula"),
        (r'[0-9]', "Número"),
        (r'[!@#$%^&*()_+\-=\[\]{};\'\\:"|<,./>?]', "Símbolo"),
    ]
    score = sum(1 for regex, _ in criterios if re.search(regex, senha))

    if len(senha) >= 12 and score == 4:
        return "Forte"
    elif len(senha) >= 8 and score >= 3:
        return "Média"
    else:
        return "Fraca"

def salvar_senha(senha):
    with open("senhas_salvas.txt", "a") as f:
        f.write(senha + "\n")

# Interface Gráfica
root = tk.Tk()
root.title("Gerador de Senhas Seguras")
root.geometry("400x350")
root.resizable(False, False)

frame = tk.Frame(root, padx=20, pady=20)
frame.pack()

tk.Label(frame, text="Tamanho da Senha:").pack()
entry_tamanho = tk.Entry(frame)
entry_tamanho.insert(0, "12")
entry_tamanho.pack()

var_maiusculas = tk.BooleanVar(value=True)
var_minusculas = tk.BooleanVar(value=True)
var_numeros = tk.BooleanVar(value=True)
var_simbolos = tk.BooleanVar(value=True)

tk.Checkbutton(frame, text="Incluir Letras Maiúsculas", variable=var_maiusculas).pack(anchor="w")
tk.Checkbutton(frame, text="Incluir Letras Minúsculas", variable=var_minusculas).pack(anchor="w")
tk.Checkbutton(frame, text="Incluir Números", variable=var_numeros).pack(anchor="w")
tk.Checkbutton(frame, text="Incluir Símbolos", variable=var_simbolos).pack(anchor="w")

tk.Button(frame, text="Gerar Senha", command=gerar_senha, bg="#4CAF50", fg="white").pack(pady=10)

entry_resultado = tk.Entry(frame, width=30, font=("Arial", 12))
entry_resultado.pack(pady=5)

label_forca = tk.Label(frame, text="", font=("Arial", 10, "bold"))
label_forca.pack()

root.mainloop()
