## Sumário
- [Variáveis e Constantes](#variáveis-e-constantes)
- [Arrays](#arrays)
- [Condicionais](#condicionais)
- [Function](#function)
- [Loop](#loop)
- [Objetos](#objetos)
- [Orientação a objetos](#orientação-a-objetos)

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

```Javascript
(function(x1, x2, operador){
	return eval('${x1} ${operador} ${x2}');
})(2, 2, "*");
```


### Arrow Function

```javascript
let calc = (x1, x2, operador) => {
	return eval('${x1} ${operador} ${x2}');
}
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


## Orientação a objetos

```javascript
//classe
class Carro {

}
```
>primeira letra de uma classe sempre maiúscula

Uma classe é um conjunto de atributos e metódos. Objeto é quem representa uma classe.
Dentro de uma classe, você vai encontrar: variáveis e funções. Variáveis são recursos que armazenam informações na memória; Funções são códigos que execultam uma ação e retornam algum valor. 
*Só que, como variáveis e funções ficaram dentro de uma classe, elas ficaram metidas, não querem ser chamadas assim. Agora elas passam a ser chamadas de atributos e metódos.*

Atributo é o mesmo que uma variável, só que dentro de uma classe; e metódo é a mesma coisa que uma função, só que dentro de uma classe. É claro que aí ganham alguns recursos a mais.

```javascript
// objeto
let carro1 = new Carro();
```


### Método construtor e encapsulamento
#### Construtor
```javascript
class Carro {
	constructor(){
		this.nomeCarro = "unknown";
		this.motor;
	}
}
```

#### Encapsulamento com getters e setters

```javascript
class Carro {
	constructor(){
		this._nomeCarro = "unknown";
		this._motor;
	}

	get nomeCarro() {
		return this._nomeCarro;
	}
	set nomeCarro(value) {
		return this._nomeCarro = value;
	}
}

	
```



***

### Manipulando DOM
>Document Object Model

```javascript
class Carro {
	constructor(){
		this._nomeCarro = "unknown";
		this._motor;
		this._initialize(); // +
	}

	// +
	initialize(){
		let algumID = document.querySelector("#nomeCarro");

		algumID.innerHTML = "Mustang GT";
	}

	get nomeCarro() {
		return this._nomeCarro;
	}
	set nomeCarro(value) {
		return this._nomeCarro = value;
	}
}

	
```

