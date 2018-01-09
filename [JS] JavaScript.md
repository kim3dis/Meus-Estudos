# Javascript

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