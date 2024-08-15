import math
# funções para resolver a lista

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
    f = (c * 1, 8) + 32
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
        return "igual"