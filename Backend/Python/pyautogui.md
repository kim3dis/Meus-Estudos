# PyAutoGUI

## Sumário


## Instalação
### Windows
```shell
C:\Python34\pip.exe install pyautogui
```

### Linux
```bash
pip3 install python3-xlib
```

```bash
sudo apt-get install scrot
```

```bash
sudo apt-get install python3-tk
```

```bash
sudo apt-get install python3-dev
```

```bash
pip3 install pyautogui
```


***

## import 
```python
import pyautogui
```


***

## Funções
Basta fazer o ```import``` e chamar o pyautogui seguido da função.

### size
Essa função retorna o valor do monitor.

```python
tamanho_tela = pyautogui.size()
print(tamanho_tela)
```


### position
Essa função retorna a posição do mouse na tela.

```python
posicao_tela = pyautogui.position()
print(posicao_tela)
```


### moveTo
Essa função move o mouse para a posição indicada nos paramêtros, recebendo X (largura), Y (altura) e segundos para o mouse chegar no local. Essa última é opcional.

```python
pyautogui.moveTo(100, 200)
pyautogui.moveTo(none, 400, 3)
```


### moveRel
Essa função move o mouse para uma posição relativa a anterior. Como ```moveTo```, recebe três paramêtros e o último é opcional.

```python
pyautogui.moveRel(-200, 200, 2)
pyautogui.moveRel(500, -100, 3)

```


### dragTo e dragRel
Essa função é similar as outras duas anteriores, ```moveTo``` e ```moveRel```. A diferença é que ele move "segurando" alguma tecla. Exemplo, move o mouse até X local com o botão direito segurado.

```python
pyautogui.dragTo(200, 300, 1, button='left')
pyautogui.dragTo(300, 200, button='right')

pyautogui.dragRel(-300, 200, 2, button='right')
pyautogui.dragRel(-200, 400, button='left')
```


### animações no mouse
Há algumas animações que o mouse pode fazer até chegar o local especificado se adicionarmos. Abaixo tem uma lista de todos os tipos.

- linear (padrão)
- easeInQuad
- easeOutQuad
- easeInBounce
- easeInElastic

Abaixo como usar.

```python
pyautogui.moveTo(200, 70, 2, pyautogui.easeInQuad)
```


### click
Essa função ativa o clique do mouse com alguns paramêtros.

```python
pyautogui.click(900, 70)
pyautogui.click(x=100, y=55)
```

Podemos passar alguns outros paramêtros como:

#### button
```python
pyautogui.click(button='left')
pyautogui.click(button='middle')
pyautogui.click(button='right')
```

#### clicks
```python
pyautogui.click(clicks=2)
pyautogui.click(clicks=1, interval=0.50) #pode se adicionar um intervalo entre os clicks também
```

#### doubleClick e tripleClick()
```python
pyautogui.doubleClick()
```