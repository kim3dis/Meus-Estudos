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















<!--  -->
