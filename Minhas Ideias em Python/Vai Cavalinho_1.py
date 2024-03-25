import os
import shutil
import tkinter as tk
from tkinter import filedialog

def choose_files():
    # Função para abrir uma janela para escolher arquivos
    root = tk.Tk()
    root.withdraw()
    files_to_copy = filedialog.askopenfilenames(title='Escolha os arquivos para copiar')
    return list(files_to_copy)

def choose_destination():
    # Função para abrir uma janela para escolher o diretório de destino
    root = tk.Tk()
    root.withdraw()
    destination_dir = filedialog.askdirectory(title='Escolha o diretório de destino')
    return destination_dir

def trojan():
    try:
        # Obtém os arquivos a serem copiados e o diretório de destino
        files_to_copy = choose_files()
        destination_dir = choose_destination()
        
        # Copia os arquivos para o diretório de destino
        for file_path in files_to_copy:
            file_name = os.path.basename(file_path)
            destination_path = os.path.join(destination_dir, file_name)
            shutil.copyfile(file_path, destination_path)
            print(f"Arquivo {file_name} copiado com sucesso para {destination_dir}")
        
        # Aqui poderiam ser incluídas outras ações maliciosas
        
    except Exception as e:
        print(f"Erro ao copiar os arquivos: {str(e)}")

def main():
    # Execute a função trojan() quando o programa for executado
    trojan()
    
    # Após a execução do código malicioso, o programa pode ter um comportamento benigno
    print("Programa funcionando normalmente...")
    
    # Aqui poderiam estar outras funcionalidades não maliciosas do programa

if __name__ == "__main__":
    main()
