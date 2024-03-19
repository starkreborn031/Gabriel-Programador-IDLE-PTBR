import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog
import subprocess
import os

# Função para conectar-se ao dispositivo
def connect_to_device(device_info):
    ip_address = device_info['ip']
    username = username_entry.get()
    password = password_entry.get()

    if not username or not password:
        messagebox.showerror("Erro", "Por favor, insira o nome de usuário e a senha.")
        return

    try:
        # Verificar se o dispositivo está acessível na rede
        response = os.system(f"ping -n 1 {ip_address} > nul")
        if response != 0:
            messagebox.showerror("Erro", "O dispositivo não está acessível na rede.")
            return

        # Verificar as credenciais de login
        ssh_command = f"ssh {username}@{ip_address} -o BatchMode=yes -o ConnectTimeout=10 -o StrictHostKeyChecking=no"
        process = subprocess.Popen(ssh_command, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        stdout, stderr = process.communicate(input=f"{password}\n".encode())
        
        if process.returncode != 0:
            messagebox.showerror("Erro", f"Falha ao conectar-se ao dispositivo {ip_address}. Verifique as credenciais de login.")
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

from scapy.all import ARP, Ether, srp

# Função para buscar dispositivos na rede
def scan_network(ip_range):
    arp = ARP(pdst=ip_range)
    ether = Ether(dst="ff:ff:ff:ff:ff:ff")
    packet = ether/arp
    result = srp(packet, timeout=3, verbose=0)[0]
    devices = [{'ip': received.psrc, 'mac': received.hwsrc} for _, received in result]
    return devices

# Função para iniciar a busca de dispositivos
def start_scan():
    ip_range = '192.168.1.1/24'  # Altere conforme necessário
    devices = scan_network(ip_range)
    update_device_list(devices)

# Função para atualizar a lista de dispositivos na interface gráfica
def update_device_list(devices):
    device_listbox.delete(0, tk.END)
    for device in devices:
        device_listbox.insert(tk.END, f"IP: {device['ip']} - MAC: {device['mac']}")

# Criar a janela principal da aplicação
window = tk.Tk()
window.title("Monitor de Rede")

# Botão para iniciar a busca de dispositivos
scan_button = tk.Button(window, text="Buscar Dispositivos", command=start_scan)
scan_button.pack()

# Lista de dispositivos encontrados na rede
device_listbox = tk.Listbox(window, width=50)
device_listbox.pack()

# Campos de entrada para nome de usuário e senha
username_label = tk.Label(window, text="Nome de Usuário:")
username_label.pack()
username_entry = tk.Entry(window)
username_entry.pack()

password_label = tk.Label(window, text="Senha:")
password_label.pack()
password_entry = tk.Entry(window, show="*")
password_entry.pack()

# Botão para conectar-se ao dispositivo selecionado na lista
connect_button = tk.Button(window, text="Conectar Dispositivo", command=lambda: connect_to_device(selected_device_info()))
connect_button.pack()

# Função para obter as informações do dispositivo selecionado na lista
def selected_device_info():
    selected_device_index = device_listbox.curselection()
    if selected_device_index:
        selected_device = device_listbox.get(selected_device_index[0])
        ip_address = selected_device.split()[1]
        return {'ip': ip_address}
    else:
        messagebox.showerror("Erro", "Selecione um dispositivo para se conectar.")
        return {}

# Rodar a aplicação
window.mainloop()
