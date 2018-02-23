# Ajax

## Sumário

## Fonte
Documentos: http://www.jack.eti.br/www/arquivos/apostilas/web/apostila_ajax.pdf

## O que é e não é Ajax?
Ajax não é uma framework, nem uma API, nem uma tecnologia em si. Ajax é uma funcionalidade implementada por um conjunto de objetos em JavaScript, sendo o mais importante chamado de XMLHttpResquest.
> XMLHttpRequest: trata uma requisição ou resposta do servidor com um documento XML DOM. Contém uma série de metódos que possibilita que o browser possa realizar requisições e receber respostas do servidor sem precisar atualizar a página em questão.

## Primeiros passos: Explicando um exemplo
```javascript
// parte 1
function chamaAjax() {
  var req;
  var isIE;

  if(window.XMLHttpRequest) {
    req = new XMLHttpRequest();
  } else if (window.ActiveXObject) {
    isIE = true;
    req = new ActiveXObject("Microsoft.XMLHTTP");
  }
  
  // parte 2
  var url = "ajax?nome=kim";
  req.onreadystatechange = processRequest;
  req.open("GET", url, true);
  req.send(null);

}

```
Com a parte 1 do código acima, teremos a variável ```req``` instânciada com um objeto ```XMLHttpRequest``` para qualquer browser.
Na parte 2, a tarefa de passar ao servidor, através do método http GET, os paramêtros para processamento. Após ```req.send(null)```, a requisição é transmitida.

**As outras propriedades do objeto XMLHttpsRequest serão explicadas mais a frente.**

```javascript
function processRequest() {
  if (req.readyState == 4) {
    if (req.status == 200) {
      var texto = req.responseText;
      alert("resposta = "+texto);
    }
  }
}
```
O método javascript acima é responsável por, simplesmente recuperar o texto enviado pelo servidor e mostrá-lo ao usuário.
