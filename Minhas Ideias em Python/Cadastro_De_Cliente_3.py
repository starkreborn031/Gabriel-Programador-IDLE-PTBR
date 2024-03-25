import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog
from datetime import datetime
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from tkcalendar import DateEntry
from ttkthemes import ThemedStyle  # Adicionando tema para a interface gráfica

class CadastroClientesApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Cadastro de Clientes")
        self.root.geometry("800x600")
        
        # Adicionando tema para a interface gráfica
        self.style = ThemedStyle(self.root)
        self.style.set_theme("arc")  # Escolhendo o tema 'arc'

        # Cabeçalho
        self.header_label = ttk.Label(self.root, text="STARK TECH MG", font=("Arial", 20, "bold"), padding=10)
        self.header_label.pack()

        # Número de pedido
        self.numero_pedido_label = ttk.Label(self.root, text="Número de Pedido:")
        self.numero_pedido_label.pack()
        self.numero_pedido_entry = ttk.Entry(self.root)
        self.numero_pedido_entry.pack()

        # Frame para os dados do cliente
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

        self.data_label = ttk.Label(self.cliente_frame, text="Data de Nascimento:")
        self.data_label.grid(row=2, column=0, padx=10, pady=5, sticky=tk.W)
        self.data_entry = DateEntry(self.cliente_frame, width=12, background='gray', foreground='white', borderwidth=2)
        self.data_entry.grid(row=2, column=1, padx=10, pady=5)

        self.endereco_label = ttk.Label(self.cliente_frame, text="Endereço:")
        self.endereco_label.grid(row=3, column=0, padx=10, pady=5, sticky=tk.W)
        self.endereco_entry = ttk.Entry(self.cliente_frame)
        self.endereco_entry.grid(row=3, column=1, padx=10, pady=5)

        # Botão para cadastrar cliente
        self.botao_cadastrar = ttk.Button(self.root, text="Cadastrar", command=self.cadastrar_cliente)
        self.botao_cadastrar.pack(pady=10)

    def cadastrar_cliente(self):
        numero_pedido = self.numero_pedido_entry.get()
        nome = self.nome_entry.get()
        cpf = self.cpf_entry.get()
        data_nascimento = self.data_entry.get()
        endereco = self.endereco_entry.get()

        # Validar se os campos obrigatórios estão preenchidos
        if not numero_pedido or not nome or not cpf or not data_nascimento or not endereco:
            messagebox.showwarning("Atenção", "Preencha todos os campos obrigatórios.")
            return

        # Gerar PDF com os dados do cliente
        dados_cliente = {
            'Número de Pedido': numero_pedido,
            'Nome': nome,
            'CPF': cpf,
            'Data de Nascimento': data_nascimento,
            'Endereço': endereco
        }

        self.gerar_pdf(dados_cliente)

    def gerar_pdf(self, dados_cliente):
        file_path = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF Files", "*.pdf")])

        if file_path:
            numero_registro = datetime.now().strftime("%Y%m%d%H%M%S")
            nome_arquivo = f"{file_path}-{numero_registro}.pdf"

            c = canvas.Canvas(nome_arquivo, pagesize=letter)
            c.drawString(100, 750, "STARK TECH MG - Cadastro de Cliente")
            c.drawString(100, 730, f"Número de Pedido: {dados_cliente['Número de Pedido']}")
            c.drawString(100, 710, f"Nome: {dados_cliente['Nome']}")
            c.drawString(100, 690, f"CPF: {dados_cliente['CPF']}")
            c.drawString(100, 670, f"Data de Nascimento: {dados_cliente['Data de Nascimento']}")
            c.drawString(100, 650, f"Endereço: {dados_cliente['Endereço']}")
            c.drawString(100, 630, "Data e Hora: " + datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
            c.drawString(100, 610, "Assinatura:")
            c.save()
            messagebox.showinfo("Sucesso", f"PDF gerado com sucesso: {nome_arquivo}")
        else:
            messagebox.showerror("Erro", "Nenhum arquivo selecionado para salvar.")

root = tk.Tk()
app = CadastroClientesApp(root)
root.mainloop()
