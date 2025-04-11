import tkinter as tk
from tkinter import filedialog
from bot import enviar_mensagens as enviar_do_bot  # Renomeando a função importada

def selecionar_arquivo():
    caminho = filedialog.askopenfilename()
    entrada_arquivo.delete(0, tk.END)  # Limpa o campo de entrada
    entrada_arquivo.insert(0, caminho)  # Insere o caminho do arquivo selecionado

def enviar_mensagens_interface():
    caminho = entrada_arquivo.get()
    if caminho:
        enviar_do_bot(caminho)  # Chamando a função correta

# Criando a interface
root = tk.Tk()
root.title("Bot WhatsApp")

entrada_arquivo = tk.Entry(root, width=50)
entrada_arquivo.pack(pady=10)

tk.Button(root, text="Selecionar Arquivo", command=selecionar_arquivo).pack(pady=5)
tk.Button(root, text="Enviar Mensagens", command=enviar_mensagens_interface).pack(pady=10)

root.mainloop()
