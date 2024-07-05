import tkinter as tk
import pyperclip

def copiar_mensagem():
    opcao_selecionada = mensagem_listbox.get(tk.ACTIVE)
    
    if opcao_selecionada:
        nome = nome_entry.get().title()
        email = email_entry.get()
        
        if opcao_selecionada == "Primeiro Contato":
            mensagem = "Olá, *{}!* Sou o Danilo da QRPoint! Espero que esteja tudo bem.\n\nTivemos um cadastro no e-mail *{}* para testar o nosso sistema de controle de ponto.\n\nPosso ajudar?".format(nome, email)
        elif opcao_selecionada == "Acompanhamento":
            mensagem = "Olá, *{}!* Tudo bem? \n\nEstou entrando em contato para verificar se está precisando de ajuda com o QRPoint!".format(nome)
        elif opcao_selecionada == "Planos e Preços":
            mensagem = "Segue os valores disponíveis:\n\nDe 01 a 10 colaboradores (essencial): R$ 62,90;\nDe 01 a 10 colaboradores (completo): R$ 78,90;\nDe 11 a 25 colaboradores (completo): R$ 155,90;\nDe 26 a 50 colaboradores (completo): R$ 243,90;\nDe 51 a 100 colaboradores (completo): R$ 342,90;\nDe 101 a 300 colaboradores (completo): R$ 586,90;\nDe 301 a 600 colaboradores (completo): R$ 996,90;\nDe 601 a 1000 colaboradores (completo): R$ 1.771,90;\nDe 1001 a 3000 colaboradores (completo): R$ 2.342,90;".format()
        elif opcao_selecionada == "Fechar":
            mensagem = "Olá, *{}!* Tudo bem? \n\nEstou entrando em contato para verificar se possui interesse em dar contunidade ao QRPoint!".format(nome)
        # Adicione mais opções conforme necessário
        
        pyperclip.copy(mensagem)
        mensagem_copiada_label.config(text="A mensagem foi copiada para a área de transferência.")

# Cria uma janela Tkinter
root = tk.Tk()
root.title("Copiar Mensagem")

# Rótulos
nome_label = tk.Label(root, text="Nome:")
email_label = tk.Label(root, text="Email:")
mensagem_copiada_label = tk.Label(root, text="")

# Campos de entrada
nome_entry = tk.Entry(root)
email_entry = tk.Entry(root)

# Lista de mensagens
mensagem_listbox = tk.Listbox(root, selectmode=tk.SINGLE)
mensagens = ["Primeiro Contato", "Acompanhamento", "Planos e Preços", "Fechar"]  # Adicione mais opções conforme necessário
for mensagem in mensagens:
    mensagem_listbox.insert(tk.END, mensagem)

# Botão para copiar mensagem
copiar_button = tk.Button(root, text="Copiar Mensagem", command=copiar_mensagem)

# Layout dos widgets
nome_label.pack()
nome_entry.pack()
email_label.pack()
email_entry.pack()
mensagem_listbox.pack()
copiar_button.pack()
mensagem_copiada_label.pack()

root.mainloop()
