valor1 = bool(int(input("Digite 1 para VERDADEIRO ou 0 para FALSO (primeiro valor): ")))
valor2 = bool(int(input("Digite 1 para VERDADEIRO ou 0 para FALSO (segundo valor): ")))

if valor1 and valor2:
    print("Ambos são VERDADEIROS.")
else:
    print("Ambos são FALSOS ou um deles é FALSO.")
