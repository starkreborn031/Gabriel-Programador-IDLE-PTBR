# Comentários de linha única começam com um símbolo numérico.

""" 

Strings multilinhas podem ser escritas usando três "s e são frequentemente usadas como documentação. 

"""

'''
#####################################################
     1. Tipos de dados e operadores primitivos 
####################################################
'''


    # Você tem números 

3   # => 3


    # Matemática é o que você esperaria 1  +  1    # => 2 

8  -  1    # => 7 
10  *  2   # => 20 
35/5 #  => 7,0   
    
    
    # A divisão inteira arredonda para baixo para números positivos e negativos. 

5  //  3        # => 1 
- 5  //  3       # => -2 
5.0  //  3.0    # => 1.0 # funciona em carros alegóricos também 
- 5.0  //  3.0   # => -2.0

    

    # O resultado da divisão é sempre um float 

10,0  /  3   # => 3,3333333333333335


    
    # Operação módulo 

7  %  3    # => 1 

    
    # i% j tem o mesmo sinal que j, ao contrário de C 

- 7  %  3   # => 2



    # Exponenciação (x**y, x elevado à y-ésima potência) 

2 ** 3   # => 8



    # Imponha precedência com parênteses 

1  +  3  *  2     # => 7 
( 1  +  3 )  *  2   # => 8



    # Valores booleanos são primitivos (Nota: letras maiúsculas) 

True    # => True 
False   # => False



    # negar com not 

not  True    # => False 
not  False   # => True



    # Operadores Booleanos 
    # Observe que "e" e "ou" diferenciam maiúsculas de minúsculas 


True and False  # => False
False or True   # => True


    # Verdadeiro e Falso são na verdade 1 e 0, mas com palavras-chave diferentes 

True  +  True       # => 2 
True  *  8          # => 8 
False  -  5         # => -5



    # Os operadores de comparação observam o valor numérico de Verdadeiro e Falso 

0  ==  False        # => Verdadeiro 
2  >  True          # => Verdadeiro 
2  ==  True         # => Falso 
- 5  !=  False      # => Verdadeiro



    # None, 0 e strings/lists/dicts/tuples/sets vazios são avaliados como False. 
    # Todos os outros valores são True 

bool ( 0 )      # => False 
bool ( "" )     # => False 
bool ([])       # => False 
bool ({})       # => False 
bool (())       # => False 
bool ( set ())  # => Falso 
bool ( 4 )      # => Verdadeiro 
bool ( - 6 )    # => Verdadeiro



    # O uso de operadores lógicos booleanos em ints os converte em booleanos para avaliação, 
    # mas seu valor não convertido é retornado. Não confunda com bool(ints) e bit a bit 
    # e/ou (&,|) 

bool ( 0 )      # => False 
bool ( 2 )      # => True 
0  and  2       # => 0
bool ( - 5 )    # => Verdadeiro 
bool ( 2 )      # => Verdadeiro 
- 5  or  0      # => -5



    # Igualdade é == 

1  ==  1   # => Verdadeiro 
2  ==  1   # => Falso



    # A desigualdade é ! = 

1   !=  1   # => Falso 
2   !=  1   # => Verdadeiro



    # Mais comparações 

1  <  10   # => Verdadeiro 
1  >  10   # => Falso 
2  <=  2   # => Verdadeiro 
2  >=  2   # => Verdadeiro



    # Ver se um valor está em um intervalo 

1  <  2  and  2  <  3   # => Verdadeiro 
2  <  3  and  3  <  2   # => Falso 


    # O encadeamento faz com que isso pareça mais agradável 

1  <  2  <  3   # => Verdadeiro 
2  <  3  <  2   # => Falso

    
    
    # (is vs. ==) verifica se duas variáveis ​​se referem ao mesmo objeto, mas == verifica 
    # se os objetos apontados possuem os mesmos valores. 

a  =  [ 1 ,  2 ,  3 ,  4 ]          # Aponte a para uma nova lista, [1, 2, 3, 4] 
b  =  a                             # Aponte b para onde a está apontando 
b  and  a                           # => Verdadeiro, a e b refere-se ao mesmo objeto 
b  ==  a                            # => Verdadeiro, os objetos de a e b são iguais 
b  =  [ 1 ,  2 ,  3 ,  4 ]          # Aponte b em uma nova lista, [1, 2, 3, 4] 
b  and  a                           # => Falso, a e b não se referem ao mesmo objeto 
b  ==  a                            # => Verdadeiro, os objetos de a e b são iguais



    # Strings são criadas com " ou ' 

"Esta é uma string." 
'Esta também é uma string.'



    # Strings também podem ser adicionadas 

"Hello "  +  "world!"   # => "Olá, mundo!" 



    # Literais de string (mas não variáveis) podem ser concatenados sem usar '+' 

"Hello "  "world!"     # => "Olá, mundo!"



    # Uma string pode ser tratada como uma lista de caracteres 

"Olá, mundo!" [ 0 ]   # => 'H'



    # Você pode encontrar o comprimento de uma string 

len ( "This is a string" )   # => 16



    # Desde o Python 3.6, você pode usar strings f ou literais de string formatados. 

name  =  "Reiko" 
print ("Ela disse que seu nome é {name}.")      # => "Ela disse que o nome dela é Reiko" 



    # Qualquer expressão Python válida dentro dessas chaves é retornada para a string. 

print ("{nome} tem {len(nome)} caracteres.") # => "Reiko tem 5 caracteres."

    
    
    # Nenhum é um objeto 

None  # => Nenhum

    
    
    # Não use o símbolo de igualdade "==" para comparar objetos com None 
    # Use "is" em vez disso. Isso verifica a igualdade da identidade do objeto. 

"etc"  and  None   # => Falso 
None  and  None    # => Verdadeiro




'''
####################################################
 2. Variáveis e coleções 
####################################################
'''



    # Python tem uma função de impressão 

print ( "Eu sou Python. Prazer em conhecê-lo!" )   # => Eu sou Python. Prazer em conhecê-lo!

    
    
    # Por padrão, a função print também imprime uma nova linha no final. 
    # Use o argumento opcional end para alterar a string final. 

print ( "Olá, Mundo" ,  end = "!" )   # => Olá, Mundo!

    
    
    # Maneira simples de obter dados de entrada do console 

input_string_var  =  input ( "Insira alguns dados: " )  # Retorna os dados como uma string

    
    
    # Não há declarações, apenas atribuições. 
    # A convenção para nomear variáveis ​​é o estilo Snake_case 

some_var  =  5 
some_var   # => 5

    
    
    # Acessar uma variável não atribuída anteriormente é uma exceção. 
    # Consulte Control Flow para saber mais sobre tratamento de exceções. 

some_unknown_var  # Raises a NameError

    
    
    # if pode ser usado como uma expressão 
    # Equivalente ao operador ternário '?:' de C 

"yay!"  if  0  >  1  else  "não!"   # => "não!"



    # Lista sequências de armazenamento 

li  =  [] 



    # Você pode começar com uma lista pré-preenchida 

other_li  =  [ 4 ,  5 ,  6 ]

    
    
    # Adicione coisas ao final de uma lista com o acréscimo 

li . acrescentar ( 1 )      # li agora é [1] 
li . acrescentar ( 2 )      # li agora é [1, 2] 
li . acrescentar ( 4 )      # li agora é [1, 2, 4] 
li . anexar ( 3 )           # li agora é [1, 2, 4, 3] 



    # Remova do final com pop 

li . pop ()         # => 3 e li agora é [1, 2, 4] 



    # Vamos colocar de volta 

li . acrescentar ( 3 )     # li agora é [1, 2, 4, 3] novamente.



    # Acesse uma lista como faria com qualquer array 

li [ 0 ]    # => 1 



    # Veja o último elemento 

li [ - 1 ]   # => 3



    # Olhar para fora dos limites é um IndexError 

li [ 4 ]   # Gera um IndexError

    
    
    # Você pode visualizar intervalos com sintaxe de fatia. 
    # O índice inicial está incluído, o índice final não é 
    # (É um intervalo fechado/aberto para vocês, tipos matemáticos.) 

li [ 1 : 3 ]    # Lista de retorno do índice 1 a 3 => [2, 4] 
li [ 2 :]       # Retorna lista começando no índice 2 => [4, 3] 
li [: 3 ]       # Retorna lista do início até o índice 3 => [1, 2, 4] 
li [:: 2 ]      # Retorna lista selecionando elementos com um tamanho de passo de 2 => [1, 4] 
li [:: - 1 ]    # Retorna a lista na ordem inversa => [3, 4, 2, 1] 

    
    
    # Use qualquer combinação destes para criar fatias avançadas 
    # li[start :fim:etapa]



    # Faça uma cópia profunda de uma camada usando fatias 

li2  =  li [:]   # => li2 = [1, 2, 4, 3] mas (li2 é li) resultará em falso.

    
    
    # Remova elementos arbitrários de uma lista com "del" 

del  li [ 2 ]   # li agora é [1, 2, 3]



    # Remove a primeira ocorrência de um valor 

li . remove ( 2 )   # li agora é [1, 3] 
li . remove ( 2 )   # Gera um ValueError pois 2 não está na lista



    # Insira um elemento em um índice específico 

li . insert ( 1 ,  2 )   # li agora é [1, 2, 3] novamente

    
    # Obtenha o índice do primeiro item encontrado que corresponde ao argumento 

li . índice ( 2 )   # => 1 
li . index ( 4 )   # Gera um ValueError pois 4 não está na lista

    
    
    # Você pode adicionar listas 
    # Nota: os valores para li e para other_li não são modificados. 

li  +  other_li   # => [1, 2, 3, 4, 5, 6]



    # Concatena listas com "extend()" 

li . extend ( other_li )   # Agora li é [1, 2, 3, 4, 5, 6]

    
    
    # Verifica a existência em uma lista com "in" 

1  in  li   # => True

    
    
    # Examine o comprimento com "len()" 

len ( li )   # => 6


    
    
    # Tuplas são como listas, mas são imutáveis. 

tup  =  ( 1 ,  2 ,  3 ) 
tup [ 0 ]                   # => 1 
tup [ 0 ]  =  3             # Gera um TypeError



    # Observe que uma tupla de comprimento um deve ter uma vírgula após o último elemento, mas 
    # tuplas de outros comprimentos, mesmo zero, não. 

type (( 1 ))    # => <class 'int'> 
type (( 1 ,))   # => <class 'tuple'> 
type (())       # => <class 'tuple'>



    # Você também pode fazer a maioria das operações de lista em tuplas 

len ( tup )                 # => 3 
tup  +  ( 4 ,  5 ,  6 )     # => (1, 2, 3, 4, 5, 6) 
tup [: 2 ]                  # => (1, 2) 
2  and  tup                 # => Verdadeiro



    # Você pode descompactar tuplas (ou listas) em variáveis 

a,  b,  c  =  ( 1 ,  2 ,  3 )     # a agora é 1, b agora é 2 e c agora é 3 



    # Você também pode fazer descompactação estendida 

a ,  * b ,  c  =  ( 1 ,  2 ,  3 ,  4 )   # a agora é 1, b agora é [2, 3] e c agora é 4 

    
    
    # Tuplas são criadas por padrão se você deixar de fora os parênteses 

d ,  e ,  f  =  4 ,  5 ,  6   # a tupla 4, 5, 6 é descompactada nas variáveis ​​d, e e f 

    
    
    # respectivamente, de modo que d = 4, e = 5 e f = 6 
    # Agora veja como é fácil trocar dois valores 

e ,  d  =  d ,  e   # d agora é 5 e e agora é 4




    # Os dicionários armazenam mapeamentos de chaves para valores 

vazio_dict  =  {} 



    # Aqui está um dicionário pré-preenchido 

fill_dict  =  { "um" :  1 ,  "dois" :  2 ,  "três" :  3 }



    # As chaves de notas para dicionários devem ser de tipos imutáveis. Isso é para garantir que 
    # a chave possa ser convertida em um valor de hash constante para pesquisas rápidas. 
    # Tipos imutáveis ​​incluem ints, floats, strings, tuples. 

invalid_dict  =  {[ 1 , 2 , 3 ]:  "123" }               # => Produza um TypeError: unashable type: 'list' 
valid_dict  =  {( 1 , 2 , 3 ):[ 1 , 2 , 3 ]}            # Os valores podem ser de qualquer tipo, no entanto.


    
    
    # Procure valores com [] 

fill_dict [ "one" ]   # => 1

    
    
    
    # Obtenha todas as chaves como iteráveis ​​com "keys()". Precisamos encerrar a chamada em list() 
    # para transformá-la em uma lista. Falaremos sobre isso mais tarde. Nota - para version  
    # do Python <3.7, a ordem das chaves do dicionário não é garantida. Seus resultados podem 

    # não corresponder exatamente ao exemplo abaixo. No entanto, a partir do Python 3.7, 


    # not match the example below exactly. However, as of Python 3.7, dictionary
    # items maintain the order at which they are inserted into the dictionary.

list(filled_dict.keys())  # => ["three", "two", "one"] in Python <3.7
list(filled_dict.keys())  # => ["one", "two", "three"] in Python 3.7+




    # Get all values as an iterable with "values()". Once again we need to wrap it
    # in list() to get it out of the iterable. Note - Same as above regarding key

    # ordering.

list(filled_dict.values())  # => [3, 2, 1]  in Python <3.7
list(filled_dict.values())  # => [1, 2, 3] in Python 3.7+



    # Check for existence of keys in a dictionary with "in"

"one" in filled_dict  # => True
1 in filled_dict      # => False



    # Looking up a non-existing key is a KeyError

filled_dict["four"]  # KeyError



    # Use "get()" method to avoid the KeyError

filled_dict.get("one")      # => 1
filled_dict.get("four")     # => None



    # The get method supports a default argument when the value is missing

filled_dict.get("one", 4)   # => 1
filled_dict.get("four", 4)  # => 4




    # "setdefault()" inserts into a dictionary only if the given key isn't present

filled_dict.setdefault("five", 5)  # filled_dict["five"] is set to 5
filled_dict.setdefault("five", 6)  # filled_dict["five"] is still 5




    # Adding to a dictionary

filled_dict.update({"four":4})  # => {"one": 1, "two": 2, "three": 3, "four": 4}
filled_dict["four"] = 4         # another way to add to dict



    # Remove keys from a dictionary with del

del filled_dict["one"]  # Removes the key "one" from filled dict



    # From Python 3.5 you can also use the additional unpacking options

{'a': 1, **{'b': 2}}  # => {'a': 1, 'b': 2}
{'a': 1, **{'a': 2}}  # => {'a': 2}



    # Sets store ... well sets

empty_set = set()



    # Initialize a set with a bunch of values.

some_set = {1, 1, 2, 2, 3, 4}  # some_set is now {1, 2, 3, 4}



    # Similar to keys of a dictionary, elements of a set have to be immutable.

invalid_set = {[1], 1}  # => Raises a TypeError: unhashable type: 'list'
valid_set = {(1,), 1}



    # Add one more item to the set

filled_set = some_set
filled_set.add(5)  # filled_set is now {1, 2, 3, 4, 5}


    # Sets do not have duplicate elements

filled_set.add(5)  # it remains as before {1, 2, 3, 4, 5}



    # Do set intersection with &

other_set = {3, 4, 5, 6}
filled_set & other_set  # => {3, 4, 5}



    # Do set union with |

filled_set | other_set  # => {1, 2, 3, 4, 5, 6}



    # Do set difference with -

{1, 2, 3, 4} - {2, 3, 5}  # => {1, 4}



    # Do set symmetric difference with ^

{1, 2, 3, 4} ^ {2, 3, 5}  # => {1, 4, 5}



    # Check if set on the left is a superset of set on the right

{1, 2} >= {1, 2, 3} # => False



    # Check if set on the left is a subset of set on the right

{1, 2} <= {1, 2, 3} # => True



    # Check for existence in a set with in

2 in filled_set   # => True
10 in filled_set  # => False



    # Make a one layer deep copy

filled_set = some_set.copy()  # filled_set is {1, 2, 3, 4, 5}
filled_set is some_set        # => False



''' 
####################################################
            3. Fluxo de controle e iteráveis
#################################################### 
'''


    # Vamos apenas criar uma variável 

some_var  =  5


    # Aqui está uma instrução if. O recuo é significativo em Python! 
    # A convenção é usar quatro espaços, não tabulações. 
    # Isso imprime "some_var é menor que 10" 

if  some_var  >  10 : 
    print ( "some_var é totalmente maior que 10." ) 
elif  some_var  <  10 :     # Esta cláusula elif é opcional. 
    print ( "some_var é menor que 10." ) 
else :                   # Isso também é opcional. 
    print ( "some_var é de fato 10." )


""" 
Loops For iteram sobre impressões de listas: 
    cachorro é um mamífero 
    gato é um mamífero 
    mouse é um mamífero 
""" 


for  animal  in  [ "dog" ,  "cat" ,  "mouse" ]: 
    
    # Você pode usar format() para interpolar strings formatadas 
    print ( "{} é um mamífero" .formato ( animal ) )


""" 
"range(number)" retorna um iterável de números de zero até (mas excluindo) o número fornecido imprime: 
    0 
    1 
    2 
    3 
""" 

for  i  in  range ( 4 ): 
    print ( i )


""" 
"range(inferior, superior)" retorna um iterável de números do número inferior ao número superior impresso: 
    4 
    5 
    6 
    7 
""" 

for  i  in  range ( 4 ,  8 ): 
    print ( i )




''' 
"range(inferior, superior, passo)" retorna um iterável de números do número inferior ao número superior, enquanto incrementa por passo. Se o passo não for indicado, o valor padrão é 1. imprime: 4 6 '''

for  i  in  range ( 4 ,  8 ,  2 ): 
    print ( i )



# Faça um loop em uma lista para recuperar o índice e o valor de cada item da lista: 
'''     
        0 dog 
        1 cat 
        2 mouse
'''
 
animais  =  [ "dog" ,  "cat" ,  "mouse" ] 
for  i ,  valor  in  enumerate ( animais ): 
    print ( i ,  valor )




"""
While loops go until a condition is no longer met.
prints:
    0
    1
    2
    3
"""

x = 0
while x < 4:
    print(x)
    x += 1          # Shorthand for x = x + 1

    

    
    
    # Handle exceptions with a try/except block
try:
            # Use "raise" to raise an error
    raise IndexError("This is an index error")
except IndexError as e:
    pass                                        # Refrain from this, provide a recovery (next example).
except (TypeError, NameError):
    pass                                        # Multiple exceptions can be processed jointly.
else:                                           # Optional clause to the try/except block. Must follow
                                                # all except blocks.
    print("All good!")                          # Runs only if the code in try raises no exceptions
finally:                                        # Execute under all circumstances
    print("We can clean up resources here")




    
    # Instead of try/finally to cleanup resources you can use a with statement

with open("myfile.txt") as f:
    for line in f:
        print(line)




    # Writing to a file

contents = {"aa": 12, "bb": 21}
with open("myfile1.txt", "w+") as file:
    file.write(str(contents))        # writes a string to a file

import json
with open("myfile2.txt", "w+") as file:
    file.write(json.dumps(contents)) # writes an object to a file


    
    
    # Reading from a file

with open('myfile1.txt', "r+") as file:
    contents = file.read()           # reads a string from a file
print(contents)



    # print: {"aa": 12, "bb": 21}

with open('myfile2.txt', "r+") as file:
    contents = json.load(file)       # reads a json object from a file
print(contents)



    # print: {"aa": 12, "bb": 21}



    # Python oferece uma abstração fundamental chamada Iterable. 
    # Um iterável é um objeto que pode ser tratado como uma sequência. 
    # O objeto retornado pela função range é iterável.

filled_dict = {"one": 1, "two": 2, "three": 3}
our_iterable = filled_dict.keys()
print(our_iterable)                                 # => dict_keys(['one', 'two', 'three']). This is an object
                                                    # that implements our Iterable interface.

    # We can loop over it.



for i in our_iterable:
    print(i)            # Prints one, two, three




    # However we cannot address elements by index.

our_iterable[1]         # Raises a TypeError




    # An iterable is an object that knows how to create an iterator.

our_iterator = iter(our_iterable)



    # Our iterator is an object that can remember the state as we traverse through
    # it. We get the next object with "next()".

next(our_iterator)      # => "one"




    # It maintains state as we iterate.

next(our_iterator)      # => "two"
next(our_iterator)      # => "three"




    # After the iterator has returned all of its data, it raises a
    # StopIteration exception

next(our_iterator)      # Raises StopIteration




    # We can also loop over it, in fact, "for" does this implicitly!

our_iterator = iter(our_iterable)
for i in our_iterator:
    print(i)            # Prints one, two, three




    # You can grab all the elements of an iterable or iterator by call of list().

list(our_iterable)  # => Returns ["one", "two", "three"]
list(our_iterator)  # => Returns [] because state is saved



'''
################################################### 
                    4. Funções 
###################################################
'''



    # Use "def" para criar novas funções 

def  add ( x ,  y ): 
    print ( "x is {} and y is {}" . format ( x ,  y )) 
    return  x  +  y   # Retorna valores com uma instrução de retorno

    
    
    # Chamando funções com parâmetros 

add ( 5 ,  6 )   # => imprime "x é 5 e y é 6" e retorna 11

    
    
    # Outra maneira de chamar funções é com argumentos de palavras-chave 

add ( y = 6 ,  x = 5 )   # Argumentos de palavras-chave podem chegar em qualquer ordem.



    # Você pode definir funções que aceitam um número variável de 
    # argumentos posicionais 

def  varargs ( * args ): 
    return  args

varargs ( 1 ,  2 ,  3 )   # => (1, 2, 3)



    # Você pode definir funções que recebem um número variável de 
    # argumentos de palavras-chave, bem como 

def  keywords_args ( ** kwargs ): 
    return  kwargs



    # Vamos chamá-lo para ver o que acontece 

keywords_args ( big = "foot" ,  loch = "ness" )   # => {"big": "foot", "loch": "ness"}




    # Você pode fazer as duas coisas ao mesmo tempo, se quiser 

def  all_the_args ( * args ,  ** kwargs ): 
    print ( args ) 
    print ( kwargs )


"""
all_the_args(1, 2, a=3, b=4) prints:
    (1, 2)
    {"a": 3, "b": 4}
"""




    # Ao chamar funções, você pode fazer o oposto de args/kwargs! 
    # Use * para expandir args (tuplas) e use ** para expandir kwargs (dicionários). 

args  =  ( 1 ,  2 ,  3 ,  4 ) 
kwargs  =  { "a" :  3 ,  "b" :  4 } 

all_the_args ( * args )             # equivalente: all_the_args(1, 2, 3, 4) 
all_the_args ( ** kwargs )          # equivalente: all_the_args(a=3, b=4) 
all_the_args ( * args ,  ** kwargs )   # equivalente: all_the_args(1, 2, 3, 4, a=3, b=4)

    
    
    
    # Retornando vários valores (com atribuições de tupla) 

def  swap ( x ,  y ): 
    return  y ,  x      # Retorna vários valores como uma tupla sem parênteses. 
                        # (Nota: os parênteses foram excluídos, mas podem ser incluídos)

x  =  1 
y  =  2 
x ,  y  =  swap ( x ,  y )      # => x = 2, y = 1 

    # (x, y) = swap(x,y) # Novamente o uso de parênteses é opcional.




    # escopo global 

x  =  5

def  set_x ( num ): 
    # o escopo local começa aqui 
    # local var x não é o mesmo que global var x 
    x  =  num     # => 43 
    print ( x )    # => 43

def  set_global_x ( num ): 
    # global indica que determinada var reside no escopo global 
    global  x 
    print ( x )    # => 5 
    x  =  num     # global var x agora está definido como 6 
    print ( x )    # => 6

set_x ( 43 ) 
set_global_x ( 6 ) 


""" 
    imprime: 
            43 
            5 
            6 
"""



    # Python tem funções de primeira classe 

def  create_adder ( x ): 
    def  adder ( y ): 
        return  x  +  y 
    return  adder

add_10  =  create_adder ( 10 ) 
add_10 ( 3 )    # => 13




    # Closures in nested functions:
    # We can use the nonlocal keyword to work with variables in nested scope which shouldn't be declared in the inner functions.

def create_avg():
    total = 0
    count = 0
    def avg(n):
        nonlocal total, count
        total += n
        count += 1
        return total/count
    return avg

avg = create_avg()
avg(3) # => 3.0
avg(5) # (3+5)/2 => 4.0
avg(7) # (8+7)/3 => 5.0





    # Existem também funções anônimas 

( lambda  x :  x  >  2 )( 3 )                           # => True 
( lambda  x ,  y :  x  **  2  +  y  **  2 )( 2 ,  1 )   # => 5





    # Existem listas de funções de ordem superior integradas ( map ( add_10 ,  [ 1 ,  2 ,  3 ]))           
    # => [11, 12, 13] 

list ( map ( max ,  [ 1 ,  2 ,  3 ],  [ 4 ,  2 ,  1 ]))             # => [4, 2, 3]
list ( map ( lambda  x :  x  >  5 ,  [ 3 ,  4 ,  5 ,  6 ,  7 ]))    # => [6, 7]




    # Podemos usar compreensões de lista para bons mapas e filtros. 
    # A compreensão de lista armazena a saída como uma lista (que pode ser aninhada). 

[add_10(i) for i in [1, 2, 3]]         # => [11, 12, 13]
[x for x in [3, 4, 5, 6, 7] if x > 5]  # => [6, 7]




    # Você também pode construir compreensões de conjunto e ditado. 

{x for x in 'abcddeef' if x not in 'abc'}  # => {'d', 'e', 'f'}
{x: x**2 for x in range(5)}  # => {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}


'''
####################################################
                 5. Modules
####################################################
'''


    # You can import modules

import math
print(math.sqrt(16))  # => 4.0



    # You can get specific functions from a module

from math import ceil, floor
print(ceil(3.7))   # => 4
print(floor(3.7))  # => 3

    
    
    # You can import all functions from a module.
    # Warning: this is not recommended

from math import *




    # You can shorten module names

import math as m
math.sqrt(16) == m.sqrt(16)  # => True

    
    
    
    # Python modules are just ordinary Python files. You
    # can write your own, and import them. The name of the
    # module is the same as the name of the file.

    # You can find out which functions and attributes
    # are defined in a module.

import math
dir(math)

    
    
    
    # If you have a Python script named math.py in the same
    # folder as your current script, the file math.py will
    # be loaded instead of the built-in Python module.
    # This happens because the local folder has priority
    # over Python's built-in libraries.




'''
####################################################
                 6. Classes
####################################################
'''



    # We use the "class" statement to create a class

class Human:

    # A class attribute. It is shared by all instances of this class
    species = "H. sapiens"

    # Basic initializer, this is called when this class is instantiated.
    # Note that the double leading and trailing underscores denote objects
    # or attributes that are used by Python but that live in user-controlled
    # namespaces. Methods(or objects or attributes) like: __init__, __str__,
    # __repr__ etc. are called special methods (or sometimes called dunder
    # methods). You should not invent such names on your own.
    
    def __init__(self, name):
        # Assign the argument to the instance's name attribute
        self.name = name
        # Initialize property
        self._age = 0           # the leading underscore indicates the "age" property is 
                                # intended to be used internally
                                # do not rely on this to be enforced: it's a hint to other devs

    
    # An instance method. All methods take "self" as the first argument
    def say(self, msg):
        print("{name}: {message}".format(name=self.name, message=msg))


    # Another instance method
    def sing(self):
        return 'yo... yo... microphone check... one two... one two...'


    # A class method is shared among all instances
    # They are called with the calling class as the first argument

    @classmethod
    def get_species(cls):
        return cls.species



    # A static method is called without a class or instance reference

    @staticmethod
    def grunt():
        return "*grunt*"




    # A property is just like a getter.
    # It turns the method age() into a read-only attribute of the same name.
    # There's no need to write trivial getters and setters in Python, though.

    @property
    def age(self):
        return self._age




    # This allows the property to be set

    @age.setter
    def age(self, age):
        self._age = age




    # This allows the property to be deleted

    @age.deleter
    def age(self):
        del self._age


    
    
    # When a Python interpreter reads a source file it executes all its code.
    # This __name__ check makes sure this code block is only executed when this
    # module is the main program.

if __name__ == '__main__':
    
    # Instantiate a class
    i = Human(name="Ian")
    i.say("hi")                     # "Ian: hi"
    j = Human("Joel")
    j.say("hello")                  # "Joel: hello"
                # i and j are instances of type Human; i.e., they are Human objects.

    # Call our class method
    
    i.say(i.get_species())          # "Ian: H. sapiens"
    
    # Change the shared attribute
    
    Human.species = "H. neanderthalensis"
    i.say(i.get_species())          # => "Ian: H. neanderthalensis"
    j.say(j.get_species())          # => "Joel: H. neanderthalensis"

    
    # Call the static method
    
    print(Human.grunt())            # => "*grunt*"

    # Static methods can be called by instances too
    
    print(i.grunt())                # => "*grunt*"

    # Update the property for this instance
    
    i.age = 42
    
    # Get the property
    
    i.say(i.age)                    # => "Ian: 42"
    j.say(j.age)                    # => "Joel: 0"
    # Delete the property
    del i.age
    # i.age                         # => this would raise an AttributeError


'''
####################################################
                 6.1 Inheritance
####################################################
'''



    # Inheritance allows new child classes to be defined that inherit methods and
    # variables from their parent class.

    # Using the Human class defined above as the base or parent class, we can
    # define a child class, Superhero, which inherits the class variables like
    # "species", "name", and "age", as well as methods, like "sing" and "grunt"
    # from the Human class, but can also have its own unique properties.

    # To take advantage of modularization by file you could place the classes above
    # in their own files, say, human.py

    # To import functions from other files use the following format
    # from "filename-without-extension" import "function-or-class"


from human import Human


    # Specify the parent class(es) as parameters to the class definition

class Superhero(Human):

    # If the child class should inherit all of the parent's definitions without
    # any modifications, you can just use the "pass" keyword (and nothing else)
    # but in this case it is commented out to allow for a unique child class:
    # pass

    # Child classes can override their parents' attributes

    species = 'Superhuman'

    # Children automatically inherit their parent class's constructor including
    # its arguments, but can also define additional arguments or definitions
    # and override its methods such as the class constructor.
    # This constructor inherits the "name" argument from the "Human" class and
    # adds the "superpower" and "movie" arguments:

    def __init__(self, name, movie=False,
                 superpowers=["super strength", "bulletproofing"]):

        # add additional class attributes:

        self.fictional = True
        self.movie = movie

        # be aware of mutable default values, since defaults are shared

        self.superpowers = superpowers



        # The "super" function lets you access the parent class's methods
        # that are overridden by the child, in this case, the __init__ method.
        # This calls the parent class constructor:

        super().__init__(name)

    # override the sing method

    def sing(self):
        return 'Dun, dun, DUN!'

    # add an additional instance method

    def boast(self):
        for power in self.superpowers:
            print("I wield the power of {pow}!".format(pow=power))


if __name__ == '__main__':
    sup = Superhero(name="Tick")

    # Instance type checks

    if isinstance(sup, Human):
        print('I am human')
    if type(sup) is Superhero:
        print('I am a superhero')

    # Get the "Method Resolution Order" used by both getattr() and super()
    # (the order in which classes are searched for an attribute or method)
    # This attribute is dynamic and can be updated

    print(Superhero.__mro__)    # => (<class '__main__.Superhero'>,
                                # => <class 'human.Human'>, <class 'object'>)

    # Calls parent method but uses its own class attribute

    print(sup.get_species())    # => Superhuman

    # Calls overridden method

    print(sup.sing())           # => Dun, dun, DUN!

    # Calls method from Human

    sup.say('Spoon')            # => Tick: Spoon

    # Call method that exists only in Superhero

    sup.boast()                 # => I wield the power of super strength!
                                # => I wield the power of bulletproofing!

    # Inherited class attribute

    sup.age = 31
    print(sup.age)              # => 31

    # Attribute that only exists within Superhero

    print('Am I Oscar eligible? ' + str(sup.movie))


'''
####################################################
             6.2 Multiple Inheritance
####################################################
'''



    # Another class definition
    # bat.py

class Bat:

    species = 'Baty'

    def __init__(self, can_fly=True):
        self.fly = can_fly

    # This class also has a say method

    def say(self, msg):
        msg = '... ... ...'
        return msg

    # And its own method as well

    def sonar(self):
        return '))) ... ((('

if __name__ == '__main__':
    b = Bat()
    print(b.say('hello'))
    print(b.fly)


    # And yet another class definition that inherits from Superhero and Bat
    # superhero.py

from superhero import Superhero
from bat import Bat

# Define Batman as a child that inherits from both Superhero and Bat

class Batman(Superhero, Bat):

    def __init__(self, *args, **kwargs):
        # Typically to inherit attributes you have to call super:
        # super(Batman, self).__init__(*args, **kwargs)
        # However we are dealing with multiple inheritance here, and super()
        # only works with the next base class in the MRO list.
        # So instead we explicitly call __init__ for all ancestors.
        # The use of *args and **kwargs allows for a clean way to pass
        # arguments, with each parent "peeling a layer of the onion".
        Superhero.__init__(self, 'anonymous', movie=True,
                           superpowers=['Wealthy'], *args, **kwargs)
        Bat.__init__(self, *args, can_fly=False, **kwargs)

        # override the value for the name attribute
        self.name = 'Sad Affleck'

    def sing(self):
        return 'nan nan nan nan nan batman!'


if __name__ == '__main__':
    sup = Batman()

    # The Method Resolution Order
    print(Batman.__mro__)       # => (<class '__main__.Batman'>,
                                # => <class 'superhero.Superhero'>,
                                # => <class 'human.Human'>,
                                # => <class 'bat.Bat'>, <class 'object'>)

    # Calls parent method but uses its own class attribute

    print(sup.get_species())    # => Superhuman

    # Calls overridden method

    print(sup.sing())           # => nan nan nan nan nan batman!

    # Calls method from Human, because inheritance order matters
    
    sup.say('I agree')          # => Sad Affleck: I agree

    # Call method that exists only in 2nd ancestor
    
    print(sup.sonar())          # => ))) ... (((

    
    # Inherited class attribute
    
    sup.age = 100
    print(sup.age)              # => 100

    # Inherited attribute from 2nd ancestor whose default value was overridden.
    
    print('Can I fly? ' + str(sup.fly)) # => Can I fly? False


'''
####################################################
                7. Advanced
####################################################
'''



    # Generators help you make lazy code.
def double_numbers(iterable):
    for i in iterable:
        yield i + i

    # Generators are memory-efficient because they only load the data needed to
    # process the next value in the iterable. This allows them to perform
    # operations on otherwise prohibitively large value ranges.
    # NOTE: `range` replaces `xrange` in Python 3.

for i in double_numbers(range(1, 900000000)):  # `range` is a generator.
    print(i)
    if i >= 30:
        break

    
    
    # Just as you can create a list comprehension, you can create generator
    # comprehensions as well.

values = (-x for x in [1,2,3,4,5])
for x in values:
    print(x)  # prints -1 -2 -3 -4 -5 to console/terminal



    # You can also cast a generator comprehension directly to a list.

values = (-x for x in [1,2,3,4,5])
gen_to_list = list(values)
print(gen_to_list)  # => [-1, -2, -3, -4, -5]


    # Decorators are a form of syntactic sugar.
    # They make code easier to read while accomplishing clunky syntax.

    # Wrappers are one type of decorator.
    # They're really useful for adding logging to existing functions without needing to modify them.

def log_function(func):
    def wrapper(*args, **kwargs):
        print("Entering function", func.__name__)
        result = func(*args, **kwargs)
        print("Exiting function", func.__name__)
        return result
    return wrapper

@log_function               # equivalent:
def my_function(x,y):       # def my_function(x,y):
    return x+y              #   return x+y
                            # my_function = log_function(my_function)
    
    # The decorator @log_function tells us as we begin reading the function definition
    # for my_function that this function will be wrapped with log_function.
    # When function definitions are long, it can be hard to parse the non-decorated
    # assignment at the end of the definition.

my_function(1,2)                # => "Entering function my_function"
                                # => "3"
                                # => "Exiting function my_function"



    # But there's a problem.
    # What happens if we try to get some information about my_function?

print(my_function.__name__)                 # => 'wrapper'
print(my_function.__code__.co_argcount)     # => 0. The argcount is 0 because both arguments in wrapper()'s signature are optional.

    # Because our decorator is equivalent to my_function = log_function(my_function)
    # we've replaced information about my_function with information from wrapper




    # Fix this using functools

from functools import wraps

def log_function(func):
    @wraps(func)                            # this ensures docstring, function name, arguments list, etc. are all copied
                                            # to the wrapped function - instead of being replaced with wrapper's info
    def wrapper(*args, **kwargs):
        print("Entering function", func.__name__)
        result = func(*args, **kwargs)
        print("Exiting function", func.__name__)
        return result
    return wrapper

@log_function               
def my_function(x,y):       
    return x+y              

my_function(1,2)                            # => "Entering function my_function"
                                            # => "3"
                                            # => "Exiting function my_function"

print(my_function.__name__)                 # => 'my_function'
print(my_function.__code__.co_argcount)     # => 2