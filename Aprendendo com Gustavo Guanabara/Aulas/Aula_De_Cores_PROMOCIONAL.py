#   Aprendendo a usar cores no terminal Python
"""     Se você precisa usar cores específicas utilizando o padrão ANSI em Python, você pode utilizar sequências de escape para definir as cores. Veja um exemplo abaixo de como utilizar o padrão ANSI para imprimir o texto em uma cor específica: """

#   Imprime o texto em vermelho
print("\033[31mOlá, mundo!\033[0m")

"""     Neste exemplo, \033[31m define a cor vermelha e \033[0m retorna à cor padrão. Você pode substituir 31 por qualquer um dos seguintes códigos de cores ANSI: """

#   30: preto
#   31: vermelho
#   32: verde
#   33: amarelo
#   34: azul
#   35: magenta
#   36: ciano
#   37: branco

"""     Além disso, você pode usar os códigos de cores ANSI em combinação com a formatação de texto para estilizar o texto, como negrito, sublinhado, entre outros. Por exemplo: """

#   Imprime o texto em negrito e sublinhado
print("\033[1m\033[4mOlá, mundo!\033[0m")

"""     Neste exemplo, \033[1m define o texto em negrito e \033[4m define o texto como sublinhado. Utilize \033[0m para resetar as formatações e retornar ao formato padrão.


    Lembre-se de que nem todos os terminais e IDEs suportam completamente as sequências de escape ANSI, portanto, o resultado pode variar dependendo do ambiente onde seu código é executado. """


#
#


"""     Entendendo os Códigos de Escape ANSI
    Os códigos de escape ANSI são sequências de caracteres que começam com um escape (ESC ou \033) seguido por [, e então finalizados com um ou mais códigos numéricos separados por ;, terminando com m. Por exemplo, \033[31m mudará a cor do texto para vermelho.


Aqui está uma lista básica de alguns dos códigos de cores e estilos ANSI mais comuns:

    Reset: 0 (reseta a cor para o padrão)
    Negrito: 1

        Cores do texto:
    Preto: 30 Vermelho: 31 Verde: 32 Amarelo: 33 Azul: 34 Magenta: 35 Ciano: 36 Branco: 37

        Cores de fundo:
    Preto: 40 Vermelho: 41 Verde: 42 Amarelo: 43 Azul: 44 Magenta: 45 Ciano: 46 Branco: 47

        Como Usar
    Para usar esses códigos no Python, você simplesmente concatena eles com a sua string. Veja um exemplo básico: """

print("\033[31m" + "Texto em vermelho" + "\033[0m")

"""     Neste exemplo, \033[31m muda a cor do texto para vermelho, e \033[0m reseta a cor para o padrão do terminal.

     Criando Funções Auxiliares
    Para facilitar o uso e evitar a repetição de códigos, é uma boa ideia criar funções auxiliares: """

def color_text(text, color_code):
    return f"\033[{color_code}m{text}\033[0m"

print(color_text("Texto em vermelho", 31))
print(color_text("Texto em verde com negrito", "32;1"))

"""     Exemplo Avançado
    Você pode combinar vários estilos e cores: """

def colored(text, color=37, bg_color=40, style=0):
    return f"\033[{style};{color};{bg_color}m{text}\033[0m"

# Texto vermelho em negrito com fundo amarelo
print(colored("Alerta crítico!", 31, 43, 1))

""" Limitações
    
    Os códigos ANSI funcionam bem na maioria dos terminais Unix/Linux e no PowerShell do Windows 10/11, mas podem não funcionar em alguns ambientes Windows mais antigos ou em determinados editores de código/IDEs sem suporte adequado.

    A legibilidade pode variar dependendo das configurações de cor do terminal do usuário.
Com essas informações e exemplos, você deve ser capaz de começar a usar cores e estilos no terminal com seus programas Python, tornando-os visualmente mais informativos e agradáveis. """

# ____________________________________________________________________________________________________________________________________________________________________________________________________

print('Olá Mundo!')

#

print('\033[0;31;43 m Olá Mundo!')

#

print('\033[0;31;43m Olá Mundo! \033[m')

#

valor_a = 5
valor_b = 10
print('Os Valores são {} e {}.'.format(valor_a, valor_b))

#

valor_a = 5
valor_b = 10
print('Os Valores são \033[1;31;42m{}\033[m e \033[0;32;43m{}\033[m.'.format(valor_a, valor_b))

#

nome = 'Gabriel De Sousa Rocha'
print('Olá! Muito prazer em te conhecer, {}{}{}!!!'.format('\033[4;34m', nome, '\033[m'))

#

nome = 'Gabriel De Sousa Rocha'
cores = {'limpa':'\033[m',
        'azul':'\033[34m',
        'amarelo':'\033[33m'
        }
print('Olá! Muito prazer em te conhecer, {}{}{}!!!'.format(cores['amarelo'], nome, cores['azul']))

#

nome = 'Gabriel De Sousa Rocha'
cores = {
        'limpa':'\033[m',
        'azul':'\033[34m' '\33[m',
        'amarelo':'\033[33m' '\33[m'
        }
print('Olá! Muito prazer em te conhecer, {}{}{}!!!'.format(cores['amarelo'], nome, cores['azul']))

#