# NodeJS

## O que é
É um interpretador de códigos JS baseado em V8 (engine)

## Respondendo requisições HTTP
```javascript
var http = require('http'); // incorporando a lib http

http.createServer(function(req, res){
	res.end("<meta charset='utf-8'");
	res.end("<h1>Essa é a minha resposta!</h1>");
}).listen(3000); 
```
>```req``` é a requisição; ```res``` é a resposta;


## Respondendo requisições com base na URL (.url)
```javascript
var http = require('http'); // incorporando a lib http

http.createServer(function(req, res){
	console.log("Acesso à página."); // mostra no terminal que foi acessado a página

	// tratamento com base na URL
	if(req.url == "/") {
		res.end("<h1>Essa é a minha resposta!</h1>");
		console.log(req.url);
	} else {
		res.end("<h1>Oops, dont worry. <br>We not found this page, but you can try again.</h1>");
		console.log(req.url);
	}
}).listen(3000); 
```


## Recursos importantes para produtividade
### npm
Gerenciador de pacotes JS.
#### Instalação
```bash
sudo apt install npm
```

No arquivo do projeto, rode o seguinte comando. Dê enter até finalizar e gerar o arquivo _package.json_.
```bash
npm init
```

### Express
Framework nodejs para aplicações web.
#### Instalação
```bash
npm install express -save
```
>```-save``` o express vai junto com o projeto

#### refactoring do projeto
Crie /app.js
```javascript
// FILE: app.js

var express = require('express');
```
>O módulo express


### EJS (<%= Embedded JavaScript %>)
Linguagem de modelagem utilizando JS para criar páginas HTML.

### NodeMon
Utilitário que reiniciar automaticamente o servidor NodeJS quando houver alguma alteração nos scripts.

