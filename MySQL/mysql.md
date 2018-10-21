# MySQL
Fontes utilizadas:
- Curso em vídeo: Curso de MySQL;
- Udemy: PHP;
- Learning PHP, MySQL, Javascript and CSS [Robin Nixon]

>Arquivos guardam tabelas; tabelas armazenam registros; registros são compostos por campos;



# Criando e usando um banco de dados
Banco de dados são coleções de dados com caracteristícas separadas, porém estão organizados em locais específicos.
No MySQL é simples, basta executar o código abaixo:
```mysql
CREATE DATABASE cadastro;
```

Após criar, não esqueça de selecionar o banco de dados para usar:
```mysql
USE cadastro;
```

# Criando uma tabela
Se para criar um banco de dados
 foi ```CREATE DATABASE```, então para criar uma tabela será ```CREATE TABLE nomeTabela();```

```mysql
CREATE TABLE pessoas(
	nome varchar(30),
	idade tinyint,
	sexo char(1),
	peso float,
	altura float,
	nacionalidade varchar(20)
);
```

# Tipos primitivos
Temos 4 tipos primitivos, mas com algumas subdivisões.

__Númericos:__ Inteiro, Real e Lógico;
__Data/Tempo:__ Date, DateTime, TimeStamp, Time, Year;
__Literal:__ Caractere, Texto, Binários e Coeleções;
__Espacial:__ Geometry, Point, Polygon, MultiPolygon;

Dessas subdivisões, temos mais subdivisões:
#### Númericos:
__Inteiro:__ TinyInt, SmallInt, Int, MediumInt, BigInt;
__Real:__ Decimal, Float, Double, Real;
__Lógico:__ Bit, Boolean;

#### Literal:
__Caractere:__ char e varchar;
A diferença entre os dois é que o **char** guarda caracteres fixos e o **varchar** guarda os variantes;
__Texto:__ TinyText, Text, MediumText, LongText;
__Binário:__ TinyBlob, Blob, MediumBlob, LongBlob;
__Coleção:__ Enum e Set;

# Descrevendo a tabela
Usa-se o comando ```describe nomeTabela;``` para fazer uma descrição de uma tabela, incluindo os nomes das colunas, os tipos, se estão vazias, etc.

```mysql
describe pessoas; 
```

# A falta do primary key
A ausência do ```primary key``` pode acarretar a duplicação do cadastro em uma tabela. Esse cadastro pode ser criado inúmeras vezes com as mesmas informações. Ou seja, em uma tabela com informações sobre pessoas pode acontecer de existir as mesmas informações sobre a mesma pessoa inúmeras vezes por ter sido inserida mais de uma vez.

# Melhorias na tabela
```mysql
id int NOT NULL AUTO_INCREMENT,
nome varchar(30) NOT NULL,
nascimento date,
sexo enum('M', 'F'),
peso decimal(5,2),
altura decimal(3,2),
nacionalidade varchar(20) DEFAULT 'Brasil',
PRIMARY KEY (id)
) DEFAULT CHARSET = utf8;
```

# Inserindo dados na tabela e os visualizando

Para inserir basta usar dois comandos: ```INSERT INTO nomeTabela()``` e ```VALUES()```
```mysql
INSERT INTO pessoas (nome, nascimento, sexo, peso, altura, nacionalidade) VALUES ('kim', '1500-01-01', 'M', '30.4', '3.90', 'Portugal');
```

```mysql
UPTADE tb_usuarios SET dessenha = '123456' WHERE idusuario = 1;
```


# SELECT
Para visualizar usamos o ```SELECT * FROM nomeTabela```.
>O * representa "tudo" na tabela
```mysql
SELECT * FROM pessoas;
```


# SELECT DISTINCT
Como o nome já diz, seleciona apenas linhas distintas, ou seja, linhas que se diferem / que não são iguais.

```mysql
SELECT DISTINCT FROM pessoas;
```


>Se você estiver inserindo dados na tabela e for exatamente a ordem definida da tabela, podemos omitir o primeiro parentêse.
```mysql
INSERT INTO pessoas VALUES ('kim', '1500-01-01', 'M', '30.4', '3.90', 'Portugal');
```
Dessa forma fica mais simples ainda.

Ainda sim, podemos inserir multiplos dados de um só vez.
```mysql
INSERT INTO pessoas VALUES (DEFAULT, 'João', '1730-12-18', 'M', '80.6', '1.60', 'Irlanda'),
(DEFAULT, 'Adalberto', '1790-10-24', 'M', '88.2', '1.84', 'Brasil'),
(DEFAULT, 'Maria', '1840-8-1', 'F', '65', '2', 'Alemanha');
```

# LIMIT
O ```LIMIT``` deixa você escolher quantas linhas retornarão na query e/ou de onde iniciar.

```mysql
SELECT nome FROM pessoas LIMIT 3;
SELECT nome FROM pessoas LIMIT 2, 3;
```
>Quando dado 2 parametros, o primeiro significa: pule este número de resultados; o segundo é quanto após pular devem ser retornados.


# Alterar a estrutura da tabela
## Adicionar colunas
```mysql
ALTER TABLE pessoas ADD COLUMN profissao VARCHAR(10);
```
**Mas o que acontece com os dados já inseridos na tabela?**
Continuam lá, acontece que só será acrescentado mais uma coluna, e para os dados já existentes, nesta coluna será adicionado um null.

## Remover colunas
```mysql
ALTER TABLE pessoas
DROP COLUMN profissao;
```

## Escolhendo posição da coluna
```mysql
ALTER TABLE pessoas
ADD COLUMN profissao VARCHAR(10) AFTER nome;
```

Após a coluna nome, ele adicionará a coluna profissão.

**Se existe o AFTER, também existe o BEFORE, certo?**
Errado. Caso você queira adicionar uma coluna antes da primeira, que aqui no caso é "nome", usamos o comando abaixo:
```mysql
ALTER TABLE pessoas
ADD COLUMN profissao VARCHAR(10) FIRST;
```

## Modificando definições
```mysql
ALTER TABLE pessoas
MODIFY COLUMN profissao VARCHAR(20) NOT NULL DEFAULT '';
```
O DEFAULT foi adicionado vazio, pois há um conflito com o NOT NULL. Se lembrarmos, quando se cria uma coluna nova havendo dados na tabela, essa coluna, por padrão, terá valor null. Adicionando o NOT NULL como paramêtro a este campo gera um conflito. Assim, para evitar isso, colocamos que, por padrão, quando não houver inserção neste campo, ele não ser null, mas será '' (vazio sem ser null).

## Renomeando colunas
```mysql
ALTER TABLE pessoas
CHANGE COLUMN profissao prof VARCHAR(20);
```

>Colocando novos paramêtros, ele perderá os antigos como NOT NULL DEFAULT '', para manter, basta não adicionar nada após o novo nome.

## Renomeando a tabela
```mysql
ALTER TABLE pessoas
RENAME TO robos;
```

## Adicionando mais uma tabela
```mysql
CREATE TABLE IF NOT EXISTS cursos (
	nome varchar(30) NOT NULL UNIQUE,
	descricao text,
	carga int UNSIGNED,
	totaulas int UNSIGNED,
	ano year DEFAULT '2018'
) DEFAULT CHARSET = utf8;
```

>IF NOT EXISTS: __Se não existir__ a tabela 'cursos', crie uma

>UNIQUE: Não deixa colocar dois valores com dados iguais

>UNSIGNED: Sem sinal. Como negativo (-).

## Adicionando chave primária
```mysql
ALTER TABLE cursos
ADD COLUMN idcursos INT FIRST;

ALTER TABLE cursos
ADD PRIMARY KEY(idcurso);
```

## Apagar tabela
```mysql
CREATE TABLE IF NOT EXISTS teste(teste int);
DROP TABLE IF EXISTS teste;
```