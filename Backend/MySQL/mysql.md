# MySQL

Fontes utilizadas:
- Curso em vídeo: Curso de MySQL;
- Udemy: PHP;

>Arquivos guardam tabelas; tabelas armazenam registros; registros são compostos por campos;

>Banco de dados são coleções de dados com caracteristícas separadas, porém estão organizados em locais específicos


# Criando e usando um banco de dados
No MySQL é simples, basta executar o código abaixo:
```mysql
CREATE DATABASE cadastro;
```

Após criar, não esqueça de selecionar o banco de dados para usar:
```mysql
USE cadastro;
```

# Criando uma tabela
Se para criar uma tabela foi ```CREATE DATABASE```, então para criar uma tabela será ```CREATE TABLE nomeTabela();```

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
A diferença entre os dois é que o **char** guarda caracteres fixos e o **varchar** guarda os variantes.
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