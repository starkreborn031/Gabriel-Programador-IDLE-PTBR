import tkinter as tk
from tkinter import ttk, messagebox

class CalculadoraApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora Multifuncional")

        # Configurando o tamanho da janela para 800x800
        largura_janela = 800
        altura_janela = 800
        largura_tela = root.winfo_screenwidth()
        altura_tela = root.winfo_screenheight()

        pos_x = largura_tela // 2 - largura_janela // 2
        pos_y = altura_tela // 2 - altura_janela // 2

        self.root.geometry(f"{largura_janela}x{altura_janela}+{pos_x}+{pos_y}")

        self.tabControl = ttk.Notebook(root)

        self.aba_media = tk.Frame(self.tabControl)
        self.aba_tinta = tk.Frame(self.tabControl)
        self.aba_produtos = tk.Frame(self.tabControl)

        self.configurar_aba_media()
        self.configurar_aba_tinta()
        self.configurar_aba_produtos()

        self.tabControl.pack(expand=1, fill="both")

    def configurar_aba_media(self):
        tk.Label(self.aba_media, text="Calculadora de Média", font=('Arial', 14, 'bold')).pack(pady=10)
        self.nota1_entry = tk.Entry(self.aba_media, font=('Arial', 14))
        self.nota2_entry = tk.Entry(self.aba_media, font=('Arial', 14))
        self.nota3_entry = tk.Entry(self.aba_media, font=('Arial', 14))

        tk.Label(self.aba_media, text="Nota 1:", font=('Arial', 14)).pack(pady=5)
        self.nota1_entry.pack(pady=5)
        tk.Label(self.aba_media, text="Nota 2:", font=('Arial', 14)).pack(pady=5)
        self.nota2_entry.pack(pady=5)
        tk.Label(self.aba_media, text="Nota 3:", font=('Arial', 14)).pack(pady=5)
        self.nota3_entry.pack(pady=5)

        tk.Button(self.aba_media, text="Calcular Média", command=self.calcular_media, font=('Arial', 14, 'bold')).pack(pady=10)

        self.tabControl.add(self.aba_media, text="Média")

    def calcular_media(self):
        try:
            nota1 = float(self.nota1_entry.get())
            nota2 = float(self.nota2_entry.get())
            nota3 = float(self.nota3_entry.get())

            media = (nota1 + nota2 + nota3) / 3
            mensagem = f"A média das notas é: {media:.2f}"

            # Adiciona um Label com a resposta na aba correspondente
            tk.Label(self.aba_media, text=mensagem, font=('Arial', 14)).pack(pady=10)
        except ValueError:
            messagebox.showerror("Erro", "Por favor, insira valores numéricos para as notas.")

    def configurar_aba_tinta(self):
        tk.Label(self.aba_tinta, text="Calculadora de Tinta", font=('Arial', 14, 'bold')).pack(pady=10)
        self.largura_entry = tk.Entry(self.aba_tinta, font=('Arial', 14))
        self.altura_entry = tk.Entry(self.aba_tinta, font=('Arial', 14))

        tk.Label(self.aba_tinta, text="Largura (m):", font=('Arial', 14)).pack(pady=5)
        self.largura_entry.pack(pady=5)
        tk.Label(self.aba_tinta, text="Altura (m):", font=('Arial', 14)).pack(pady=5)
        self.altura_entry.pack(pady=5)

        tk.Button(self.aba_tinta, text="Calcular Tinta", command=self.calcular_tinta, font=('Arial', 14, 'bold')).pack(pady=10)

        self.tabControl.add(self.aba_tinta, text="Tinta")

    def calcular_tinta(self):
        try:
            largura = float(self.largura_entry.get())
            altura = float(self.altura_entry.get())

            area_parede = largura * altura
            quantidade_tinta = area_parede / 2

            mensagem = f"A área da parede é: {area_parede:.2f} metros quadrados\n"
            mensagem += f"Serão necessários {quantidade_tinta:.2f} litros de tinta para pintar a parede."

            # Adiciona um Label com a resposta na aba correspondente
            tk.Label(self.aba_tinta, text=mensagem, font=('Arial', 14)).pack(pady=10)
        except ValueError:
            messagebox.showerror("Erro", "Por favor, insira valores numéricos para largura e altura.")

    def configurar_aba_produtos(self):
        tk.Label(self.aba_produtos, text="Leitura de Produtos", font=('Arial', 14, 'bold')).pack(pady=10)

        # Inicializa uma lista para armazenar os produtos e seus preços
        self.produtos = []

        # Loop para receber os dados dos 5 produtos
        for i in range(5):
            frame_produto = tk.Frame(self.aba_produtos)
            frame_produto.pack(pady=5)

            tk.Label(frame_produto, text=f"Produto {i+1}", font=('Arial', 14)).pack(side=tk.LEFT)
            nome_produto_entry = tk.Entry(frame_produto, font=('Arial', 14))
            nome_produto_entry.pack(side=tk.LEFT, padx=5)

            tk.Label(frame_produto, text="Preço:", font=('Arial', 14)).pack(side=tk.LEFT)
            preco_produto_entry = tk.Entry(frame_produto, font=('Arial', 14))
            preco_produto_entry.pack(side=tk.LEFT, padx=5)

            self.produtos.append((nome_produto_entry, preco_produto_entry))

        tk.Button(self.aba_produtos, text="Calcular Desconto", command=self.calcular_desconto, font=('Arial', 14, 'bold')).pack(pady=10)

        self.tabControl.add(self.aba_produtos, text="Produtos")

    def calcular_desconto(self):
        desconto_percentual = 5
        for nome_produto_entry, preco_produto_entry in self.produtos:
            try:
                preco = float(preco_produto_entry.get())
                novo_preco = preco * (1 - desconto_percentual / 100)
                mensagem = f"Produto: {nome_produto_entry.get()}, Novo Preço: R${novo_preco:.2f}"

                # Adiciona um Label com a resposta na aba correspondente
                tk.Label(self.aba_produtos, text=mensagem, font=('Arial', 14)).pack(pady=10)
            except ValueError:
                messagebox.showerror("Erro", "Por favor, insira valores numéricos para os preços dos produtos.")

if __name__ == "__main__":
    root = tk.Tk()
    app = CalculadoraApp(root)
    root.mainloop()
