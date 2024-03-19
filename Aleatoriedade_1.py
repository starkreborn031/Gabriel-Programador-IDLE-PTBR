import tkinter as tk
from tkinter import ttk

# Função para calcular sucessor e antecessor
def calc_sucessor_antecessor():
    numero = int(entry_numero.get())
    label_resultado['text'] = f"Sucessor: {numero + 1}, Antecessor: {numero - 1}"

# Função para calcular dobro, triplo e raiz quadrada
def calc_dobro_triplo_raiz():
    numero = float(entry_numero_dt.get())
    label_resultado_dt['text'] = f"Dobro: {numero * 2}, Triplo: {numero * 3}, Raiz Quadrada: {numero ** 0.5}"

# Função para calcular a média das notas
def calc_media():
    notas = [float(entry_nota1.get()), float(entry_nota2.get()), float(entry_nota3.get())]
    label_resultado_media['text'] = f"Média: {sum(notas) / len(notas)}"

# Função para calcular área e tinta necessária
def calc_area_tinta():
    largura = float(entry_largura.get())
    altura = float(entry_altura.get())
    area = largura * altura
    tinta = area / 2
    label_resultado_area['text'] = f"Área: {area}m², Tinta Necessária: {tinta}L"

# Configuração da janela principal
root = tk.Tk()
root.title("Aplicativo Multifuncional")
root.geometry("800x800")

# Criação do notebook (abas)
notebook = ttk.Notebook(root)
notebook.pack(pady=10, expand=True)

# Aba de Sucessor e Antecessor
frame_sa = ttk.Frame(notebook, width=800, height=800)
frame_sa.pack(fill='both', expand=True)
notebook.add(frame_sa, text='Sucessor e Antecessor')

# Widgets para a aba de Sucessor e Antecessor
entry_numero = ttk.Entry(frame_sa)
entry_numero.pack(pady=20)
button_calcular_sa = ttk.Button(frame_sa, text="Calcular", command=calc_sucessor_antecessor)
button_calcular_sa.pack(pady=10)
label_resultado = ttk.Label(frame_sa, text="")
label_resultado.pack(pady=10)

# Aba de Dobro, Triplo e Raiz Quadrada
frame_dt = ttk.Frame(notebook, width=800, height=800)
frame_dt.pack(fill='both', expand=True)
notebook.add(frame_dt, text='Dobro, Triplo e Raiz')

# Widgets para a aba de Dobro, Triplo e Raiz Quadrada
entry_numero_dt = ttk.Entry(frame_dt)
entry_numero_dt.pack(pady=20)
button_calcular_dt = ttk.Button(frame_dt, text="Calcular", command=calc_dobro_triplo_raiz)
button_calcular_dt.pack(pady=10)
label_resultado_dt = ttk.Label(frame_dt, text="")
label_resultado_dt.pack(pady=10)

# Aba de Média das Notas
frame_media = ttk.Frame(notebook, width=800, height=800)
frame_media.pack(fill='both', expand=True)
notebook.add(frame_media, text='Média das Notas')

# Widgets para a aba de Média das Notas
entry_nota1 = ttk.Entry(frame_media)
entry_nota1.pack(pady=10)
entry_nota2 = ttk.Entry(frame_media)
entry_nota2.pack(pady=10)
entry_nota3 = ttk.Entry(frame_media)
entry_nota3.pack(pady=10)
button_calcular_media = ttk.Button(frame_media, text="Calcular Média", command=calc_media)
button_calcular_media.pack(pady=10)
label_resultado_media = ttk.Label(frame_media, text="")
label_resultado_media.pack(pady=10)

# Aba de Área e Tinta Necessária
frame_area = ttk.Frame(notebook, width=800, height=800)
frame_area.pack(fill='both', expand=True)
notebook.add(frame_area, text='Área e Tinta')

# Widgets para a aba de Área e Tinta Necessária
entry_largura = ttk.Entry(frame_area)
entry_largura.pack(pady=10)
entry_altura = ttk.Entry(frame_area)
entry_altura.pack(pady=10)
button_calcular_area = ttk.Button(frame_area, text="Calcular Área e Tinta", command=calc_area_tinta)
button_calcular_area.pack(pady=10)
label_resultado_area = ttk.Label(frame_area, text="")
label_resultado_area.pack(pady=10)

# Executa o aplicativo
root.mainloop()
