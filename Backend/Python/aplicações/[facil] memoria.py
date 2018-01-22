import random

parar = False

while parar == False:
        valor = random.randint(0,9)
        print(valor)
        tentar = int(input())


        def converter4str(inteiro):
                return str(inteiro)

        valor = converter4str(valor)
        tentar = converter4str(tentar)
        nivel = 1

        while valor == tentar:
                alt_valor = random.randint(0,9)
                alt_valor = converter4str(alt_valor)
                valor = valor + alt_valor
                nivel += 1

                print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
                print("Nível: " + converter4str(nivel))
                print(alt_valor)
                
                alt_tentar = int(input())
                alt_tentar = converter4str(alt_tentar)
                tentar = alt_tentar

                print("A sequência era:   " + valor)
                print("Sua tentativa foi: " + tentar)
                
        continuar = input("Quer continuar? (s/n)")
        if continuar == "n":
                parar = False
                break
