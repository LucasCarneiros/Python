pares = impares = soma_pares = soma_total = contagem = 0

while True:
    numero = int(input("Digite um número positivo (ou 0 para sair): "))
    if numero == 0:
        break
    contagem += 1
    soma_total += numero
    if numero % 2 == 0:
        pares += 1
        soma_pares += numero
    else:
        impares += 1

media_pares = soma_pares / pares if pares > 0 else 0
media_geral = soma_total / contagem if contagem > 0 else 0

print(f"Quantidade de pares: {pares}, ímpares: {impares}")
print(f"Média dos pares: {media_pares:.2f}")
print(f"Média geral: {media_geral:.2f}")
