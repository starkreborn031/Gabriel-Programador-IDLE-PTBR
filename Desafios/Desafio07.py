""" Primeiro, vamos definir os códigos em um arquivo chamado ansicolors.py. Depois, vou mostrar como você pode importá-lo e usá-lo em seus projetos.

Código da Biblioteca ansicolors.py """

# ansicolors.py

# Dicionário de cores do texto
text_colors = {
    "black": "30",
    "red": "31",
    "green": "32",
    "yellow": "33",
    "blue": "34",
    "magenta": "35",
    "cyan": "36",
    "white": "37",
    "bright_black": "90",
    "bright_red": "91",
    "bright_green": "92",
    "bright_yellow": "93",
    "bright_blue": "94",
    "bright_magenta": "95",
    "bright_cyan": "96",
    "bright_white": "97",
}

# Dicionário de cores de fundo
bg_colors = {
    "black": "40",
    "red": "41",
    "green": "42",
    "yellow": "43",
    "blue": "44",
    "magenta": "45",
    "cyan": "46",
    "white": "47",
    "bright_black": "100",
    "bright_red": "101",
    "bright_green": "102",
    "bright_yellow": "103",
    "bright_blue": "104",
    "bright_magenta": "105",
    "bright_cyan": "106",
    "bright_white": "107",
}

# Dicionário de estilos
styles = {
    "reset": "0",
    "bold": "1",
    "dim": "2",
    "italic": "3",
    "underline": "4",
    "blink": "5",
    "reverse": "7",
    "hidden": "8",
}

def colorize(text, color=None, bg_color=None, style=None):
    color_code = text_colors.get(color, "")
    bg_code = bg_colors.get(bg_color, "")
    style_code = styles.get(style, "")
    return f"\033[{style_code};{color_code};{bg_code}m{text}\033[0m"

def reset():
    return "\033[0m"

""" Como Usar a Biblioteca ansicolors.py em Seus Projetos
Aqui está como você pode importar e usar a ansicolors.py em outro arquivo Python: """

# main.py
from ansicolors import colorize, reset

# Usando a função colorize
print(colorize("Hello, World!", color="green"))
print(colorize("Aviso Importante!", color="yellow", style="bold"))
print(colorize("Erro Crítico!", color="red", bg_color="white", style="bold"))
print(colorize("Isso é um teste.", color="blue", style="underline"))

# Resetando manualmente (opcional se for a última linha)
print(reset())


#

""" 
Para usar a biblioteca ansicolors.py em seus projetos Python, siga estas etapas:

Crie um arquivo para a biblioteca:

Copie o código da ansicolors.py para um novo arquivo chamado, por exemplo, ansicolors.py.
Salve esse arquivo no mesmo diretório que o seu script principal ou em um local onde seja facilmente acessível pelos seus projetos.
Importe a biblioteca no seu script principal:

Em cada projeto onde você deseja usar as cores ANSI, importe a biblioteca no seu script principal. """

from ansicolors import colorize, reset

""" Use as funções da biblioteca:

Em seguida, você pode usar as funções colorize e reset conforme necessário para formatar o texto. """

# Exemplo de uso
print(colorize("Hello, World!", color="green"))
print(colorize("Aviso Importante!", color="yellow", style="bold"))
print(colorize("Erro Crítico!", color="red", bg_color="white", style="bold"))
print(colorize("Isso é um teste.", color="blue", style="underline"))

# Resetando manualmente (opcional se for a última linha)
print(reset())

""" Adapte conforme necessário:

Sinta-se à vontade para expandir ou personalizar a biblioteca conforme necessário para atender aos requisitos específicos de cada projeto. Adicione mais cores, estilos ou outras funcionalidades conforme apropriado.
Lembre-se dos requisitos do ambiente:

Tenha em mente que o suporte aos códigos de escape ANSI pode variar dependendo do ambiente. Em geral, eles funcionam bem em terminais Unix/Linux e no PowerShell do Windows 10/11, mas pode haver limitações em alguns ambientes Windows mais antigos ou em determinados editores de código/IDEs sem suporte adequado.
Ao seguir essas etapas, você poderá incorporar facilmente a biblioteca ansicolors.py em cada um dos seus projetos Python, melhorando a apresentação visual da saída do terminal de maneira consistente. """

