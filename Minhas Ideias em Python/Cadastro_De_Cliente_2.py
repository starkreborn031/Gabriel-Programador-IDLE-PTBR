import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog
from datetime import datetime
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

class CadastroClientesApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Cadastro de Clientes")
        self.root.geometry("600x400")

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
        self.data_entry = ttk.Entry(self.cliente_frame)
        self.data_entry.grid(row=2, column=1, padx=10, pady=5)

        self.endereco_label = ttk.Label(self.cliente_frame, text="Endereço:")
        self.endereco_label.grid(row=3, column=0, padx=10, pady=5, sticky=tk.W)
        self.endereco_entry = ttk.Entry(self.cliente_frame)
        self.endereco_entry.grid(row=3, column=1, padx=10, pady=5)

        self.computador_frame = ttk.LabelFrame(self.root, text="Dados do Computador")
        self.computador_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)

        self.tipo_label = ttk.Label(self.computador_frame, text="Tipo de Computador:")
        self.tipo_label.grid(row=0, column=0, padx=10, pady=5, sticky=tk.W)
        self.tipo_combobox = ttk.Combobox(self.computador_frame, values=["Desktop", "Notebook", "PC Gamer"])
        self.tipo_combobox.grid(row=0, column=1, padx=10, pady=5)

        self.obs_label = ttk.Label(self.computador_frame, text="Observações:")
        self.obs_label.grid(row=1, column=0, padx=10, pady=5, sticky=tk.W)
        self.obs_entry = ttk.Entry(self.computador_frame)
        self.obs_entry.grid(row=1, column=1, padx=10, pady=5)

        self.botao_cadastrar = ttk.Button(self.root, text="Cadastrar", command=self.cadastrar_cliente)
        self.botao_cadastrar.pack(pady=10)

    def cadastrar_cliente(self):
        nome = self.nome_entry.get()
        cpf = self.cpf_entry.get()
        data_nascimento = self.data_entry.get()
        endereco = self.endereco_entry.get()
        tipo_computador = self.tipo_combobox.get()
        observacoes = self.obs_entry.get()

        dados_cliente = {
            'nome': nome,
            'cpf': cpf,
            'data_nascimento': data_nascimento,
            'endereco': endereco,
            'tipo_computador': tipo_computador,
            'observacoes': observacoes
        }

        self.gerar_pdf(dados_cliente)

    def gerar_pdf(self, dados_cliente):
        # Solicita o local para salvar o PDF
        file_path = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF Files", "*.pdf")])

        if file_path:
            numero_registro = datetime.now().strftime("%Y%m%d%H%M%S")
            nome_arquivo = f"{file_path}-{numero_registro}.pdf"

            c = canvas.Canvas(nome_arquivo, pagesize=letter)
            c.drawString(100, 750, "Cadastro de Cliente")
            c.drawString(100, 730, f"Nome: {dados_cliente['nome']}")
            c.drawString(100, 710, f"CPF: {dados_cliente['cpf']}")
            c.drawString(100, 690, f"Data de Nascimento: {dados_cliente['data_nascimento']}")
            c.drawString(100, 670, f"Endereço: {dados_cliente['endereco']}")
            c.drawString(100, 650, f"Tipo de Computador: {dados_cliente['tipo_computador']}")
            c.drawString(100, 630, f"Observações: {dados_cliente['observacoes']}")
            # Adicione outros campos conforme necessário

            c.save()
            messagebox.showinfo("Sucesso", f"PDF gerado com sucesso: {nome_arquivo}")
        else:
            messagebox.showerror("Erro", "Nenhum arquivo selecionado para salvar.")

root = tk.Tk()
app = CadastroClientesApp(root)
root.mainloop()
