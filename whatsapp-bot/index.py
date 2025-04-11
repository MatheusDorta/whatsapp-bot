import tkinter as tk
from tkinter import filedialog, messagebox
import pandas as pd

#Função para carregar o arquivo Excel
def carregar_excel():
    arquivo_path = filedialog.askopenfilename(filetypes=[("Arquivos Excel", "*.xlsx;*.xls")])
    if arquivo_path:
        try:
            df = pd.read_excel(arquivo_path)
            if 'Número' in df.columns:
                lista_numeros.delete(0, tk.END) # Limpa a lista antes de adicionar novos números
                for numero in df['Número']:
                    lista_numeros.insert(tk.END, str(numero)) # Adiciona o número à lista
                messagebox.showinfo("Sucesso", "Números carregados com sucesso!")
            else:
                messagebox.showerror("Erro", "O arquivo não contém uma coluna 'Número'.")
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao carregar o arquivo: {e}")
            
# Criar Janela
janela = tk.Tk()
janela.title("Bot de WhatsApp - Importar Excel")
janela.geometry("400x300")

# Botão para importar Excel
btn_importar = tk.Button(janela, text="Importar Excel", command=carregar_excel)
btn_importar.pack(pady=10)

# Lista para exibir os números
lista_numeros = tk.Listbox(janela)
lista_numeros.pack(expand=True, fill=tk.BOTH, padx=10, pady=10)

#Rodar a Interface
janela.mainloop()
