peso = float(input("Digite o peso (em kg): "))
altura = float(input("Digite a altura (em metros): "))

IMC = peso / (altura ** 2)

print(f"Seu IMC é: {IMC:.2f}")

if IMC < 18.5:
    print("Condição: Abaixo do peso")
elif 18.5 <= IMC < 25:
    print("Condição: Peso normal")
elif 25 <= IMC < 30:
    print("Condição: Acima do peso")
else:
    print("Condição: Obeso")
