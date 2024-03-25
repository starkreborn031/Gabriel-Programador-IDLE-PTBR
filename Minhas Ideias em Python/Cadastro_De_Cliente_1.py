from datetime import datetime
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def cadastrar_cliente():
    nome = input("Digite o nome completo do cliente: ")
    cpf = input("Digite o CPF do cliente: ")
    data_nascimento = input("Digite a data de nascimento do cliente (DD/MM/AAAA): ")
    endereco = input("Digite o endereço do cliente: ")

    return {'nome': nome, 'cpf': cpf, 'data_nascimento': data_nascimento, 'endereco': endereco}

def cadastrar_computador():
    tipo_computador = input("Digite o tipo de computador (DESKTOP/NOTEBOOK/PC GAMER): ")
    # Suponha que cada tipo de computador tenha seus próprios campos específicos, você pode adaptar conforme necessário.
    # Por exemplo, para um desktop, você pode pedir informações como processador, memória RAM, etc.
    # Vou deixar isso como um exercício para você implementar.

def gerar_pdf(dados_cliente):
    numero_registro = datetime.now().strftime("%Y%m%d%H%M%S")
    nome_arquivo = f"cadastro_cliente_{numero_registro}.pdf"

    c = canvas.Canvas(nome_arquivo, pagesize=letter)
    c.drawString(100, 750, "Cadastro de Cliente")
    c.drawString(100, 730, f"Nome: {dados_cliente['nome']}")
    c.drawString(100, 710, f"CPF: {dados_cliente['cpf']}")
    c.drawString(100, 690, f"Data de Nascimento: {dados_cliente['data_nascimento']}")
    c.drawString(100, 670, f"Endereço: {dados_cliente['endereco']}")
    # Adicione aqui as informações do computador e outros campos conforme necessário
    c.drawString(100, 650, "Observações:")
    c.drawString(100, 630, "Data e Hora:")
    c.drawString(100, 610, "Assinatura:")
    c.drawString(100, 590, "Relato do Problema:")
    c.save()

    print(f"PDF gerado com sucesso: {nome_arquivo}")

def main():
    dados_cliente = cadastrar_cliente()
    cadastrar_computador()
    gerar_pdf(dados_cliente)

if __name__ == "__main__":
    main()
