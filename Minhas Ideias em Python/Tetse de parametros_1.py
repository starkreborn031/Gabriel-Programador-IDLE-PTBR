import nmap
import paramiko
import tkinter as tk
from tkinter import simpledialog
from subprocess import call

# Função para verificar dispositivos e portas
def verificar_dispositivos_e_portas(ip_range):
    nm = nmap.PortScanner()
    nm.scan(hosts=ip_range, arguments='-p 1-65535')

    dispositivos_portas = {}
    for host in nm.all_hosts():
        dispositivos_portas[host] = []
        for proto in nm[host].all_protocols():
            ports = nm[host][proto].keys()
            for port in ports:
                dispositivos_portas[host].append(port)

    return dispositivos_portas

# Função para conectar via SSH e abrir acesso remoto

def abrir_acesso_remoto(ip, porta, usuario, senha):
    try:
        # Comando para abrir a conexão remota via Área de Trabalho Remota do Windows
        call(['mstsc', f'/v:{ip}:{porta}', f'/u:{usuario}', f'/p:{senha}'])
        print("Conexão remota aberta com sucesso!")
    except Exception as e:
        print(f"Erro ao abrir conexão remota: {e}")

# Informe o range de IPs da sua rede (exemplo: 192.168.1.1/24)

ip_range = input("Informe o range de IPs da sua rede (exemplo: 192.168.1.1/24): ")
dispositivos_portas = verificar_dispositivos_e_portas(ip_range)
print("Dispositivos e portas disponíveis na rede:")
for dispositivo, portas in dispositivos_portas.items():
    print(f"Dispositivo: {dispositivo} - Portas: {', '.join(map(str, portas))}")

# Solicitar informações para conexão remota

ip_alvo = input("Informe o IP do dispositivo alvo: ")
porta_alvo = int(input("Informe a porta do dispositivo alvo: "))
usuario_alvo = input("Informe o usuário para acesso remoto: ")
senha_alvo = simpledialog.askstring("Senha", "Informe a senha para acesso remoto:")

abrir_acesso_remoto(ip_alvo, porta_alvo, usuario_alvo, senha_alvo)
