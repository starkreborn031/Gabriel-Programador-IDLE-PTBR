import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog
from datetime import datetime
import random
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from tkcalendar import DateEntry
from ttkthemes import ThemedStyle

class CadastroClientesApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Cadastro de Clientes")
        self.root.geometry("900x800")
        
    
        self.style = ThemedStyle(self.root)
        self.style.set_theme("arc")

        self.header_label = ttk.Label(self.root, text="STARK TECH MG", font=("Arial", 25, "bold"), padding=10)
        self.header_label.pack()
        
        self.abas = ttk.Notebook(self.root)
        self.abas.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)

        self.abas_clientes = ttk.Frame(self.abas)
        self.abas_orcamento = ttk.Frame(self.abas)

        self.abas.add(self.abas_clientes, text='Clientes')
        self.abas.add(self.abas_orcamento, text='Orçamento')

    # Widgets para a aba Clientes
        self.cliente_frame = ttk.LabelFrame(self.abas_clientes, text="Dados do Cliente")
        self.cliente_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)

        self.nome_label = ttk.Label(self.cliente_frame, text="Nome completo:")
        self.nome_label.grid(row=0, column=0, padx=10, pady=5, sticky=tk.W)
        self.nome_entry = ttk.Entry(self.cliente_frame)
        self.nome_entry.grid(row=0, column=1, padx=10, pady=5)

        self.cpf_label = ttk.Label(self.cliente_frame, text="CPF:")
        self.cpf_label.grid(row=1, column=0, padx=10, pady=5, sticky=tk.W)
        self.cpf_entry = ttk.Entry(self.cliente_frame)
        self.cpf_entry.grid(row=1, column=1, padx=10, pady=5)

        self.telefone_label = ttk.Label(self.cliente_frame, text="Telefone:")
        self.telefone_label.grid(row=2, column=0, padx=10, pady=5, sticky=tk.W)
        self.telefone_entry = ttk.Entry(self.cliente_frame)
        self.telefone_entry.grid(row=2, column=1, padx=10, pady=5)

        self.data_label = ttk.Label(self.cliente_frame, text="Data de Entrada OS:")
        self.data_label.grid(row=3, column=0, padx=10, pady=5, sticky=tk.W)
        self.data_entry = DateEntry(self.cliente_frame, width=12, background='gray', foreground='white', borderwidth=2, date_pattern='dd/mm/yyyy')
        self.data_entry.grid(row=3, column=1, padx=10, pady=5)

        self.endereco_label = ttk.Label(self.cliente_frame, text="Endereço:")
        self.endereco_label.grid(row=4, column=0, padx=10, pady=5, sticky=tk.W)
        self.endereco_entry = ttk.Entry(self.cliente_frame)
        self.endereco_entry.grid(row=4, column=1, padx=10, pady=5)

        self.telefone_label = ttk.Label(self.cliente_frame, text="Telefone:")
        self.telefone_label.grid(row=2, column=0, padx=10, pady=5, sticky=tk.W)
        self.telefone_entry = ttk.Entry(self.cliente_frame)
        self.telefone_entry.grid(row=2, column=1, padx=10, pady=5)

        self.data_label = ttk.Label(self.cliente_frame, text="Data de Nascimento:")
        self.data_label.grid(row=3, column=0, padx=10, pady=5, sticky=tk.W)
        self.data_entry = DateEntry(self.cliente_frame, width=12, background='gray', foreground='white', borderwidth=2, date_pattern='dd/mm/yyyy')
        self.data_entry.grid(row=3, column=1, padx=10, pady=5)

        self.endereco_label = ttk.Label(self.cliente_frame, text="Endereço:")
        self.endereco_label.grid(row=4, column=0, padx=10, pady=5, sticky=tk.W)
        self.endereco_entry = ttk.Entry(self.cliente_frame)
        self.endereco_entry.grid(row=4, column=1, padx=10, pady=5)

        self.computador_frame = ttk.LabelFrame(self.root, text="Dados do Computador/Notebook")
        self.computador_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)

        self.tipo_label = ttk.Label(self.computador_frame, text="Tipo de Computador:")
        self.tipo_label.grid(row=0, column=0, padx=10, pady=5, sticky=tk.W)
        self.tipo_combobox = ttk.Combobox(self.computador_frame, values=["PC GAMER", "PC BÁSICO", "NOTEBOOK"])
        self.tipo_combobox.grid(row=0, column=1, padx=10, pady=5)

        # Widgets para a aba Orçamento
        self.orcamento_frame = ttk.LabelFrame(self.abas_orcamento, text="Orçamento")
        self.orcamento_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)

        self.valor_label = ttk.Label(self.orcamento_frame, text="Valor:")
        self.valor_label.grid(row=0, column=0, padx=10, pady=5, sticky=tk.W)
        self.valor_entry = ttk.Entry(self.orcamento_frame)
        self.valor_entry.grid(row=0, column=1, padx=10, pady=5)

        self.desconto_label = ttk.Label(self.orcamento_frame, text="Desconto (%):")
        self.desconto_label.grid(row=1, column=0, padx=10, pady=5, sticky=tk.W)
        self.desconto_entry = ttk.Entry(self.orcamento_frame)
        self.desconto_entry.grid(row=1, column=1, padx=10, pady=5)

        self.observacao_label = ttk.Label(self.orcamento_frame, text="Observações:")
        self.observacao_label.grid(row=2, column=0, padx=10, pady=5, sticky=tk.W)
        self.observacao_entry = ttk.Entry(self.orcamento_frame, width=50)                           # Aumente a largura do campo
        self.observacao_entry.grid(row=2, column=1, padx=10, pady=5)

        self.pecas_frame = ttk.LabelFrame(self.computador_frame, text="Peças do Computador")
        self.pecas_frame.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky=tk.W+tk.E)

        self.placa_mae_label = ttk.Label(self.pecas_frame, text="Placa Mãe:")
        self.placa_mae_label.grid(row=0, column=0, padx=10, pady=5, sticky=tk.W)
        self.placa_mae_entry = ttk.Entry(self.pecas_frame)
        self.placa_mae_entry.grid(row=0, column=1, padx=10, pady=5)

        self.placa_video_label = ttk.Label(self.pecas_frame, text="Placa de Vídeo:")
        self.placa_video_label.grid(row=1, column=0, padx=10, pady=5, sticky=tk.W)
        self.placa_video_entry = ttk.Entry(self.pecas_frame)
        self.placa_video_entry.grid(row=1, column=1, padx=10, pady=5)

        self.processador_label = ttk.Label(self.pecas_frame, text="Processador:")
        self.processador_label.grid(row=2, column=0, padx=10, pady=5, sticky=tk.W)
        self.processador_entry = ttk.Entry(self.pecas_frame)
        self.processador_entry.grid(row=2, column=1, padx=10, pady=5)

        self.memoria_label = ttk.Label(self.pecas_frame, text="Memória:")
        self.memoria_label.grid(row=3, column=0, padx=10, pady=5, sticky=tk.W)
        self.memoria_entry = ttk.Entry(self.pecas_frame)
        self.memoria_entry.grid(row=3, column=1, padx=10, pady=5)

        self.fonte_label = ttk.Label(self.pecas_frame, text="Fonte:")
        self.fonte_label.grid(row=4, column=0, padx=10, pady=5, sticky=tk.W)
        self.fonte_entry = ttk.Entry(self.pecas_frame)
        self.fonte_entry.grid(row=4, column=1, padx=10, pady=5)

        self.ssd_label = ttk.Label(self.pecas_frame, text="SSD:")
        self.ssd_label.grid(row=5, column=0, padx=10, pady=5, sticky=tk.W)
        self.ssd_entry = ttk.Entry(self.pecas_frame)
        self.ssd_entry.grid(row=5, column=1, padx=10, pady=5)

        self.hdd_label = ttk.Label(self.pecas_frame, text="HDD:")
        self.hdd_label.grid(row=6, column=0, padx=10, pady=5, sticky=tk.W)
        self.hdd_entry = ttk.Entry(self.pecas_frame)
        self.hdd_entry.grid(row=6, column=1, padx=10, pady=5)

        self.botao_cadastrar = ttk.Button(self.root, text="Cadastrar", command=self.cadastrar_cliente)
        self.botao_cadastrar.pack(pady=10)        

    def cadastrar_cliente(self):
        nome = self.nome_entry.get()
        cpf = self.cpf_entry.get()
        telefone = self.telefone_entry.get()
        data_entrada_os = self.data_entry.get()
        endereco = self.endereco_entry.get()
        valor = self.valor_entry.get()
        desconto = self.desconto_entry.get()
        observacoes = self.observacao_entry.get()

        if not nome or not cpf or not telefone or not data_entrada_os or not endereco \
                or not valor or not desconto:
            messagebox.showwarning("Atenção", "Preencha todos os campos obrigatórios.")
            return

        numero_pedido = str(random.randint(10000, 99999))  # Gerar número de pedido aleatório

        dados_cliente = {
            'Número de Pedido': numero_pedido,
            'Nome': nome,
            'CPF': cpf,
            'Telefone': telefone,
            'Data de Entrada OS': data_entrada_os,
            'Endereço': endereco,
            'Valor': valor,
            'Desconto (%)': desconto,
            'Observações': observacoes
        }

        self.gerar_pdf(dados_cliente)

    def gerar_pdf(self, dados_cliente):
        file_path = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF Files", "*.pdf")])

        if file_path:
            nome_arquivo = f"{file_path}-{dados_cliente['Nome']}-{dados_cliente['Número de Pedido']}.pdf"

            c = canvas.Canvas(nome_arquivo, pagesize=letter)
            c.setFont("Helvetica", 10)

            c.drawString(100, 750, "STARK TECH MG - Cadastro de Cliente")
            c.drawString(100, 730, f"Número de Pedido: {dados_cliente['Número de Pedido']}")
            c.drawString(100, 730, f"Número de Pedido: {dados_cliente['Número de Pedido']}")
            c.drawString(100, 710, f"Nome: {dados_cliente['Nome']}")
            c.drawString(100, 690, f"CPF: {dados_cliente['CPF']}")
            c.drawString(100, 670, f"Telefone: {dados_cliente['Telefone']}")
            c.drawString(100, 650, f"Data de Entrada OS: {dados_cliente['Data de Entrada OS']}")
            c.drawString(100, 630, f"Endereço: {dados_cliente['Endereço']}")
            c.drawString(100, 610, f"Valor: R$ {dados_cliente['Valor']}")
            c.drawString(100, 590, f"Desconto (%): {dados_cliente['Desconto (%)']}")
            c.drawString(100, 570, f"Observações: {dados_cliente['Observações']}")
            
            c.line(100, 250, 500, 250)  # Linha para assinatura
            c.drawString(100, 230, "Assinatura do Cliente")

            data_hora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
            c.drawString(100, 210, f"Data e Hora: {data_hora}")

            c.save()

            messagebox.showinfo("Sucesso", f"PDF gerado com sucesso em: {nome_arquivo}")
        else:
            messagebox.showwarning("Atenção", "Nome do arquivo não especificado. PDF não foi gerado.")

if __name__ == "__main__":
    root = tk.Tk()
    app = CadastroClientesApp(root)
    root.mainloop()

