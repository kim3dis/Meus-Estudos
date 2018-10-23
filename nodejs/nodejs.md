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

var express = require('express'); // recuperando a lib do express
var app = express(); // executando a função do modo do express


// função que fica escutando a porta 300; faz-se necessário um callback para o servidor.
app.listen(3000, function(){
	console.log("Estou escutando na porta 3000 com Express!");
}); 

```
>O módulo express retorna uma função, todavia não a executa. É necessário chamar a função.


#### Tratando URL(rotas) com Express
Ao tentar requisitar a página, deparamos com a mensagem _Cannot GET/_. Essa mensagem vem do Express. O Express já tratou o erro. Ele já identificou que não existe caminho/página/resposta para ser dada no endereço raíz (/).

```javascript
// FILE: app.js

//passa o caminho e o callback
app.get('/', function(req, res){
	res.send('<h1>Sou a raíz com Express.</h1>');
});
```
>OBS.: utiliza-se o ```end()``` no NodeJS; no Express, utiliza-se ```send()```.


### EJS (<%= Embedded JavaScript %>)
Linguagem de modelagem utilizando JS para criar páginas HTML.
```bash
npm install ejs --save
```

Agora precisamos informar que a Engine de View do Express passou a ser o módulo EJS.
```javascript
// FILE: app.js

app.set('view engine', 'ejs'); // usamos esse método para modificar alguma coisa na 'tabela de propriedades' do Express.
```

#### Preparando o ambiente para deixar as views em local
Por padrão, crie o diretório: _/views/_.
A ideia é, dentro desse diretório, criar nossos arquivos HTML para que esses arquivos possam ser consumidos em função das requisições.

```javascript
// FILE: app.js


//app.get('/', function(req, res){
//	res.send('<h1>Sou a raíz com Express.</h1>');
//});

// trocamos de send para render
app.get('/shop', function{
	res.render("shop.ejs"); // agora basta chamar o arquivo/view
});

```

```javascript
// FILE: /views/shops.ejs
<html>
	<head>
		<meta charset='utf-8'>
	</head>
	<body>
		<h1>Sessão Shop</h1>
	</body>
</html>
```


### NodeMon
Utilitário que reiniciar automaticamente o servidor NodeJS quando houver alguma alteração nos scripts.

