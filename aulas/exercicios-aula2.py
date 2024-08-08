# atv 1
import random
import time

x = int(input("Digite um número: "))
soma = 0

for i in range(x):
    numAle = random.randint(1, 10)
    soma += numAle
    # print(numAle)
print("Soma dos valores -> ",soma)

# atv 2
for i in range(20, 0, -1):
    print(i)
    time.sleep(1)

# atv 3
num = int(input("Insira o número da tabuada: "))

for i in range(1, 11):
    print(num,"X",i,"=",num*i)