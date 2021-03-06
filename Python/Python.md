# Python

## Sumário
[Fontes usadas](#fontes-usadas)

[Por que usar Python?](#por-que-usar-python?)

[Qual o inconveniente?](#qual-o-inconveniente?)

[Instalação](#instalação)

[Variáveis e operações](#variáveis-e-operações)

[Gerando números por meio de funções](#gerando-números-por-meio-de-funções)

[Operadores aritméticos](#operadores-aritméticos)

[type()](#type())

[Multiline](#multiline)

[len](#len)

[Mais operações](#mais-operações)

[Pegando dados](#pegando-dados)

[Comparações](#comparações)

[Condicionais: if, elif e else](#Condicionais:-if-elif,-e-else)

[Operadores lógicos](#operadores-lógicos)

[Loops](#loops)

[Listas](#listas)

[Range](#range)

[Enumerando coleções com for e enumerate](#enumerando-coleções-com-for-e-enumerate)

[Funções](#funções)

[Orientação a objetos](#orientação-a-objetos)


***

## Fontes usadas
#### Livros
#### Vídeos
Udemy: Python Scrapy: Capture Dados Web

#### Tópicos na internet

## Por que usar Python?
 - Qualidade de software;
 - Produtividade do desenvolvedor;
 - Portabilidade do programa;
 - Bibliotecas de suporte;
 - Integração de componentes;


***

## Qual o inconveniente?
Sua velocidade de execução pode nem sempre ser tão rápida quanto as linguagens compiladas, como C e C++.


***

## Instação
### Linux
No linux, o Python já vem instalado. O que pode ser adicionado é uma IDLE, como o PyCharm.


***

## Variáveis e operações
Python 3 possui três tipos de números embutidos: ```int```, ```float``` e ```complex```.

É muito simples declarar variáveis em Python, veja:

```Python
a = 10 # inteiro
b = 5 # inteiro
print(a + b) # imprime 15
```

```Python
x = 4
y = x
x = 0
# x equivale a 0, y equivale ao primeiro valor de x, 4
```

### Complexos
Os números complexos têm sufixo j ou J:

```Python
complexo = 1+2j
real_complexo = 1+2j.real
imaginaria_complexo = 1+2j.imag  
```

## Gerando números por meio de funções
```Python
x_float = float(2.5)
x_int = int(3)
```

***

## Operadores aritméticos
O conjunto base de operadores aritméticos com números em Python é:

```Python
adicao = 5 + 5
subtracao = 5 - 5
multiplicacao = 5 * 5
divisao = 5 / 5
divisao2 = 5 // 4
resto = 5 % 4
potencia = 5 ** 5
```

***

## type()
Podemos saber o tipo da variável com ```type(obj)```.

```Python
type(4.0) // retorna: <type 'float'>
```


***

## multiline
Com três aspas simples ou duplas podemos criar uma multiline. Ela é muito empregada em formatação de saída de console.

```Python
print("""\
Uso: programa [opção]
    -h      Exibe ajuda.
    -p      Porta.
""")
```


***

## len
Para saber o tamanho de uma string (palavras), usamos ```len(string)```.

```Python
nome = "kim"
print(len(ent)) # output: 3
```


***

## Mais operações
Podemos executar outras operações como: ```o in kim```, se "o" está em "kim"; ```n not in kim```, se "n" não está em "kim"; ```lu + ol```, concatenação de lu com ol; ```"a" * 4```, 4 repetições com "a".

```python
>>> "k" in "kim3dis"
# True

>>> z not in "kim3dis"
# True

>>> "kim" + "3dis"
# kim3dis

>>> "i" * 3
# iii
```


***

## Pegando dados
Usamos a função ```input()``` para capturar um input do usuário. 


```python
nome = input("Informe seu nome:");
```


O valor retornado é sempre uma string, mesmo que o usuário tenha colocado algum número. Caso não queremos que os dados inseridos não seja strings, basta adicionarmos nas as funções de conversão ```int()``` e ```float()```, e dentro dos parâmetros dessas funções, adicionar o ```input()```. Veja abaixo:

```python
idade = int(input("Insira sua idade: "))
media = float(input("Insira sua média: "))
```


***

## Comparações
Python possui 8 operadores, aqui abaixo está a lista de alguns deles:
 - ```<``` menor que; 
 - ```<=``` menor ou igual que;
 - ```>``` maior que;
 - ```>=``` maior ou igual que;
 - ```=``` igual;
 - ```!=``` não igual;

Ao comparar objetos, será retornado um valor booleano: ```true``` ou ```false```.


***

## Condicionais: if, elif e else
```if``` é um comando que avalia uma __expressão__ e escolhe um bloco para ser executado de acordo com o resultado dessa avaliação (true ou false).

```python
nome = input(insira seu nome: )
if nome == "":
	print("você não inseriu seu nome.")
else:
	print("Obrigado por inserir seu nome")
```

### elif
```elif``` avalia uma outra expressão e é executada caso esta seja verdadeira.

```python
numero = 5
tentar = int(input("Tente acertar o número: "))
if numero = tentar:
	print("Parábens, você acertou.")
elif tentar > numero:
	print("Seu número é menor")

elif tentar < numero:
	print("Seu número é maior")

else:
	print("Isso não é um número")

```


***

## Operadores lógicos
São ```and```, ```or``` e ```not```
```phyton
imposto = float(input("Imposto: "))
if imposto < 10.:
	print("Baixo")
elif imposto >= 10. and imposto <= 27.:
	print("Médio")
elif imposto > 27. and imposto < 100:
	print("Alto")
else:
	print("Imposto inválido")
```


***

## Loops
### while
```python
a = 0
b = 5
while a < b:
	a += 1
	print(a)
```



***

## Lista
```python
listas = ["world", "hello", "listas são legais", 2, 2.1]
```

As listas elas são mutáveis, logo podemos realizar atribuições em índices.
```python
listas = ["world", "hello", "listas são legais", 2, 2.1]
lista[2] = "olá"
lista[1] = "mundo"
```

O ```if``` avalia listas vazias como ```false```.


### Percorrer listas com for
```python
listas = ["world", "hello", "listas são legais", 2, 2.1]
for percorrer in lista:
	print(percorrer)

### saída ###
# world
# hello
# listas são legais
# 2
# 2.1
######
```


***

## range
```python
for i in range(5):
	print(i)

### saída ###
# 0
# 1
# 2
# 3
# 4
```


***

## Enumerando coleções com for e enumerate

```python
lista = ["sou zero", "sou um"]
for i, lista in enumarate(lista):
	print(i, lista)

### saída ###
# 0 sou zero
# 1	sou um
```


***

## Funções
Em python, funções são objetos de primeira classe, portanto, podem ser passadas como parâmetros, atribuídas a variáveis, retornar outras funções e, até mesmo, terem atributos próprios.

```python
def soma(a, b):
	return a + b
resultado = soma(1, 3)
```


***

### Manipulação de arquivos
Para criar arquivos, utiliza-se o ```open()```, dentro dos paramêtros informamos o nome do arquivo seguido de sua extensão. Conseguimos inserir mais um paramêtro para dizer o modo do arquivo.

```python
contatos = open('contatos.csv', 'w') # w é de escrita, 'write'
```
> No segundo paramêtro, existem mais duas opção para o 'w', que é o 'wt' e o 'wb'. O 'wt' é escrita de texto, o 'wb' é escrita binária. Se não houver especificação, como foi o caso a cima, ele entenderá que é escrita com texto (wt) por padrão.



Para escrever, usa-se o ```write()```.

```python
# linha a cima, contato = open(...)
contatos.write('%s, %s, %s' %(nome, email, telefone))
```


Hora de sair e fechar o arquivo:
```python
# os dois comandos a cima ...

contatos.flush()
contatos.close()
```

> Se for tudo declarado desta maneira, o arquivo será criado na mesma pasta do arquivo python.


### Ler o arquivo
Tudo certo, mas e para ler?
Só usar o modo de leitura:

```python
contatos = open('contatos.csv')
print(contatos.read())
contatos.close()
```
***

Na primeira linha abrimos o arquivo. Se não adicionarmos um modo, por padrão, ele abrirá como modo de leitura, 'r' (read).
Já na segunda linha, chamamos a função read() e pedimos para printar o que tem dentro do arquivo.
E na última, fechamos o arquivo.


### Continuar a escrever
Se escrevermos no arquivo, salvar e tentar escrever algo utilizando os códigos acima veremos que ele sobrescreveu os dados antigos. E talvez não seja isso que queremos em determinadas vezes. A solução é usar no modo o 'a' ao invés do 'w'.

```python
contatos = open('contatos.csv', 'a')
contatos.write('\n Não sobrescrevo mais o arquivo. c:')
arquivo.flush()
arquivo.close()
```

> O \n é somente para escrever na linha de baixo.


## Orientação a objetos

```python
class Robo(object):
	def __init___(self, x, y):
		self.x = x
		self.y = y

robo1 = Robo(5, 5)

class Robo3D(Robo):
	def __init__(self, x, y, z):
		super(Robo3D, self).__init__(x, y) # herdar da primeira classe
		self.z = z

robo 2 = robo3D(5, 6, 8)
```

>A classe Robo herda de object

> ```def __init__(self):``` é um construtor ou inicializador, tem a função de inicializar a instância. Este 'self' poderia ser qualquer nome. Ele é a instância atual.

>Nunca é preciso dar o valor de ```self```.

>