# Criar um aplicativo gráfico com várias abas, cada uma executando uma funcionalidade específica como descrito nos seus pedidos, requer o uso de uma biblioteca gráfica. No Python, uma das opções mais populares para isso é o tkinter. Abaixo está um exemplo básico de como criar um aplicativo com tkinter que contém três abas: uma para calcular a porção inteira de um número, outra para calcular a hipotenusa, e a terceira para sortear e exibir a ordem de apresentação dos alunos.

# Lembre-se, este é um exemplo básico. Para personalizar o layout e torná-lo mais bonito, você pode explorar mais opções de widgets e estilos disponíveis no tkinter.

import tkinter as tk
from tkinter import ttk
from math import trunc, hypot, radians, sin, cos, tan
from random import shuffle

# Função para calcular a porção inteira
def calcular_porcao_inteira():
    numero = float(entry_numero_real.get())
    resultado_inteiro.config(text=f'Porção inteira: {trunc(numero)}')

# Função para calcular a hipotenusa
def calcular_hipotenusa():
    oposto = float(entry_cateto_oposto.get())
    adjacente = float(entry_cateto_adjacente.get())
    resultado_hipotenusa.config(text=f'Hipotenusa: {hypot(oposto, adjacente):.2f}')

# Função para sortear a ordem de apresentação
def sortear_ordem():
    alunos = [entry_aluno1.get(), entry_aluno2.get(), entry_aluno3.get(), entry_aluno4.get()]
    shuffle(alunos)
    resultado_ordem.config(text='Ordem:\n' + '\n'.join(alunos))

# Criando a janela principal
app = tk.Tk()
app.title("App de Utilidades Escolares")
app.geometry("800x800")

# Configurando o notebook
notebook = ttk.Notebook(app)
notebook.pack(pady=10, expand=True)

# Criando as abas
aba_inteiro = ttk.Frame(notebook, width=800, height=780)
aba_hipotenusa = ttk.Frame(notebook, width=800, height=780)
aba_sorteio = ttk.Frame(notebook, width=800, height=780)

aba_inteiro.pack(fill='both', expand=True)
aba_hipotenusa.pack(fill='both', expand=True)
aba_sorteio.pack(fill='both', expand=True)

# Adicionando as abas ao notebook
notebook.add(aba_inteiro, text='Porção Inteira')
notebook.add(aba_hipotenusa, text='Hipotenusa')
notebook.add(aba_sorteio, text='Sorteio da Ordem')

# --- Aba da Porção Inteira ---
frame_inteiro = ttk.Frame(aba_inteiro)
frame_inteiro.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

tk.Label(frame_inteiro, text="Digite um número real:").pack()
entry_numero_real = tk.Entry(frame_inteiro)
entry_numero_real.pack()
tk.Button(frame_inteiro, text="Calcular", command=calcular_porcao_inteira).pack()
resultado_inteiro = tk.Label(frame_inteiro)
resultado_inteiro.pack()

# --- Aba da Hipotenusa ---
frame_hipotenusa = ttk.Frame(aba_hipotenusa)
frame_hipotenusa.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

tk.Label(frame_hipotenusa, text="Cateto oposto:").pack()
entry_cateto_oposto = tk.Entry(frame_hipotenusa)
entry_cateto_oposto.pack()
tk.Label(frame_hipotenusa, text="Cateto adjacente:").pack()
entry_cateto_adjacente = tk.Entry(frame_hipotenusa)
entry_cateto_adjacente.pack()
tk.Button(frame_hipotenusa, text="Calcular", command=calcular_hipotenusa).pack()
resultado_hipotenusa = tk.Label(frame_hipotenusa)
resultado_hipotenusa.pack()

# --- Aba do Sorteio ---
frame_sorteio = ttk.Frame(aba_sorteio)
frame_sorteio.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

tk.Label(frame_sorteio, text="Aluno 1:").pack()
entry_aluno1 = tk.Entry(frame_sorteio)
entry_aluno1.pack()
tk.Label(frame_sorteio, text="Aluno 2:").pack()
entry_aluno2 = tk.Entry(frame_sorteio)
entry_aluno2.pack()
tk.Label(frame_sorteio, text="Aluno 3:").pack()
entry_aluno3 = tk.Entry(frame_sorteio)
entry_aluno3.pack()
tk.Label(frame_sorteio, text="Aluno 4:").pack()
entry_aluno4 = tk.Entry(frame_sorteio)
entry_aluno4.pack()
tk.Button(frame_sorteio, text="Sortear Ordem", command=sortear_ordem).pack()
resultado_ordem = tk.Label(frame_sorteio)
resultado_ordem.pack()

app.mainloop()

# Este código cria um aplicativo GUI com tkinter que possui três abas diferentes para as funcionalidades solicitadas. Os elementos dentro de cada aba estão centralizados, e a janela tem um tamanho fixo de 800x800 pixels. Para tornar o layout mais bonito, você pode explorar opções como modificar as fontes, cores, adicionar padding aos widgets, e usar imagens ou ícones se necessário.