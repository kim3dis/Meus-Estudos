import pyautogui

print("""\
=Spambot=

Uso:
-n	-----	Números
-p	-----	Palavras
""")
opcao = input("->")

if opcao == "-n":
	print("num")

if opcao == "-p":
	print("pal")
    # msg = input("Mensagem: ")
	while True:
		pyautogui.typewrite("teste")
        pyautogui.press('enter')
        
# a = 1
# for x in range(0, 3):
# 	a = str(a)
# 	pyautogui.typewrite(a)
# 	pyautogui.press('enter')
# 	a = int(a)
# 	a += 1
