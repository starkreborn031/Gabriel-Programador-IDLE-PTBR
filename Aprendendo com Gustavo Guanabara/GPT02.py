import tkinter as tk
from tkinter import simpledialog, messagebox


def obter_entrada():
    root = tk.Tk()
    root.withdraw()  # Oculta a janela principal

    palavra = simpledialog.askstring("Entrada", "Digite uma palavra:")
    numero = simpledialog.askstring("Entrada", "Digite um número:")
    caractere = simpledialog.askstring("Entrada", "Digite um caractere especial:")

    return palavra, numero, caractere


def exibir_informacoes(palavra, numero, caractere):
    # Seu código de verificação aqui...

    # Exibindo informações usando messagebox
    mensagem = f"""
=== Informações sobre as entradas ===
Palavra: {palavra} - Tipo: {type(palavra)}
Número: {numero} - Tipo: {type(numero)}
Caractere: {caractere} - Tipo: {type(caractere)}
"""
    messagebox.showinfo("Informações", mensagem)

    # Adicione mais caixas de diálogo conforme necessário...


# Função principal
def main():
    root = tk.Tk()
    root.title("Verificador de Entradas")
    root.geometry("400x300")  # Tamanho da janela

    # Adicionando um rótulo
    label = tk.Label(root, text="Bem-vindo ao Verificador de Entradas", font=("Helvetica", 14))
    label.pack(pady=10)

    # Botão para iniciar o processo
    button = tk.Button(root, text="Iniciar", command=lambda: iniciar_processo(root))
    button.pack(pady=20)

    root.mainloop()


def iniciar_processo(root):
    palavra, numero, caractere = obter_entrada()
    exibir_informacoes(palavra, numero, caractere)
    root.destroy()  # Fechar a janela após exibir as informações


if __name__ == "__main__":
    main()
