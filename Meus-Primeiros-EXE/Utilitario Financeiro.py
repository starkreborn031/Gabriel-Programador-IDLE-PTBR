import tkinter as tk
from tkinter import ttk

class AplicativoCompleto:
    def __init__(self, root):
        self.root = root
        self.root.title("Utilitário Completo")
        self.root.geometry("800x800")

        # Configurando a GUI
        self.tabControl = ttk.Notebook(root)

        # Adicionando abas
        self.adicionar_aba("Conversão de Unidades", self.pedido_unidades)
        self.adicionar_aba("Tabuada", self.pedido_tabuada)
        self.adicionar_aba("Conversão de Moeda", self.pedido_conversao_moeda)
        self.adicionar_aba("Descontos Salariais", self.pedido_descontos_salariais)

        # Exibindo a GUI
        self.tabControl.pack(expand=1, fill="both")

    def adicionar_aba(self, nome_aba, pedido_funcao):
        aba = ttk.Frame(self.tabControl)
        self.tabControl.add(aba, text=nome_aba)

        # Configuração para centralizar os widgets
        aba.columnconfigure(0, weight=1)
        aba.columnconfigure(1, weight=1)

        pedido_funcao(aba)

    def pedido_unidades(self, aba):
        tk.Label(aba, text="Digite a quantidade em quilômetros:", font=("Arial", 12, "bold")).grid(row=0, column=0, columnspan=2, pady=10)
        entry_km = tk.Entry(aba, font=("Arial", 12))
        entry_km.grid(row=1, column=0, columnspan=2, pady=10)

        def calcular_conversao():
            km = float(entry_km.get())
            metros = km * 1000
            centimetros = km * 100000
            milimetros = km * 1000000

            resultado_label.config(text=f"Em metros: {metros:.2f} m\nEm centímetros: {centimetros:.2f} cm\nEm milímetros: {milimetros:.2f} mm", font=("Arial", 12, "bold"))

        tk.Button(aba, text="Calcular", command=calcular_conversao, font=("Arial", 12, "bold")).grid(row=2, column=0, columnspan=2, pady=20)
        resultado_label = tk.Label(aba, text="", font=("Arial", 12))
        resultado_label.grid(row=3, column=0, columnspan=2)

    def pedido_tabuada(self, aba):
        tk.Label(aba, text="Digite um número para ver sua tabuada:", font=("Arial", 12, "bold")).grid(row=0, column=0, columnspan=2, pady=10)
        entry_numero = tk.Entry(aba, font=("Arial", 12))
        entry_numero.grid(row=1, column=0, columnspan=2, pady=10)

        def calcular_tabuada():
            numero = int(entry_numero.get())
            resultado = ""
            for i in range(1, 11):
                resultado += f"{numero} x {i} = {numero * i}\t|\t{numero} ÷ {i} = {numero / i:.2f}\n"

            resultado_label.config(text=resultado, font=("Arial", 12, "bold"))

        tk.Button(aba, text="Calcular", command=calcular_tabuada, font=("Arial", 12, "bold")).grid(row=2, column=0, columnspan=2, pady=20)
        resultado_label = tk.Label(aba, text="", font=("Arial", 12))
        resultado_label.grid(row=3, column=0, columnspan=2)

    def pedido_conversao_moeda(self, aba):
        tk.Label(aba, text="Digite a quantia de dinheiro em reais:", font=("Arial", 12, "bold")).grid(row=0, column=0, columnspan=2, pady=10)
        entry_reais = tk.Entry(aba, font=("Arial", 12))
        entry_reais.grid(row=1, column=0, columnspan=2, pady=10)

        def calcular_conversao_moeda():
            reais = float(entry_reais.get())
            cotacao_dolar = 3.27
            dolares = reais / cotacao_dolar

            resultado_label.config(text=f"Com R${reais:.2f}, você pode trocar por aproximadamente ${dolares:.2f}.", font=("Arial", 12, "bold"))

        tk.Button(aba, text="Calcular", command=calcular_conversao_moeda, font=("Arial", 12, "bold")).grid(row=2, column=0, columnspan=2, pady=20)
        resultado_label = tk.Label(aba, text="", font=("Arial", 12))
        resultado_label.grid(row=3, column=0, columnspan=2)

    def pedido_descontos_salariais(self, aba):
        tk.Label(aba, text="Digite o nome completo do funcionário:", font=("Arial", 12, "bold")).grid(row=0, column=0, pady=10)
        entry_nome = tk.Entry(aba, font=("Arial", 12))
        entry_nome.grid(row=0, column=1, pady=10)

        tk.Label(aba, text="Digite o salário bruto do funcionário:", font=("Arial", 12, "bold")).grid(row=1, column=0, pady=10)
        entry_salario = tk.Entry(aba, font=("Arial", 12))
        entry_salario.grid(row=1, column=1, pady=10)

        def calcular_descontos():
            nome_completo = entry_nome.get()
            salario_bruto = float(entry_salario.get())

            # Faixas de desconto de INSS
            faixas_inss = [(0, 1045.00, 0.075), (1045.01, 2089.60, 0.09), (2089.61, 3134.40, 0.12), (3134.41, 6101.06, 0.14)]

            # Calculando o desconto de INSS
            desconto_inss = 0
            for faixa in faixas_inss:
                if salario_bruto > faixa[0]:
                    desconto_inss += min(salario_bruto - faixa[0], faixa[1] - faixa[0] + 0.01) * faixa[2]

            # Faixas de desconto de Imposto de Renda
            faixas_ir = [(0, 1903.98, 0, 0), (1903.99, 2826.65, 0.075, 142.80),
                         (2826.66, 3751.05, 0.15, 354.80), (3751.06, 4664.68, 0.225, 636.13),
                         (4664.69, float('inf'), 0.275, 869.36)]

            # Calculando o desconto de Imposto de Renda
            base_calculo_ir = salario_bruto - desconto_inss
            desconto_ir = 0

            for faixa in faixas_ir:
                if base_calculo_ir > faixa[0]:
                    desconto_ir += (min(base_calculo_ir, faixa[1]) - faixa[0]) * faixa[2] - faixa[3]

            salario_liquido = salario_bruto - desconto_inss - desconto_ir

            # Mostrar resultados
            resultado_label.config(text=f"Nome: {nome_completo}\nSalário bruto: R${salario_bruto:.2f}\nDesconto INSS: R${desconto_inss:.2f}\nDesconto IR: R${desconto_ir:.2f}\nSalário líquido: R${salario_liquido:.2f}", font=("Arial", 12, "bold"))

        tk.Button(aba, text="Calcular Descontos", command=calcular_descontos, font=("Arial", 12, "bold")).grid(row=2, column=0, columnspan=2, pady=20)
        resultado_label = tk.Label(aba, text="", font=("Arial", 12))
        resultado_label.grid(row=3, column=0, columnspan=2)

if __name__ == "__main__":
    root = tk.Tk()
    app_completo = AplicativoCompleto(root)
    root.mainloop()

