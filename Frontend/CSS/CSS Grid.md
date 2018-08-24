# CSS GRID

## display

```css
.grid {
	display: grid;
}
```

## Grid Container
### grid-template-columns
```HTML
<section class="grid grid-template-columns-1">
	<div class="items">1</div>
	<div class="items">2</div>
	<div class="items">3</div>
</section>
```

```css

.grid-template-columns-1 {
	.grid-template-columns: 1fr 3fr 1fr; 
}

.items {
	margin: 5px;
	background: tomato;
	text-align: center;
	font-size: 1.5em;
}

```


#### repeat();
>Não há necessidade de escrever várias colunas. Basta usar um repetidor.

```CSS

.grid-template-columns-2 {
	grid-template-columns: 2fr repeat(3, 1fr) 2fr;
}

```

##### auto-fit
>coloca o máximo que der em um espaço

Com o auto-fit é possível criar realmente layouts responsivos.

```CSS

.grid-template-columns-1 {
	grid-template-columns: repeat(auto-fit, 100px);
	max-width: 600px;
}

.grid-template-columns-2 {
	grid-template-columns: repeat(auto-fit, minmax(100px, auto));
}

```


### grid-template-rows

```HTML
<section class="grid grid-template-rows-1">
	<div class="items">1</div>
	<div class="items">2</div>
	<div class="items">3</div>
</section>
```

```css

.grid-template-rows-1 {
	.grid-template-rows: 50px 100px 50px 200px; 
}

.items {
	margin: 5px;
	background: tomato;
	text-align: center;
	font-size: 1.5em;
}

```



### Grid-template-columns + rows
```css
.grid-template-rows-1 {
	.grid-template-columns: 100px auto 50px;
	.grid-template-rows: 50px 200px 50px; 
}
 
.items {
	margin: 5px;
	background: tomato;
	text-align: center;
	font-size: 1.5em;
}

```


### Grid-template-areas
```HTML
<section class="grid grid-template-areas-1">
	<div class="items logo">logo</div>
	<div class="items nav">nav</div>
	<div class="items nav">nav</div>
	<div class="items sidenav">sidenav</div>
	<div class="items content">content</div>
	<div class="items advert">advert</div>
	<div class="items sidenav">sidenav</div>
	<div class="items footer">footer</div>
	<div class="items footer">footer</div>

	
</section>
```


```css

/* definir estrutura */
.grid-template-areas-1 {
	grid-template-areas: 
	"logo nav nav"
	"sidenav content advert"
	"sidenav footer footer"
	;
}

/* definir localização */
.logo {
	grid-area: logo;
}
.nav {
	grid-area: nav;
}
.sidenav {
	grid-area: sidenav;
}
.content {
	grid-area: content;
}
.advert {
	grid-area: advert;
}
.footer {
	grid-area: footer;
}


.items {
	margin: 5px;
	background: tomato;
	text-align: center;
	font-size: 1.5em;
}

```
