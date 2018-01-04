# Conteúdo do livro: CSS Eficiente Técnicas e ferramentas que fazem a diferença nos seus estilos - Casa dos Códigos


## Superqualificando seletores
Seletores superqualificados fazem com que o navegador trabalhe mais do que precisa e deveria. Construa seletores mais enxultos e de alto desempenho, eliminando as partes desnecessárias.


Um exemplo, infelizmente, bastante comum:

``ul#nav li a {} ``
Já se sabe que, se o __a__ está dentro de __li__, que tem que estar dentro de __#nav__, de modo que é possível, eliminar o __li__ do seletor logo de cara. Como o __#nav__ é um ID, o elemento __ul__ também pode ser eliminado.

Então, uma forma melhor, mas ainda não ideal de se escrever, seria:

``#nav a {}``



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



## SMACSS
* Base;
* Layout;
* Module (Módulo);
* State (Estado);
* Theme (Tema);



## Pré-processadores CSS
Um pré-processador é um programa que recebe texto e efetua conversões léxicas nele. As conversões podem incluir substituição de macros, inclusão condicional e inclusão de outros arquivos.

Quer dizer, você escreverá código na sintaxe do pré-processador de sua preferência e, através de alguns processos de conversão, ele transforma (ou compila) essa sintaxe específica e própria em código CSS, a que todos já estamos habituados. Caso contrário, não se teria nenhuma estilização, já que, para este fim, os navegadores precisam de arquivos .css.

### SASS e LESS
Sass e Less fornecem quase o mesmo acervo de funcionalidades. Há várias controvérsias e discussões acalouradas entre os adeptos de um e outro, mas a verdade é que, nessa quase conversão de características, ao optar por usar Sass ou Less, você estará bem servido e conseguirá melhorar muito a organização e workflow de desenvolvimento de estilos!

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
}```


### Referência ao ascendente
Em algumas situações, é preciso fazer referência ao ascendente para se montar uma regra apropriadamente. Por exemplo, dentro do aninhamento permitido por Sass, como seria para colocar uma regra com :hover ?
Para esses casos, Sass provê uma característica muito interessante, tornando possível fazer referência ao elemento ascendente imediatamente superior: o caractere &.

```SCSS
.selector {
  $:hover {

  }
}
```
Isso geraria: ```.selector:hover {}```

A intenção com **&** é repetir o seletor ascendente.


## Variáveis
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
