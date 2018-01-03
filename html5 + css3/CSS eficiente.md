# Conteúdo do livro: CSS Eficiente Técnicas e ferramentas que fazem a diferença nos seus estilos - Casa dos Códigos


## Superqualificando seletores
Seletores superqualificados fazem com que o navegador trabalhe mais do que precisa e deveria. Construa seletores mais enxultos e de alto desempenho, eliminando as partes desnecessárias.

Um exemplo, infelizmente, bastante comum:
``ul#nav li a {} ``
Já se sabe que, se o __a__ está dentro de __li__, que tem que estar dentro de __#nav__, de modo que é possível, eliminar o __li__ do seletor logo de cara. Como o __#nav__ é um ID, o elemento __ul__ também pode ser eliminado.

Então, uma forma melhor, mas ainda não ideal de se escrever, seria:
``#nav a {}``
