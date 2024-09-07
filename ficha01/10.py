A = int(input("Digite o valor de A: "))
fatorial = 1

print(f"{A}! = ", end="")
for i in range(A, 0, -1):
    fatorial *= i
    if i > 1:
        print(f"{i} x ", end="")
    else:
        print(f"{i} = {fatorial}")
