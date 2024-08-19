import math
# funções para resolver cada questão da lista

def soma(n1, n2):
    return n1 + n2

def media(n1, n2, n3, n4):
    m = (n1 + n2 + n3 + n4)/4
    return m

def converter_em_centimetros(metros):
    return metros/100

def area_circulo(r):
    area = math.pi * (r ** 2)
    return area

def area_quadrado_dobro(l):
    area = (l ** l) * 2
    return area

def calcular_hora_mes(hr_ganha, hr_trab_mes):
    salario = hr_ganha * hr_trab_mes
    return salario

def celsius_p_fahr(c):
    f = (c * 1.8) + 32
    return f

def fahr_p_celsius(f):
    c = 5 * ((f-32) / 9)
    return c

def maior_dois(n1, n2):
    if n1 > n2:
        return n1
    elif n2 > n1:
        return n2
    else:
        return "os dois"
    
def positivo_negativo(num):
    if num>0:
        return "positivo"
    else:
        return "negativo"
    
def sexo_letra(char):
    if char.upper() == "F":
        return "F - Feminino"
    elif char.upper() == "M":
        return "M - Masculino"
    else:
        return "Sexo Inválido"

def vogal_consoante(char):
    vogais = ["a","i","e","o","u"]
    consoantes = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']
    if char.lower() in vogais:
        return "vogal"
    elif char.lower() in consoantes:
        return "consoante"
    else:
        return "inválido"
    

def aprovacao(n1, n2):
    m = (soma(n1,n2))/2
    if m >= 10:
        return "Aprovado com Distinção"
    elif m >=7:
        return "Aprovado"
    elif m < 7:
        return "Reprovado"

def validacao(nome, idade, salario, sexo, est_civil):
    val_nome = len(nome) > 3
    val_idade = 0 <= idade <= 150
    val_salario = salario > 0
    val_sexo = sexo_letra(sexo)
    val_estado = est_civil in ['s', 'c', 'v', 'd']

    if val_nome is True and val_estado is True and val_idade is True and val_salario is True and val_sexo != "Sexo Inválido":
        return "Os dados conferem!"
    else:
        return "Dado inválido!"
    
def imprimir_num():
    print("Um abaixo do outro: ")
    for i in range(1,21):
        print(i)
    p = ""
    for i in range(1,21):
        p += str(i) + " "
    print("ao lado: \n"+p)

def soma_media(n1,n2,n3,n4,n5):
    s = n1 + n2 + n3 + n4 + n5
    m = s / 5
    print("soma dos números:",s)
    print("média dos números:",m)

def impares():
    for i in range(1,51):
        if i%2==1:
            print(i)

def intervalo(n1, n2):
    for i in range(n1,n2):
        print(i)

def soma_tres(n1,n2,n3):
    s = soma(n1,n2)+n3
    return s

def p_n(n1):
    if positivo_negativo(n1) == 'positivo':
        print("P")
    else:
        print("N")

def somaImposto(taxa_P, custo):
    precotx = ((taxa_P /100) * custo) + custo
    return precotx

def comparacao_string(txt1, txt2):
    print(f'Tamanho de "{txt1}": {len(txt1)}')
    print(f'Tamanho de "{txt2}": {len(txt2)}')

    if len(txt1) != len(txt2):
        print("As duas strings são de tamanhos diferentes.")
    else:
        print("As duas strings são de tamanhos iguais.")

    if txt2 == txt1:
        print("As duas strings possuem conteúdo iguais.")
    else:
        print("As duas strings possuem conteúdo diferente.")

def nome_contrario(nome):
    n_novo = nome[::-1].upper()

    return n_novo

def nome_v(nome):
    for i in nome:
        print(i.upper())

# entrada e chamada das funções

print("1- soma")
n1 = int(input("digite um numero "))
n2 = int(input("digite um numero "))
print("Soma dos números é",soma(n1, n2),"\n")

print("2- média 4 notas")
nota1 = float(input("digite uma nota "))
nota2 = float(input("digite uma nota "))
nota3 = float(input("digite uma nota "))
nota4 = float(input("digite uma nota "))
print("A média é",media(nota1, nota2, nota3, nota4),"\n")

print("3- centimetros")
metros = float(input("digite em metros "))
print("{metros}m em centimetros é",converter_em_centimetros(metros),"\n")

print("4- raio")
r = float(input("digite o raio de um circulo "))
print("A area do circulo é",area_circulo(r),"\n")

print("5- Quadrado")
q = float(input("digite o lado do quadrado "))
print("O dobro da area do quadrado é",area_quadrado_dobro(q),"\n")

print("6- salario")
hrg = float(input("digite o valor hora "))
hrt = float(input("digite de horas trabalhadas "))
print("O salario do mês é",calcular_hora_mes(hrg, hrt),"\n")

print("7- celsius")
f = float(input("digite a temperatura fahrenheit "))
print("A temperatura em celsius é",fahr_p_celsius(f),"\n")

print("8- fahrenheit")
c = float(input("digite a temperatura celsius "))
print("A temperatura em fahrenheit é",celsius_p_fahr(c),"\n")

print("9- maior")
n1 = float(input("digite um numero "))
n2 = float(input("digite um numero "))
print("O maior número:", maior_dois(n1,n2),"\n")

print("10- positivo/negativo")
pn = float(input("digite um numero "))
print("O valor é ",positivo_negativo(pn),"\n")

print("11- f ou m")
letra = input("digite uma letra ")
print(sexo_letra(letra),"\n")

print("12- vogal ou consoante")
letra2 = input("digite uma letra ")
print(vogal_consoante(letra2),"\n")

print("13- aprovacao")
n1 = float(input("digite uma nota "))
n2 = float(input("digite uma nota "))
print(aprovacao(n1,n2),"\n")

print("14- validacao")
nome = input("digite um nome ")
idade = int(input("digite uma idade "))
sal = float(input("digite o salario "))
sexo = input("digite o sexo ")
est = input("digite o estado civil ")
print(validacao(nome, idade, sal, sexo, est),"\n")

print("15- imprimir 1 a 20")
imprimir_num()

print("\n16- soma e media")
n1 = float(input("digite uma nota "))
n2 = float(input("digite uma nota "))
n3 = float(input("digite uma nota "))
n4 = float(input("digite uma nota "))
n5 = float(input("digite uma nota "))
soma_media(n1,n2, n3, n4, n5)

print("\n17- imprimir impar")
impares()

print("\n18- intervalo")
n1 = int(input("digite um numero "))
n2 = int(input("digite um numero maior que o anterior "))
intervalo(n1,n2)

print("\n19- soma de 3")
n1 = int(input("digite um numero "))
n2 = int(input("digite um numero "))
n3 = int(input("digite um numero "))
print("O total é",soma_tres(n1,n2,n3),"\n")

print("20- p/n")
pn = float(input("digite um numero "))
p_n(pn)

print("\n21- imposto")
tx = float(input("digite a taxa "))
custo = float(input("digite o custo "))
print("O preço com imposto é ",somaImposto(tx, custo),"\n")

print("\n22- comparacao")
txt1 = input("digite uma frase ")
txt2 = input("digite uma frase ")
comparacao_string(txt1, txt2)

print("\n23- invertido maisculo")
txt1 = input("digite um nome ")
print("O nome ao contário é",nome_contrario(txt1),"\n")

print("24- nome vertical")
txt1 = input("digite um nome ")
nome_v(txt1)