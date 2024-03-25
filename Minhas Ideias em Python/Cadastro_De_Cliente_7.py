import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from ttkthemes import ThemedStyle
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from datetime import datetime

class ProgramaCadastro:
    def __init__(self, root):
        self.root = root
        self.root.title("Cadastro de Clientes - STARK TECH MG")

    # Aplicando tema 'clam' aos widgets
        self.style = ThemedStyle(root)
        self.style.set_theme("clam")

        self.tabControl = ttk.Notebook(root)

    # Aba do Cliente
        
    # Adicione aqui as configurações dos widgets para a aba do Cliente
        self.cliente_frame = ttk.Frame(self.tabControl)
        self.tabControl.add(self.cliente_frame, text='Cliente')
        self.tabControl.pack(expand=1, fill="both")

        self.lbl_nome = ttk.Label(self.cliente_frame, text="Nome do Cliente:")
        self.lbl_nome.grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.entry_nome = ttk.Entry(self.cliente_frame)
        self.entry_nome.grid(row=0, column=1, padx=5, pady=5)

        self.lbl_cpf = ttk.Label(self.cliente_frame, text="CPF:")
        self.lbl_cpf.grid(row=1, column=0, padx=5, pady=5, sticky="w")
        self.entry_cpf = ttk.Entry(self.cliente_frame)
        self.entry_cpf.grid(row=1, column=1, padx=5, pady=5)

        self.lbl_endereco = ttk.Label(self.cliente_frame, text="Endereço:")
        self.lbl_endereco.grid(row=2, column=0, padx=5, pady=5, sticky="w")
        self.entry_endereco = ttk.Entry(self.cliente_frame)
        self.entry_endereco.grid(row=2, column=1, padx=5, pady=5)

        self.lbl_telefone = ttk.Label(self.cliente_frame, text="Telefone:")
        self.lbl_telefone.grid(row=3, column=0, padx=5, pady=5, sticky="w")
        self.entry_telefone = ttk.Entry(self.cliente_frame)
        self.entry_telefone.grid(row=3, column=1, padx=5, pady=5)

        self.lbl_data_entrada = ttk.Label(self.cliente_frame, text="Data de Entrada:")
        self.lbl_data_entrada.grid(row=4, column=0, padx=5, pady=5, sticky="w")
        self.entry_data_entrada = ttk.Entry(self.cliente_frame)
        self.entry_data_entrada.grid(row=4, column=1, padx=5, pady=5)
        
        self.lbl_data_prevista = ttk.Label(self.cliente_frame, text="Data Prevista:")
        self.lbl_data_prevista.grid(row=5, column=0, padx=5, pady=5, sticky="w")
        self.entry_data_prevista = ttk.Entry(self.cliente_frame)
        self.entry_data_prevista.grid(row=5, column=1, padx=5, pady=5)

        self.btn_cadastrar_cliente = ttk.Button(self.cliente_frame, text="Cadastrar Cliente", command=self.cadastrar_cliente)
        self.btn_cadastrar_cliente.grid(row=6, columnspan=2, pady=10)

    # Aba de Orçamento
        
    # Adicione aqui as configurações dos widgets para a aba de Orçamento
        self.orcamento_frame = ttk.Frame(self.tabControl)
        self.tabControl.add(self.orcamento_frame, text='Orçamento')

        self.lbl_valor_servicos = ttk.Label(self.orcamento_frame, text="Valor dos Serviços (R$):")
        self.lbl_valor_servicos.grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.entry_valor_servicos = ttk.Entry(self.orcamento_frame)
        self.entry_valor_servicos.grid(row=0, column=1, padx=5, pady=5)

        self.lbl_valor_pecas = ttk.Label(self.orcamento_frame, text="Valor das Peças (R$):")
        self.lbl_valor_pecas.grid(row=1, column=0, padx=5, pady=5, sticky="w")
        self.entry_valor_pecas = ttk.Entry(self.orcamento_frame)
        self.entry_valor_pecas.grid(row=1, column=1, padx=5, pady=5)

        self.lbl_descricao = ttk.Label(self.orcamento_frame, text="Descrição do Serviço:")
        self.lbl_descricao.grid(row=2, column=0, padx=5, pady=5, sticky="w")
        self.text_descricao = tk.Text(self.orcamento_frame, width=30, height=5)
        self.text_descricao.grid(row=2, column=1, padx=5, pady=5)

        self.lbl_desconto = ttk.Label(self.orcamento_frame, text="Desconto (%):")
        self.lbl_desconto.grid(row=3, column=0, padx=5, pady=5, sticky="w")
        self.entry_desconto = ttk.Entry(self.orcamento_frame)
        self.entry_desconto.grid(row=3, column=1, padx=5, pady=5)

        self.btn_criar_orcamento = ttk.Button(self.orcamento_frame, text="Criar Orçamento", command=self.criar_orcamento)
        self.btn_criar_orcamento.grid(row=4, columnspan=2, pady=10)

    # Aba do Dispositivo
       
    # Adicione aqui as configurações dos widgets para a aba do Dispositivo
        self.dispositivo_frame = ttk.Frame(self.tabControl)
        self.tabControl.add(self.dispositivo_frame, text='Dispositivo')

        self.lbl_descricao_dispositivo = ttk.Label(self.dispositivo_frame, text="Descrição do Dispositivo:")
        self.lbl_descricao_dispositivo.grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.text_descricao_dispositivo = tk.Text(self.dispositivo_frame, width=30, height=5)
        self.text_descricao_dispositivo.grid(row=0, column=1, padx=5, pady=5)

        self.lbl_placa_mae = ttk.Label(self.dispositivo_frame, text="Placa Mãe:")
        self.lbl_placa_mae.grid(row=1, column=0, padx=5, pady=5, sticky="w")
        self.entry_placa_mae = ttk.Entry(self.dispositivo_frame)
        self.entry_placa_mae.grid(row=1, column=1, padx=5, pady=5)

        self.lbl_placa_video = ttk.Label(self.dispositivo_frame, text="Placa de Vídeo:")
        self.lbl_placa_video.grid(row=2, column=0, padx=5, pady=5, sticky="w")
        self.entry_placa_video = ttk.Entry(self.dispositivo_frame)
        self.entry_placa_video.grid(row=2, column=1, padx=5, pady=5)

        self.lbl_processador = ttk.Label(self.dispositivo_frame, text="Processador:")
        self.lbl_processador.grid(row=3, column=0, padx=5, pady=5, sticky="w")
        self.entry_processador = ttk.Entry(self.dispositivo_frame)
        self.entry_processador.grid(row=3, column=1, padx=5, pady=5)

        self.lbl_memoria = ttk.Label(self.dispositivo_frame, text="Memória:")
        self.lbl_memoria.grid(row=4, column=0, padx=5, pady=5, sticky="w")
        self.entry_memoria = ttk.Entry(self.dispositivo_frame)
        self.entry_memoria.grid(row=4, column=1, padx=5, pady=5)

        self.lbl_fonte = ttk.Label(self.dispositivo_frame, text="Fonte:")
        self.lbl_fonte.grid(row=5, column=0, padx=5, pady=5, sticky="w")
        self.entry_fonte = ttk.Entry(self.dispositivo_frame)
        self.entry_fonte.grid(row=5, column=1, padx=5, pady=5)

        self.lbl_ssd = ttk.Label(self.dispositivo_frame, text="SSD:")
        self.lbl_ssd.grid(row=6, column=0, padx=5, pady=5, sticky="w")
        self.entry_ssd = ttk.Entry(self.dispositivo_frame)
        self.entry_ssd.grid(row=6, column=1, padx=5, pady=5)

        self.lbl_hdd = ttk.Label(self.dispositivo_frame, text="HDD:")
        self.lbl_hdd.grid(row=7, column=0, padx=5, pady=5, sticky="w")
        self.entry_hdd = ttk.Entry(self.dispositivo_frame)
        self.entry_hdd.grid(row=7, column=1, padx=5, pady=5)

        self.lbl_tipo_pc = ttk.Label(self.dispositivo_frame, text="Tipo de PC:")
        self.lbl_tipo_pc.grid(row=8, column=0, padx=5, pady=5, sticky="w")
        self.tipo_pc_var = tk.StringVar()
        self.tipo_pc_combobox = ttk.Combobox(self.dispositivo_frame, textvariable=self.tipo_pc_var, values=["PC Gamer", "PC Básico", "Notebook"])
        self.tipo_pc_combobox.grid(row=8, column=1, padx=5, pady=5)

        self.lbl_problema = ttk.Label(self.dispositivo_frame, text="Relato do Problema:")
        self.lbl_problema.grid(row=9, column=0, padx=5, pady=5, sticky="w")
        self.text_problema = tk.Text(self.dispositivo_frame, width=30, height=5)
        self.text_problema.grid(row=9, column=1, padx=5, pady=5)

        '''self.btn_cadastrar_dispositivo = ttk.Button(self.dispositivo_frame, text="Cadastrar Dispositivo", command=self.cadastrar_dispositivo)
        self.btn_cadastrar_dispositivo.grid(row=10, columnspan=2, pady=10)'''

    # Variáveis para armazenar os dados
        self.clientes = []
        self.numero_pedido = 1

        '''self.tabControl.bind("<ButtonRelease-1>", self.atualizar_pedido)'''

    def cadastrar_cliente(self):
        nome = self.entry_nome.get()
        cpf = self.entry_cpf.get()
        endereco = self.entry_endereco.get()
        telefone = self.entry_telefone.get()
        data_entrada = self.entry_data_entrada.get()
        data_prevista = self.entry_data_prevista.get()

        if nome and cpf and endereco and telefone and data_entrada and data_prevista:
            cliente = {
                'Nome': nome,
                'CPF': cpf,
                'Endereço': endereco,
                'Telefone': telefone,
                'Data de Entrada': data_entrada,
                'Data Prevista': data_prevista,
                'Número de Pedido': self.numero_pedido,
                'Data e Hora de Assinatura': datetime.now().strftime("%d/%m/%Y %H:%M:%S")
            }

            self.clientes.append(cliente)
            self.numero_pedido += 1

            messagebox.showinfo("Sucesso", "Cliente cadastrado com sucesso!")

        # Limpar os campos após o cadastro
            self.entry_nome.delete(0, tk.END)
            self.entry_cpf.delete(0, tk.END)
            self.entry_endereco.delete(0, tk.END)
            self.entry_telefone.delete(0, tk.END)
            self.entry_data_entrada.delete(0, tk.END)
            self.entry_data_prevista.delete(0, tk.END)
        else:
            messagebox.showwarning("Erro", "Por favor, preencha todos os campos.")

    def criar_orcamento(self):
        valor_servicos = self.entry_valor_servicos.get()
        valor_pecas = self.entry_valor_pecas.get()
        descricao = self.text_descricao.get("1.0", tk.END)
        desconto = self.entry_desconto.get()

        if valor_servicos and valor_pecas and descricao and desconto:
            orcamento = {
                'Valor dos Serviços (R$)': valor_servicos,
                'Valor das Peças (R$)': valor_pecas,
                'Descrição do Serviço': descricao,
                'Desconto (%)': desconto
            }

        # Aqui você pode adicionar o orçamento ao cliente atual ou a uma lista separada de orçamentos
        # Por exemplo:
        # cliente_atual['Orçamento'] = orcamento
        # Ou:
        # self.orcamentos.append(orcamento)

            messagebox.showinfo("Sucesso", "Orçamento criado com sucesso!")

        # Limpar os campos após criar o orçamento
            self.entry_valor_servicos.delete(0, tk.END)
            self.entry_valor_pecas.delete(0, tk.END)
            self.text_descricao.delete("1.0", tk.END)
            self.entry_desconto.delete(0, tk.END)
        else:
            messagebox.showwarning("Erro", "Por favor, preencha todos os campos do orçamento.")

    # Adicione aqui a lógica para criar o PDF
    def criar_pdf(self):
            cliente_atual = self.clientes[-1]  # Pega o último cliente cadastrado
            nome_cliente = cliente_atual['Nome']
            numero_pedido = cliente_atual['Número de Pedido']

            c = canvas.Canvas(f"{nome_cliente}_Pedido{numero_pedido}.pdf", pagesize=letter)

        # Cabeçalho do PDF
            c.setFont("Helvetica-Bold", 16)
            c.drawString(200, 750, "STARK TECH MG")
            c.setFont("Helvetica", 12)
            c.drawString(200, 730, "Cadastro de Cliente e Orçamento")

        # Informações do Cliente
            c.setFont("Helvetica-Bold", 14)
            c.drawString(100, 700, "Informações do Cliente:")
            c.setFont("Helvetica", 12)
            y_position = 680
            for key, value in cliente_atual.items():
                if key != 'Número de Pedido' and key != 'Data e Hora de Assinatura':
                    c.drawString(100, y_position, f"{key}: {value}")
                    y_position -= 20

        # Informações do Dispositivo
            c.setFont("Helvetica-Bold", 14)
            c.drawString(100, y_position - 40, "Informações do Dispositivo:")
            dispositivo = {
                'Descrição do Dispositivo': self.text_descricao_dispositivo.get("1.0", tk.END),
                'Placa Mãe': self.entry_placa_mae.get(),
                'Placa de Vídeo': self.entry_placa_video.get(),
                'Processador': self.entry_processador.get(),
                'Memória': self.entry_memoria.get(),
                'Fonte': self.entry_fonte.get(),
                'SSD': self.entry_ssd.get(),
                'HDD': self.entry_hdd.get(),
                'Tipo de Computador': self.combo_tipo_computador.get(),
                'Relato do Problema': self.text_problema.get("1.0", tk.END)
            }

            y_position -= 20
            for key, value in dispositivo.items():
                c.drawString(100, y_position, f"{key}: {value}")
                y_position -= 20

        # Informações do Orçamento
            c.setFont("Helvetica-Bold", 14)
            c.drawString(100, y_position - 40, "Orçamento:")
            orcamento = {
                'Valor dos Serviços (R$)': self.entry_valor_servicos.get(),
                'Valor das Peças (R$)': self.entry_valor_pecas.get(),
                'Descrição do Serviço': self.text_descricao.get("1.0", tk.END),
                'Desconto (%)': self.entry_desconto.get()
            }

            y_position -= 20
            for key, value in orcamento.items():
                c.drawString(100, y_position, f"{key}: {value}")
                y_position -= 20

        # Linha de assinatura
            c.line(100, 100, 500, 100)
            c.drawString(100, 80, "Assinatura do Técnico: _______________________")

            c.showPage()
            c.save()

            messagebox.showinfo("Sucesso", f"PDF criado com sucesso para {nome_cliente} (Pedido {numero_pedido})")

            def atualizar_pedido(self, event):
                self.numero_pedido = len(self.clientes) + 1

if __name__ == "__main__":
    root = tk.Tk()
    programa = ProgramaCadastro(root)
    root.mainloop()
