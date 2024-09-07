soma = 0

for i in range(1,500):
    if i  % 2 != 0 and i % 3 == 0:
        soma += i

print(f"A soma  de todos os números ímpares que são múltiplos de três e que se encontram no conjunto dos números de 1 até 500 é {soma}")