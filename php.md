# Curso PHP7 - HCode

## Instalação
__Linux:__
```bash
sudo apt install lamp-server^
```

__Windows:__
Basta instalar algum WAMP (Windows: Apache + MySQL + PHP).


## Funções para sessões
Mostrar o local em que fica salvo os arquivos da sessão:

```PHP
session_save_path();
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