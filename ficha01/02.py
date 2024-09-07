alturas = []


for i in range(15):
    altura = float(input(f"Digite a altura da pessoa {i+1}: "))
    alturas.append(altura)


menor_altura = min(alturas)
maior_altura = max(alturas)


print(f"A menor altura do grupo é: {menor_altura:.2f} metros")
print(f"A maior altura do grupo é: {maior_altura:.2f} metros")
