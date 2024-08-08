# código um
a = 1
b = 2

if a>b:
    print("="*20)
    print("A maior que B")
    print("="*20)
elif b == a:
    print("="*20)
    print("B igual a A")
    print("="*20)
else:
    print("="*20)
    print("B maior que A")
    print("="*20)

# código dois
n = int(input("digite um número: "))
if n > 0:
    print(n,"é maior que 0")
elif n < 0:
    print(n,"é menor que 0")
elif n == 0:
    print(n,"é igual a 0")
else:
    print("Não é um número.")