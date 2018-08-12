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

.grid-template-columns-3 {
	grid-template-columns: repeat(auto-fit, 100px);
	max-width: 600px;
}

.grid-template-columns-4 {
	grid-template-columns: repeat(auto-fit, minmax(100px, auto));
}

```