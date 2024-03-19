import tkinter as tk
from tkinter import simpledialog, messagebox


def obter_entradas():
    root = tk.Tk()
    root.withdraw()  # Oculta a janela principal

    palavras = simpledialog.askstring("Entrada", "Digite palavras separadas por espaço:")
    numeros = simpledialog.askstring("Entrada", "Digite números separados por espaço:")
    caracteres = simpledialog.askstring("Entrada", "Digite caracteres separados por espaço:")

    palavras = palavras.split()
    numeros = numeros.split()
    caracteres = caracteres.split()

    return palavras, numeros, caracteres


def exibir_informacoes(palavras, numeros, caracteres):
    # Montando as informações para exibição
    informacoes = "=== Informações sobre as entradas ===\n"

    for palavra in palavras:
        e_verdadeira = palavra.isalpha()
        tipo_escrita = "Minúscula" if palavra.islower() else "Maiúscula" if palavra.isupper() else "Mista"
        informacoes += f"Palavra: {palavra}\n- É uma palavra válida: {e_verdadeira}\n- Tipo de Escrita: {tipo_escrita}\n"

    for numero in numeros:
        e_numero = numero.isdigit()
        e_decimal = numero.replace(".", "", 1).isdigit()
        informacoes += f"Número: {numero}\n- É um número válido: {e_numero}\n- É um número decimal: {e_decimal}\n"

    for caractere in caracteres:
        e_caractere_especial = len(caractere) == 1 and not caractere.isalnum()
        informacoes += f"Caractere: {caractere}\n- É um caractere especial válido: {e_caractere_especial}\n"

    # Exibindo informações usando messagebox
    messagebox.showinfo("Informações", informacoes)


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
    palavras, numeros, caracteres = obter_entradas()
    exibir_informacoes(palavras, numeros, caracteres)
    root.destroy()
    # Fechar a janela após exibir as informações


if __name__ == "__main__":
    main()
