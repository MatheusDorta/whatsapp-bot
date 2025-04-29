# WhatsApp Bot

Este projeto é um bot para envio automatizado de mensagens no WhatsApp usando Python.

## 📌 Funcionalidades
- Envio de mensagens automáticas para uma lista de contatos.
- Leitura de contatos a partir de um arquivo Excel.
- Interface gráfica para facilitar a operação.

## 🛠️ Tecnologias Utilizadas
- Python 3.11+
- PyWhatKit (envio de mensagens)
- Pandas (leitura de arquivos Excel)
- Tkinter (interface gráfica)
- PyInstaller (geração de executável)

## 🚀 Instalação

1. Clone o repositório:
```bash
 git clone https://github.com/seu-usuario/whatsapp-bot.git
 cd whatsapp-bot
```

2. Crie um ambiente virtual e ative:
```bash
 python -m venv env
 env\Scripts\activate  # No Windows
```

3. Instale as dependências:
```bash
 pip install -r requirements.txt
```

## 📄 Como Usar
1. Execute o bot:
```bash
 python interface.py
```
2. Selecione o arquivo Excel com os contatos.
3. Pressione "Enviar" para iniciar o envio das mensagens.

## 🔧 Gerando o Executável
Para criar um executável do bot:
```bash
 pyinstaller --onefile --windowed interface.py
```
O arquivo final estará na pasta `dist/`.

## 📝 Contribuição
1. Faça um fork do repositório.
2. Crie um branch:
```bash
 git checkout -b minha-feature
```
3. Faça suas alterações e commit:
```bash
 git commit -m "Adicionei uma nova funcionalidade"
```
4. Envie as alterações:
```bash
 git push origin minha-feature
```
5. Abra um Pull Request.



