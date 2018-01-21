# Python

## Sumário


***

## Fontes usadas
#### Livros
#### Vídeos
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

## (multiline) Formatação de saída
Com três aspas simples ou duplas podemos criar uma multiline. Ela é muito empregada em formatação de saída de console.

```Python
print("""\
Uso: programa [opção]
    -h      Exibe ajuda.
    -p      Porta.
""")
```


***

## len()
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

## Pegando dados no terminal
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

## (loop) range
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
<!--  -->
