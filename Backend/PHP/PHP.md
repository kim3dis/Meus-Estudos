# PHP

## Sumário
- [Instalação](#instalação)
- [Hello World!](#hello-world!)
- [Funções para sessões](#funções-para-sessões)
- [Funções de usuário](#funções-de-usuário)


## Instalação
__Linux:__
```bash
sudo apt install lamp-server^
```

__Windows:__

Basta instalar algum WAMP (Windows: Apache + MySQL + PHP).

>O nome do arquivo de configurações do apache é: httpd.conf

>O do php é: php.ini

Para entrar no servidor basta acessar no browser:
- localhost/
- 127.0.0.1
***

## Hello World!
Para imprimir algo na tela, basta usar o comando ```echo``` ou ```print()```

```php
<?php
echo "Hello, World!"; // imprime Hello, World!
print("Hello, World!"); // também imprime Hello, World!
?>
```


***

## Git
Git: Controle de versão.

### Instalando o Git

__Windows:__ Basta acessar o site do [git](https://www.git-scm.com) e instalar.

__Linux:__ Já vem instalado.


### Clonar
Para clonar um projeto, digite no terminal:
```bash
git clone link
```


### Criar repositório

Para iniciar um repositório vazio em uma determinada pasta, basta digitar o comando abaixo no terminal:

```bash
git init
```

Para adicionar as pastas ao Stage Area (lista de espera), que é um, area de espera ou log de confirmação (commit).

```bash
git add .
```
>o "." significa para adicionar todos os arquivos alterados. Também podemos usar o --all para assionar a mesma função.


Para confirmar, utilizamos o commit (confirmação).
```bash
git commit -m "mensagem"
```

>O -m é de mensagem

Precisamos enviar ou empurrar para o servidor.
```bash
git remote add origin [link do repositório]
git push origin master
```

Precisamos também fazer as configurações de usuário:
```bash
git config --global user.name "kim3dis"
git config --global user.email "kim3dis@gmail.com"

```

### GitHub vs. BitBucket
O github é como se fosse uma rede social de desenvolvedores. A casa do desenvolvedor.
O BitBucket é mais voltado para empresas.


***

## Array
Umas das formas mais simples de se criar:

```php
$frutas = array("laranja", "abacaxi", "melancia");
print_r($frutas);
```
>Exibe o array e sua estrutura.
>Todo array inicia em 0
>Quando o array só tem uma dimensão, ele é um vetor.


Exemplo de array bidimiensional:
```php
$carros[0][0] = "GM";
$carros[0][1] = "Cobalt";
$carros[0][2] = "Onix";
$carros[0][3] = "Camaro";

$carros[1][0] = "Ford";
$carros[1][1] = "Fiesta";
$carros[1][2] = "Fusion";
$carros[1][3] = "Eco Sport";

echo $carros[0][3]; // imprime: Camaro

echo end($carros[1]); // imprime: Eco Sport 

```


```php
$pessoas = array();

array_push($pessoas, array(
	'nome'=>'kim',
	'idade'=>55
));

array_push($pessoas, array(
	'nome'=>'mik',
	'idade'=>55
));

print_r($pessoas); // imprime a estrutura do array pessoas
print_r($pessoas[0]); //devolve o array 0
print_r($pessoas[1]["nome"]); //devolve o nome que está no array 1

```



***

## Funções de usuário
```PHP
function nomeDaFuncao($parametro1){
	// código
	echo "Hello, " + $parametro1 + "<br>";
}
nomeDaFuncao("kim3dis");

```


***

## Funções para sessões
Mostrar o local em que fica salvo os arquivos da sessão:

```PHP
session_save_path();
```