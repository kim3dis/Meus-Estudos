# Conteúdo do livro: CSS Eficiente Técnicas e ferramentas que fazem a diferença nos seus estilos - Casa dos Códigos


## Superqualificando seletores
Seletores superqualificados fazem com que o navegador trabalhe mais do que precisa e deveria. Construa seletores mais enxultos e de alto desempenho, eliminando as partes desnecessárias.


Um exemplo, infelizmente, bastante comum:

```CSS
ul#nav li a {}
```
Já se sabe que, se o __a__ está dentro de __li__, que tem que estar dentro de __#nav__, de modo que é possível, eliminar o __li__ do seletor logo de cara. Como o __#nav__ é um ID, o elemento __ul__ também pode ser eliminado.

Então, uma forma melhor, mas ainda não ideal de se escrever, seria:

```css
#nav a {}
```

***


## CSS Orientado a Objetos (OOCSS)
Não se trata de mudar a sintaxa do CSS ou instalar algum pacote mágico que o fará melhor. CSS orientado a objetos é uma __metafora__ para indicar que é possível escrever um CSS mais eficiente, sem repetições, que enseje a projetos mais profissionais.

Visa resolver problemas clássicos, tais como:
* A dificuldade de tocar projetos de médio/grande porte;
* O tamanho dos arquivos CSS é cada vez maior conforme o projeto evolui;
* Reúso de código quase inexistente;
* Código frágil/fraco;


Com uso do OOCSS:
* __Modular:__ combinável, reusável e extensível;
* __Leve:__ relacionamento 1:N entre CSS e potenciais layouts;
* __Rápido:__ poucas requisições HTTP e tamanhos mínimos de arquivos;
* __Pronto para o futuro:__ manutenível, semântico e padronizado;
* __Simplificado e acessível:__ um bombonzinho!


***


## SMACSS
* Base;
* Layout;
* Module (Módulo);
* State (Estado);
* Theme (Tema);


***


## Pré-processadores CSS
Um pré-processador é um programa que recebe texto e efetua conversões léxicas nele. As conversões podem incluir substituição de macros, inclusão condicional e inclusão de outros arquivos.

Quer dizer, você escreverá código na sintaxe do pré-processador de sua preferência e, através de alguns processos de conversão, ele transforma (ou compila) essa sintaxe específica e própria em código CSS, a que todos já estamos habituados. Caso contrário, não se teria nenhuma estilização, já que, para este fim, os navegadores precisam de arquivos .css.


***


### SASS e LESS
Sass e Less fornecem quase o mesmo acervo de funcionalidades. Há várias controvérsias e discussões acalouradas entre os adeptos de um e outro, mas a verdade é que, nessa quase conversão de características, ao optar por usar Sass ou Less, você estará bem servido e conseguirá melhorar muito a organização e workflow de desenvolvimento de estilos!


***


### Instalar e compilar (linux)
Como o Ruby já vem por padrão no linux, só basta instalar o SASS no terminal:

```bash
sudo apt install gem
sudo gem install sass --no-user-install
```

Para verificar se foi instalado com êxito:

```bash
sass -v
```


Para __compilar__ um arquivo .scss, temos que executar no terminal (dentro da pasta):

```bash
sass nomedoarquivo.scss:nomedoarquivo.css
```

Será criado dois arquivos: **nomedoarquivo.css.map** e **nomedoarquivo.css**.

Agora só basta linkar em nosso HTML o **nomedoarquivo.css**.

***


### (SASS) Aninhamento de regras
É possível aninhar regras CSS para escrever um código mais conciso e menor, conferindo hierarquia visual às regras e facilitando da leitura!

Por exemplo, veja esse trecho de CSS:

```CSS
nav ul {
  list-style: none;
  margin: 0;
  padding: 0;
}
nav li {
  display: inline-block;
}
nav a {
  display: block;
  padding: 6px 12px;
  text-decoration: none;
}
```

Em SCSS, é possível escrever assim:

```SCSS
nav {
  ul {
    margin: 0;
    padding: 0;
    list-style: none;
  }
  li {
    display: inline-block;
  }
  a {
    display: block;
    padding: 6px 12px;
    text-decoration: none;
  }
}
```

***


### Referência ao ascendente
Em algumas situações, é preciso fazer referência ao ascendente para se montar uma regra apropriadamente. Por exemplo, dentro do aninhamento permitido por Sass, como seria para colocar uma regra com :hover ?
Para esses casos, Sass provê uma característica muito interessante, tornando possível fazer referência ao elemento ascendente imediatamente superior: o caractere &.

```SCSS
.selector {
  $:hover {
    /*
    código
    */
  }
}
```

Isso geraria: ```.selector:hover {}```

A intenção com **&** é repetir o seletor ascendente.


***


### Variáveis
Para declarar uma variável, basta dar um nome qualquer precedido de $ , usar : e dar o valor que se queira, como em:

```SCSS
$mainColor: #c0ffee;

  header {
    background-color: $mainColor;
  }
```

Variáveis podem conter quaisquer valores usados em CSS, como em:

```SCSS
$font-stack: Helvetica, sans-serif;
$width: 5em;
```

***


### Interpolação de variáveis
Juntar o valor de variáveis com outras variáveis ou valores.

Para se fazer isso, referencia-se a variável usando #{VARIAVEL} e, automaticamente, a interpolação acontece. Para ficar mais claro, veja o exemplo:

```SCSS
$vert: top;
$horz: left;
$radius: 5px;
.rounded-#{$vert}-#{$horz} {
  border-#{$vert}-#{$horz}-radius: $radius;
}
```

Que gera:

```CSS
.rounded-top-left {
  border-top-left-radius: 5px;
}
```

***


## Mixins (argumentos)
Mixins permitem que se façam agrupamentos de declarações CSS para serem reusados onde se queira.
O primeiro para definir o mixin, em si; o segundo, para indicar em qual ponto do código se quer usá-lo.

```SCSS
@mixin border-radius($radius) {
  -webkit-border-radius: $radius;
  -moz-border-radius: $radius;
  -ms-border-radius: $radius;
  border-radius: $radius;
}
.box {
  @include border-radius(10px);
}
```

Isso gera:

```CSS
.box {
  -webkit-border-radius:10px;
  -moz-border-radius:10px;
  -ms-border-radius:10px;
  border-radius:10px;
}
```
***

### Extensão
é possível usar ```@extend``` para compartilhar
uma série de propriedades/valores de várias regras diferentes em uma mesma regra.

```CSS
.default-box {
  background-color: #efefef;
  border: 1px solid #000;
  color: #333;
}
.alert-box {
  @extend .default-box;
  font-size: 2em;
}
```

***

### Seletores placeholder
pode haver situações em que determinadas regras que serão estendidas só precisem existir para isso e não precisem estar presentes no CSS compilado. Para isso, saiba que existem o __seletores placeholder__.
Criar um placeholder selector é como uma regra comum, com a diferença de que não se coloca um elemento, classe ou ID, mas sim um %.

```SCSS
%bold {
  font-weight: bold;
}
%display-block {
  display: block;
}
.my-module {
  @extend %bold, %display-block;
  border: 1px solid #ccc;
}
```

***

### Importação
Para essas ocasiões, o Sass oferece um recurso de importação, usando ```@import```.

No exemplo de placeholder selectors mostrado agora há pouco, certamente haveria um arquivo Sass com todos eles e, conforme a necessidade e a organização do projeto por exemplo, o uso da metodologia SMACSS , a criação de mais arquivos para conterem as regras devidas.

Logo no início do arquivo style.scss bastaria colocar:

```SCSS
@import 'generics';
```
Tudo o que está dentro de ```_generics.scss``` poderia ser acessado. Não é preciso colocar o _ nem .scss na sintaxe de importação. Também é pos-
sível e, quase sempre, necessário importar vários arquivos, separando-os por
vírgula na declaração do ```@import```.

Neste ponto, cabem duas observações importantes. A primeira é que se deve ter atenção ao nome do arquivo que foi importado, que começa com um subtraço (underline). Dentro da dinâmica do Sass, isso é chamado de partial e significa que, na compilação, somente será gerado um arquivo CSS de style.scss . Em outras palavras, na compilação, partials não geram sua contraparte .css.
A segunda é que é importante não confundir esse @import com a importação de arquivos que já existe em CSS puro. Esta faz uma requisição extra no servidor, chamando um arquivo à parte; aquela junta todos os arquivos importados no importador, garantindo a geração de um arquivo único com
todas as regras.

**Por padrão, Sass não permite importar arquivos .css diretamente.**


***


### CSS namespaces
Tentando explicar de maneira simples e sucinta, namespaces são como regiões no código, nas quais nomes de variáveis, de funções etc. são válidos dentro destas linguagens de programação.
