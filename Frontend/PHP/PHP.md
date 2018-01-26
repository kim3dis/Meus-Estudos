# PHP

## Sumário
[Instalação](#instalação)

[Funções para sessões](#funções-para-sessões)
[Funções de usuário](#funções-de-usuário)


## Instalação
__Linux:__
```bash
sudo apt install lamp-server^
```

__Windows:__

Basta instalar algum WAMP (Windows: Apache + MySQL + PHP).

> O nome do arquivo de configurações do apache é: httpd.conf
> O do php é: php.ini

***

## 


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