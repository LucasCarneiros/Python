soma = 0
contagem = 0
positivos = 0
negativos = 0

while True:
    valor = input("Digite um número (ou 'sair' para finalizar): ")
    if valor.lower() == 'sair':
        break
    valor = float(valor)
    soma += valor
    contagem += 1
    if valor > 0:
        positivos += 1
    elif valor < 0:
        negativos += 1

if contagem > 0:
    media = soma / contagem
else:
    media = 0

percentual_positivos = (positivos / contagem) * 100 if contagem > 0 else 0
percentual_negativos = (negativos / contagem) * 100 if contagem > 0 else 0

print(f"Média aritmética: {media:.2f}")
print(f"Positivos: {positivos}, Negativos: {negativos}")
print(f"Percentual de positivos: {percentual_positivos:.2f}%")
print(f"Percentual de negativos: {percentual_negativos:.2f}%")
