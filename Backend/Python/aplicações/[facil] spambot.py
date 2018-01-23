import pyautogui

print("""\
=Spambot=

Uso:
-n		
-t		

""")


a = 1
for x in range(0, 3):	
	a = str(a)	
	pyautogui.typewrite(a)
	pyautogui.press('enter')
	a = int(a)
	a += 1	
