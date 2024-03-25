import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog
from datetime import datetime
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from tkcalendar import DateEntry
from ttkthemes import ThemedStyle

class CadastroClientesApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Cadastro de Clientes")
        self.root.geometry("800x700")
        
        self.style = ThemedStyle(self.root)
        self.style.set_theme("arc")

        self.header_label = ttk.Label(self.root, text="STARK TECH MG", font=("Arial", 20, "bold"), padding=10)
        self.header_label.pack()

        self.numero_pedido = datetime.now().strftime("%Y%m%d%H%M%S")  # Gerar número de pedido automaticamente

        self.numero_pedido_label = ttk.Label(self.root, text="Número de Pedido:")
        self.numero_pedido_label.pack()
        self.numero_pedido_entry = ttk.Entry(self.root, state='readonly')
        self.numero_pedido_entry.insert(0, self.numero_pedido)
        self.numero_pedido_entry.pack()

        self.cliente_frame = ttk.LabelFrame(self.root, text="Dados do Cliente")
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

        self.orcamento_frame = ttk.LabelFrame(self.root, text="Orçamento")
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
        self.observacao_entry = ttk.Entry(self.orcamento_frame)
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
        numero_pedido = self.numero_pedido_entry.get()
        nome = self.nome_entry.get()
        cpf = self.cpf_entry.get()
        telefone = self.telefone_entry.get()
        data_nascimento = self.data_entry.get()
        endereco = self.endereco_entry.get()
        tipo_computador = self.tipo_combobox.get()
        valor = self.valor_entry.get()
        desconto = self.desconto_entry.get()
        observacoes = self.observacao_entry.get()
        placa_mae = self.placa_mae_entry.get()
        placa_video = self.placa_video_entry.get()
        processador = self.processador_entry.get()
        memoria = self.memoria_entry.get()
        fonte = self.fonte_entry.get()
        ssd = self.ssd_entry.get()
        hdd = self.hdd_entry.get()

        if not numero_pedido or not nome or not cpf or not telefone or not data_nascimento or not endereco \
                or not tipo_computador or not valor or not desconto:
            messagebox.showwarning("Atenção", "Preencha todos os campos obrigatórios.")
            return

        dados_cliente = {
            'Número de Pedido': numero_pedido,
            'Nome': nome,
            'CPF': cpf,
            'Telefone': telefone,
            'Data de Nascimento': data_nascimento,
            'Endereço': endereco,
            'Tipo de Computador': tipo_computador,
            'Valor': valor,
            'Desconto (%)': desconto,
            'Observações': observacoes,
            'Placa Mãe': placa_mae,
            'Placa de Vídeo': placa_video,
            'Processador': processador,
            'Memória': memoria,
            'Fonte': fonte,
            'SSD': ssd,
            'HDD': hdd
        }

        self.gerar_pdf(dados_cliente)

    def gerar_pdf(self, dados_cliente):
        file_path = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF Files", "*.pdf")])

        if file_path:
            nome_arquivo = f"{file_path}-{dados_cliente['Nome']}-{dados_cliente['Número de Pedido']}.pdf"

            c = canvas.Canvas(nome_arquivo, pagesize=letter)
            c.drawString(100, 750, "STARK TECH MG - Cadastro de Cliente")
            c.drawString(100, 730, f"Número de Pedido: {dados_cliente['Número de Pedido']}")
            c.drawString(100, 710, f"Nome: {dados_cliente['Nome']}")
            c.drawString(100, 690, f"CPF: {dados_cliente['CPF']}")
            c.drawString(100, 670, f"Telefone: {dados_cliente['Telefone']}")
            c.drawString(100, 650, f"Data de Nascimento: {dados_cliente['Data de Nascimento']}")
            c.drawString(100, 630, f"Endereço: {dados_cliente['Endereço']}")
            c.drawString(100, 610, f"Tipo de Computador: {dados_cliente['Tipo de Computador']}")
            c.drawString(100, 590, f"Valor: R$ {dados_cliente['Valor']}")
            c.drawString(100, 570, f"Desconto: {dados_cliente['Desconto (%)']}%")
            c.drawString(100, 550, f"Observações: {dados_cliente['Observações']}")
            c.drawString(100, 530, "Peças do Computador:")
            c.drawString(100, 510, f"Placa Mãe: {dados_cliente['Placa Mãe']}")
            c.drawString(100, 490, f"Placa de Vídeo: {dados_cliente['Placa de Vídeo']}")
            c.drawString(100, 470, f"Processador: {dados_cliente['Processador']}")
            c.drawString(100, 450, f"Memória: {dados_cliente['Memória']}")
            c.drawString(100, 430, f"Fonte: {dados_cliente['Fonte']}")
            c.drawString(100, 410, f"SSD: {dados_cliente['SSD']}")
            c.drawString(100, 390, f"HDD: {dados_cliente['HDD']}")
            c.drawString(100, 370, "Data e Hora: " + datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
            c.drawString(100, 350, "Assinatura:")
            c.save()
            messagebox.showinfo("Sucesso", f"PDF gerado com sucesso: {nome_arquivo}")
        else:
            messagebox.showerror("Erro", "Nenhum arquivo selecionado para salvar.")

root = tk.Tk()
app = CadastroClientesApp(root)
root.mainloop()
