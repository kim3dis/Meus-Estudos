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

Antes de mais nada, precisa-se criar uma chave SSH para fazer a conexão com o github.
```bash
cd ~/.ssh
ssh-keygen
```
Dê enter para as 3 perguntas sequentes.
O que estamos procurando é um arquivo .pub chamado **id_rs**. Abra-o com um editor de texto e copie tudo que se encontra dentro ou abra no terminal com ```cat```:

```bash
ls
gedit id_rsa.pub
```

Agora basta ir nas configurações de perfil e [SSH and GPG keys](https://github.com/settings/keys), New SSH key e colar a key.

Tudo pronto, só falta dá um ```git push```.


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

## Variáveis
Variáveis são espaços de memória no computador que possuem algum valor.

```php
$nome = "kim3dis"; //string
$idade = 55; //int
$estudante = true; //boolean
```

### Apagar variáveis
```php
$var1 = 1;
$var2 = 2;
unset($var1, $var2); //as duas variáveis deixam de existir
```

### Saber se a variável existe ou está definida

```php
if(isset($nome1)){
	print("Existe!");
} else {
	print("Não existe!");
}

```

### Concatenar variáveis
Basta adicionar um ponto no meio das duas.

```php
$primeiroNome = "kim";
$segundoNome = "3dis";

$nomeCompleto = $primeiroNome . $segundoNome; // junta as duas strings, 
```


***

## Tipos de dados
Temos, no PHP, 8 tipos de dados primitivos divido em 3 grupos.

__Tipos básicos:__  int, string, float e boolean.

__Tipos compostos:__ Array e objetos.

__Tipos especiais:__ resource e null.


```php
$nome = "kim"; // string
$idade = 55; // int
$dinheiro = 0.10; // float
$estudante = true; // boolean
//////////////////////////////
$frutas = array("abacaxi", "laranja", "maçã"); // array
$nascimento = new DateTime(); // object
//////////////////////////////
$arquivo = fopen("exemplo.txt", "r"); // resource
$nulo = NULL; // null
```

>Nulo é a ausência de valor. Não existe; No vazio, ele foi iniciado. Só não tem informação. Já está reservado na memória.
>Quando se destrói uma variável ela vira null.


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


### Adicionar item na lista
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