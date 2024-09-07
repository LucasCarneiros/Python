intervalo_0_25 = 0 
intervalo_26_50 = 0
intervalo_51_75 = 0
intervalo_76_100 = 0

while True:
    numero = float(input("Digite qualquer numero"))
    if numero < 0:
        print("Numero negativo, entrada de numeros terminada")
        break
    elif numero >= 0 and numero <= 25:
        intervalo_0_25 += 1
    elif numero >= 26 and numero <= 50:
        intervalo_26_50 += 1
    elif numero >= 51 and numero <= 75:
        intervalo_51_75 += 1
    elif numero >= 76 and numero <= 100:
        intervalo_76_100 += 1
    
print(f"Esse é a quantidade numeros no intervalos entre 0 e 25 é {intervalo_0_25}")
print(f"Esse é a quantidade numeros no intervalos entre 26 e 50 é {intervalo_26_50}")
print(f"Esse é a quantidade numeros no intervalos entre 51 e 75 é {intervalo_51_75}")
print(f"Esse é a quantidade numeros no intervalos entre 76 e 100 é {intervalo_76_100}")
        