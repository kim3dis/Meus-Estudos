# Javascript

## Sumário
- [Variáveis e Constantes](#variáveis-e-constantes)
- [Arrays](#arrays)
- [Condicionais](#condicionais)
- [Function](#function)
- [Loop](#loop)
- [Objetos](#objetos)

- [jQuery](#jquery)

## Variáveis e Constantes
```Javascript
var nome = "kim3dis";
const numero = 943;
```

Constantes são valores que não se alteram;
Variáveis são valores que podem ou não se alterarem;

**Variáveis evitam repetições desnecessárias (DRY).**

### Declarar conjunto de variáveis
Use uma vírgula para declarar mais de uma variável sem repetir a palavra-chave ```var```.

```Javascript
var nome = "kim3dis",
	idade = 88,
	estudante = true;

var x = 22, y = 65, z = 53;

```



### Tipos de valores

```Javascript
var nome = "kim3dis", // string
	idade = 88, // number (int)
	estudante = true, // boolean
	emprego; // undefined

console.log(typeof nome);

```


***


## Arrays

```Javascript
var videogames = ["PS4", "XBox", "WiiU", "GBA"];
console.log(videogames);
console.log(videogames[1]); // imprime XBOX
```

### Funções na variáveis
__Quantos itens tem no array (length)__

```Javascript
var videogames = ["PS4", "XBox", "WiiU", "GBA"];
console.log(videogames.length);
```



__Último item do array__

```Javascript
var videogames = ["PS4", "XBox", "WiiU", "GBA"];
var tamanhoArray = videogames.length;
console.log(videogames[tamanhoArray - 1]);
```



__Adicionar item no array (push)__

```
var videogames = ["PS4", "XBox", "WiiU", "GBA"];
videogames.push("3DS");
```



__Retornar índice pelo nome (indexOf)__

```Javascript
var videogames = ["PS4", "XBox", "WiiU", "GBA"];
videogames.indexOf("WiiU");
console.log(videogames.indexOf("WiiU")); // Retorna 2
```


__Remover item do array (splice)__
```Javascript
var videogames = ["PS4", "XBox", "WiiU", "GBA"];
videogames.splice(3, 2); // o 3 ele indica de onde quer começar a remover; o 2 indica quantos remover;
console.log(videogames);
```



***



## Condicionais

### if e else
```Javascript
var idade = 39;
if (idade >= 18) {
	console.log('Você pode dirigir!');
} else {
	console.log('Você não pode dirigir');
}
```

### if, else e else if
```Javascript
var faculdade = true,
	ensinoMedio = true;
if (faculdade) {
	console.log('Adiciona R$1000');
} else if (ensinoMedio) {
	console.log('Adiciona RS800');
} else {
	console.log('Adiciona R$600');
}
```


### switch
Usa-se o switch quando se tem muitas opções para verificar.
```Javascript
var cor = "azul";
switch (cor) {
	case "vermelho":
		console.log("Você escolheu o vermelho!");
		break;
	case "verde":
		console.log("Você escolheu o verde!");
		break;
	case "azul":
		console.log("Você escolheu o azul!");
		break;
	default:
		console.log("Não temos essa cor.");
}
```

Usamos o ```break``` para parar os comandos de um ```case``` e sair do switch. Caso contrário, se não houvesse o ```break```, seria acessado outro ```case```.

Caso não seja nenhuma das opções predefinidas, será chamado o ```default```. No ```default``` não há utilidade de se utilizar o ```break```, pois não há nenhum ```case``` abaixo dele.


### Boolean
Retorna true ou false.

```Javascript
var teste1 = '',
	teste2 = 'Olá!';
console.log(Boolean(teste1)); // retorna false
console.log(Boolean(teste2)); // retorna true
```

Tudo o que for undefined, null, 0, NaN e string vazia retornam ```false```.



***



## Function
```Javascript
function areaQuadrado(lado) {
	var area = lado * lado;
	return area;
}
console.log(areaQuadrado(4));
```

* Variáveis dentro de uma função (escopo) pode ser acessada fora dela (outro escopo);


### Hosting
As funções declaradas vão para a memória do JS, antes da execução.


### Funções anônimas
Funções sem nome.
```Javascript
var custoCarro = function(portas) {
	var precoInicial = 10000;
	if (portas) {
		return portas * precoInicial;
	} else {
		return 2 * precoInicial;
	}
}

console.log(custoCarro());
```



***



## Loop
Executar uma condição até que ela seja verdadeira.

### for
```Javascript
for (var i = 0; i < 10; i++) {
	console.log(i);
}
```

### while
```Javascript
var i = 0;
while (i < 10) {
	console.log(i);
	i += 2;
}
```




***



## Objetos
Objetos são coleções de propriedades. Estas compostas pela chave e valor.
Objetos servem para partir o código em pequenas partes, que podem ser utilizadas quando necessário.

Basta colocar {} em uma variável que vira objeto.

```Javascript
var kim3dis = {};
console.log(typeof kim3dis); // retorna: object
```

```Javascript
var kim3dis = {
	nome: "kim3dis",
	estudante: true,
	idade: 55
};

console.log(kim3dis.idade);
```

### métodos
Valores podem ser funções, isso transforma a propriedade em um método.

```Javascript
var quadrado = {
	totalLados: 4;
	area: function(lado) {
		return lado * lado;
	},
	perimetro: function(lado) {
		return lado * this.totalLados;
	}
}
console.log(quadrado.perimetro(20));
```



***



# jQuery
jQuery é uma biblioteca de JavaScript. Que facilita a manipulação do DOM.
! __DOM:__ É tipo o HTML final do site, que a gente consegue ver nas ferramentas ali de desenvolvedor do browser.

Um código utilizando só JavaScript é bem maior do que um código jQuery.



***



## jQuery vs. JS Puro
Código para selecionar um elemento (ID) da página.

```Javascript
// JS Puro
document.getElementById("button");
document.getElementByClass("button");
```

```javascript
// jQuery
$("#button");
$(".button");
```

Caso queira ver mais, acesse o site [You might not need jquery](youmightnotneedjquery.com)



***



## Instalação
Basta acessar o site do [jQuery](https://jquery.com/download/) e escolher entre compressed ou uncompressed.
Após, só usar com script no documento HTML no ```<head>``` ou no ```<body>```.

```HTML
<script src="https://code.jquery.com/jquery-3.2.1.min.js"></script>
```



***



## Selecionando elementos no DOM

### DOM: o que é?
**Document Object Model**

O DOM é como se fosse o HTML mais vivo que sofre alteração. 



```$ = jQuery;```

O sifrão ($) é só um atalho para o nome jQuery. Eles são iguais.

Vale lembrar que, o sifrão ($), pode ser usado para iniciar uma variável.



### ID
```javascript
$('#meuID');
```

### Classes
```javascript
$('.minhaClasse');
```

### Tag HTML
```javascript
$('span'); //<span>
$('ul li a'); // igual no css; herança;
```

### Salvar uma seleção em uma variável
1. Para não se repetir varias vezes;
2. Uma vez que se coloca na variável, ficará na memória. Sendo assim, acessar ele é mais rápido do que puxar ele várias vezes de um lugar diferente;

```javascript
var $meuId = $('#meuID');
```

!__DICA:__ Quando a variável começa com sifrão ($) é só para saber que ela é um elemento de jQuery.



***



## Manipulando o DOM

### .append()
Adiciona conteúdo ao final do item selecionado (dentro da tag).

```Javascript
$('p').append('<span>adiciona ao final</span>')
```


### .apendTo()
O conteúdo do objeto jQuery que será adicionado ao parâmetro do ```appendTo()```.

```javascript
$('h2').appendTo($('h1'));
```

Neste código ele adiciona todos os h2 ao final de todos os h1.


### .html()
[get] Pega o conteúdo dentro do primeiro item selecionado e transforma em uma string.

```javascript
var paragrafo = $('p').html(); // armazena em uma variável o <p>
console.log(paragrafo); // mostra o primeiro P da página;
```

[set] Adiciona um valor a todos os itens selecionados.

```Javascript
$('p').html('Sou um texto novo.');
$('h1, h2, h3').html('Modifico todos os títulos e sub-títulos da página.');
``` 



### .text()
[get] Pega todos os valores selecionados.

```javascript
var getH3 = $('h3').text();
console.log(getH3);
```


[set] Adiciona o conteúdo, porém não renderiza o HTML dentro dele.

```javascript
$('p').text("<span>Testando</span>");
// Ele não rederizará o <span>, sendo assim, a tag <span> será mostrada na página sem quaisquer problemas.
```



### .prepend() e .prependTo()
Mesma coisa que append, porém insere antes do conteúdo da seleção.



### .after() e .insertAfter()
Adiciona conteúdo após o item selecionado.

```javascript
$('p').after('<span> * </span>');

$('<span> * </span>').insertAfter('p'); // só muda a ordem
``` 



### .before() e .insertBefore()
Mesma coisa que ```.after()```, só que adiciona antes do conteúdo.



## Eventos
São comandos que, quando ativos, fazem alguma ação.

### click / .click()
Aciona uma função após o usuário clicar no target.

```Javascript
$('a').click(function() {
	$('p').text('Mudei!'); // qualquer método
});
```



### .on()
Os eventos também podem ser escritos com a função ```.on()```.

```javascript
$('a').on('click', function(){
	$('a').text("Mudei!");
});
```

Onde está ```'click'```, é a ação que deve ser tomada.

Este dá mais flexibilidade do que o ```.click()```.



### $(this)
Use o this para se referir ao objeto do evento.

```javascript
$('a').on('click', function(){
	$(this).text('Mudei!'); // this se refere ao objeto clicado
});
```



### O event object

```javascript
$('a').on('click', function(e){
	e.preventDefault();
	$(this).text('Mudei!'); // this se refere ao objeto clicado
});
```

```preventDefault()``` 
:previne que seja feito o padrão daquele objeto, como por exemplo, um ```<a href="github.com">``` com ```preventDefault()``` este ```<a>``` não levaria a lugar algum ao ser clicado.

Digamos que tenho um ```<a>``` linkado com uma id de uma div. Eu não quero que, ao ser clicado, a tela seja redirecionada ao div instantaneamente. Gostaria de uma animação suave com JS. Para isso, eu teria que primeiro usar o ```preventDefault()``` para tirar o evento padrão e depois criar toda a animação.



### mouseenter / .mouseenter() | mouseleave / .mouseleave()

```javascript
$('p').on('mouseenter', function(){
	$(this).text('Mudei!'); //muda o texto quando o mouse entra no <p>
});

$('p').on('mouseleave', function(){
	$(this).text('Você tirou o mouse :C');
});

```



### scroll / .scroll()

```javascript
$(document).on('scroll', function(){
	$('a').append('Scrollou');
});
```



### resize

```javascript
$(window).on('resize', function(){
	$('a').text($('body').width());
});
```



## Classes
### Adicionando
```javascript
$('a').click(function() {
	$(this).addClass('active');
});
```

### Removendo
```javascript
$('a').click(function() {
	$(this).removeClass('active');
});
```

### Adicionando e Removendo
```javascript
$('a').click(function() {
	$(this).toggleClass('active');
});
```


### Verifica existência de classe
O ```.hasClass()``` verifica se a classe existe e retorna um valor booleano.

```javascript
$('a').click(function() {
	var condition = $(this).hasClass('active');
	if (condition) {
		console.log('possui a classe');
	}
});
```

### .attr()
Pega ou define o valor de um atributo específico.

```javascript
$('a').attr('href'); // get
$('a').attr('href', 'https://www.github.com'); // set

```



### .removeAttr()
Remove atributo.

```javascript
$('img').removeAttr('src');
```



### .val()
Pega valores, como de input e textarea.

```
// supondo que exista uma caixa de texto com uma classe de .nome e um botão de enviar com o ID de #enviar

$('#enviar').on('click', function(){
	var getNome = $('.nome').val();
});
```



### .remove()
Remove todos os elementos selecionados do DOM.

```javascript
$('a').remove();
// remove todos os <a> da página
```



### .empty()
Remove todos os elementos filhos no DOM.

```javascript
$('ul').empty();
// removeria os <li> do <ul>
```



### .css()
pega ou define o valor de uma propriedade CSS.

```javascript
var size = $('p').css('font-size');
console.log(size);
```


É possível atribuir mais de uma propriedade.

```javascript
$('a').css({
	'text-align': 'center',
	'text-decoration:' 'none'
});

```