import tkinter as tk
from tkinter import messagebox, simpledialog
import subprocess

# Função para conectar-se ao dispositivo
def connect_to_device(device_info):
    ip_address = device_info['ip']
    username = username_entry.get()
    password = password_entry.get()

    if not username or not password:
        messagebox.showerror("Erro", "Por favor, insira o nome de usuário e a senha.")
        return

    try:
        # Verificar as credenciais de login
        ssh_command = f"ssh {username}@{ip_address} -o BatchMode=yes -o ConnectTimeout=10 -o StrictHostKeyChecking=no -o PasswordAuthentication=yes -o PubkeyAuthentication=no"
        full_command = f"echo {password} | {ssh_command}"
        process = subprocess.Popen(full_command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = process.communicate()

        if process.returncode != 0:
            if "Permission denied" in stderr.decode():
                messagebox.showerror("Erro", f"Erro de autenticação. Verifique as credenciais de login.")
            else:
                messagebox.showerror("Erro", f"Falha ao conectar-se ao dispositivo {ip_address}. Erro: {stderr.decode()}")
            return

        # Conexão bem-sucedida
        messagebox.showinfo("Conexão bem-sucedida", f"Conectado ao dispositivo {ip_address}")
        open_terminal_ssh(ip_address)
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao conectar-se ao dispositivo {ip_address}: {e}")

# Função para abrir um terminal SSH
def open_terminal_ssh(ip_address):
    try:
        subprocess.run(["ssh", f"{username_entry.get()}@{ip_address}"], timeout=10, check=True)
    except subprocess.TimeoutExpired:
        messagebox.showerror("Erro", f"Tempo limite de conexão excedido para {ip_address}")
    except subprocess.CalledProcessError as e:
        messagebox.showerror("Erro", f"Falha ao abrir o terminal SSH: {e}")

# Restante do seu código...

# Rodar a aplicação
window.mainloop()
