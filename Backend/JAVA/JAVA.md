# Java

## Sumário



## Instalação
O JAVA possui 2 pacotes, JRE e JDK.
Se você quiser apenas executar aplicações JAVA, o JRE atende seus requisitos. Esse ambiente de execução já possui uma JVM. Porém, se você deseja criar aplicações JAVA, você precirá do JDK. No JDK, ele já possui uma JVM e JRE nele.j



## Primeiros comandos
```java
public class OlaMundo {
	public static void main(String[] args) {
        System.out.println("Olá, mundo!");
    }
}
```



## Declarando e usando variáveis

Dentro de um bloco, podemos declarar variáveis e usá-las. Em JAVA, toda variável tem um tipo que não pode ser mudado, uma vez que declarado:

```java
// tipoDaVariavel nomeDaVariavel;
int idade;
```


Com isso, foi declarado a variável ```idade```, que passa a existir a partir daquela linha.

```java
// a linha a seguir é uma tradução de: "idade deve valer quinze".
idade = 55;
```


__Imprime a idade:__

```java
System.out.println(idade);
```


```java
class TestaIdade {
	public static void main (Static args) {
		int idades = 55;
		int idadeAnoQueVem = idade + 1;
		System.out.println(idadeAnoQueVem);
	}
}
```


### Números reais (flutuantes)

```java
double pi = 3.14;
double x = 5 * 10;
```


### Valores booleanos

```java
boolean verdade = true;
```


### char

Variáveis do tipo char são pouco usadas no dia a dia.

```java
char letra = 'a';
System.out.println(letra);
```


### Tipos primitivos e valores

Esses tipos de variáveis são tipos primitivos do JAVA: o valor que elas guardam são o real conteúdo da variável. Quando você utilizar o __operador de atribuição__ (=) o valor será copiado.

```java
int i = 5; // i recebe uma cópia do valor 5
int j = i; // j recebe uma cópia do valor de i
i = i + j; // i vira 6, j continua 5
```


### Outros tipos primitivos

O JAVA tem outros, que são o byte, short, long e float.

### Casting
```java
float x = 0.0;
```

O código acima não compila, pois todos os literais com ponto flutuante são considerados ```double``` pelo JAVA. E ```float``` não pode receber um ```double``` sem perda de informações, para fazer isso funcionar podemos escrever o seguinte:

```java
float x = 0.0f;
```

```java
double d = 5;
float f = 3;

float x = f + (float) d;
```



## Condicionais

### if e else

```java
boolean condicao = true;
if (condicao) {
System.out.println("Verdade!");
}
```

Pode-se concatenar expressão booleanas através dos operadores lógicos: **&&** e **||**.



***



## Loop

### while
O ```while``` é um comando usado para fazer um __laço (loop)__, isso é, repetir um trecho de código algumas vezes.

```java
int idade 55;
while (idade < 60) {
	System.out.println9idade += 1;
}
```

### for
O for isola também um espaço para inicialização de variáveis e o modificador dessas variáveis. Isso faz com que fiquem mais legíveis, as variáveis que são relacionadas ao loop.

```java
for (int i = 0; i < 5; i += 1) {
	System.out.println(i);
}
```


### Controlando loops

Podemos decidir
```java
for (int i = x; i < x; i++) {
	if(i % 19 == 0) {
		System.out.println("Achei um número divisível por 19 entre x e y");
		break;
	}
}
```


## Orientação a objetos
Orientação a objetos é uma maneira de programar que ajuda na organização e resolve muitos problemas enfrentados pela programação procedural.


### Uma classe em JAVA
A palavra classe vem da taxonomia da biologia. Todos os seres vivos de uma mesma classe biológica têm uma série de atributos e comportamentos em comum, mas não são iguais, podem variar nos valores desses atributos e como realizam esses comportamentos. Homo Sapiens dene um grupo de seres que possuem características em comum, porém a denição (a ideia, o conceito) de um Homo Sapiens é um ser humano? Não. Tudo está especicado na classe Homo Sapiens, mas se quisermos mandar alguém correr, comer, pular, precisaremos de uma instância de Homo Sapiens, ou então de um objeto do tipo Homo Sapiens.
Um outro exemplo: uma receita de bolo. A pergunta é certeira: você come uma receita de bolo? Não. Precisamos instanciá-la, criar um objeto bolo a partir dessa especicação (a classe) para utilizá-la. Podemos criar centenas de bolos a partir dessa classe (a receita, no caso), eles podem ser bem semelhantes, alguns até
idênticos, mas são objetos diferentes.

```java
class Conta {
	int numero;
	String dono;
	double saldo;
	double limite;
}

```

### Criando e usando um objeto
Para criar (instanciar) uma **conta**, basta usar a palavra chave ```new```.

```java
class Programa {
	public static void main(String args[]) {
		Conta minhaConta = new Conta();
	}
}
```

Através da variável __minhaConta__, podemos acessar o objeto recém criado para alterar os valores dos atributos.

```java
// dentro da classe principal
minhaConta.dono = "kim";
minhaConta.saldo = 800.0;

System.out.println("Saldo atual: " + minhaConta.saldo);
```

### Métodos
Dentro da classe, também declararemos o que cada conta faz e como isto é feito - os comportamentos que cada classe tem, isto é, o que ela faz.

```java
class Conta {
	// ... outras variáveis ...

	void saca(double quantidade) {
		double novoSaldo = this.saldo - quantidade;
		this.saldo = novoSaldo;
	}
	void deposita(double quantidade) {
 		this.saldo += quantidade;
	 }
}
```

A palavra chave ```void``` diz que, quando você pedir para a conta sacar uma quantia, nenhuma informação será enviada de volta a quem pediu.

Quando alguém pedir para sacar, ele também vai dizer quanto quer sacar. Por isso precisamos declarar o método com algo dentro dos parênteses - o que vai aí dentro é chamado de argumento do método (ou parâmetro). Essa variável é uma variável comum, chamada também de temporária ou local, pois, ao final da execução desse método, ela deixa de existir.


## Arrays
```java
int[] idades;
```

O int[] é um tipo. Uma array é sempre um objeto, portanto, a variável idades é uma referência. Vamos precisar criar um objeto para poder usar a array.

```java
idades = new int[10];
idade[5] = 10;
```

```java
Conta[] minhasContas;
minhasContas = new Conta[10];

Conta contaNova = new Conta();
contaNova.saldo = 1000.0;
minhasContas[0] = contaNova;

minhasContas[1] = new Conta();
minhasContas[1].saldo = 3200.0;
```


## Modificadores de acesso e atributos de classe
### Controlando o acesso
```java

class Conta {
	private double saldo;
	private double limite;
	// ...
}

```

```private``` é um modificador de acesso (também chamado de modificador de visibilidade).

Marcando um atributo como privado, fechamos o acesso ao mesmo em relação a todas as outras classes.




### Getters e Setters
O private faz com que ninguém consiga modificar, nem mesmo ler, o atributo em questão.
Com isso temos um problema: como fazer para mostrar o saldo de uma Conta, já que nem mesmo podemos acessá-lo para leitura?


```java

class Conta {
	
	//...
	private double saldo;
	//...

	public double pegaSaldo() {
		return this.saldo;
	}

}

```

Para permitir o acesso aos atributos (já que eles são private) de uma maneira controlada, a prática mais comum é criar dois métodos, um que retorna o valor (get) e o outro que muda o valor (set).

É uma má prática criar classe e, logo em seguida, criar getters e setters para todos os seus atributos. Você só deve criar um getter ou setter se tiver a real necessidade.



### Construtores
Quando usamos a palavra chave ```new```, estamos construindo um objeto. Sempre quando o ```new``` é chamado, ele executa o construtor da classe. O construtor da classe é um bloco declarado com o mesmo nome que a classe.