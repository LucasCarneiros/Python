N = int(input("Digite um valor para N (1 a 10): "))

if 1 <= N <= 10:
    for i in range(11):
        print(f"{i} x {N} = {i * N}")
else:
    print("Valor inválido. Insira um número entre 1 e 10.")
