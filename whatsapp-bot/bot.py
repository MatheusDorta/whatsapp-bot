import pandas as pd
import tkinter as tk
from tkinter import filedialog, messagebox
import pywhatkit as kit
import time

def importar_excel():
    arquivo = filedialog.askopenfilename(filetypes=[("Excel files", "*.xlsx;*.xls")])
    if not arquivo:
        return
    try:
        df = pd.read_excel(arquivo)
        if "Números" not in df.columns:
            messagebox.showerror("Erro", "O arquivo Excel deve conter uma coluna chamada 'Números'")
            return
        numeros = df["Números"].astype(str).tolist()
        lista_numeros.delete(0, tk.END)
        for num in numeros:
            lista_numeros.insert(tk.END, num)
        messagebox.showinfo("Sucesso", "Números carregados com sucesso!")
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao carregar o arquivo: {e}")

def enviar_mensagens():
    mensagem = campo_mensagem.get("1.0", tk.END).strip()
    if not mensagem:
        messagebox.showerror("Erro", "Digite uma mensagem para enviar!")
        return
    
    for i in range(lista_numeros.size()):
        numero = lista_numeros.get(i)
        try:
            kit.sendwhatmsg_instantly(f"+55{numero}", mensagem, wait_time=10)
            time.sleep(10)  # Evitar bloqueios do WhatsApp
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao enviar para {numero}: {e}")
    messagebox.showinfo("Sucesso", "Mensagens enviadas com sucesso!")

# Criando a interface
tela = tk.Tk()
tela.title("Bot de WhatsApp")
tela.geometry("400x500")

botao_importar = tk.Button(tela, text="Importar Excel", command=importar_excel)
botao_importar.pack()

lista_numeros = tk.Listbox(tela, height=10)
lista_numeros.pack(fill=tk.BOTH, expand=True)

tk.Label(tela, text="Mensagem:").pack()
campo_mensagem = tk.Text(tela, height=4)
campo_mensagem.pack(fill=tk.BOTH, expand=True)

botao_enviar = tk.Button(tela, text="Enviar Mensagens", command=enviar_mensagens, bg="green", fg="white")
botao_enviar.pack()

tela.mainloop()
