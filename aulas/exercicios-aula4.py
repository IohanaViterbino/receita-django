# função
# def soma(n1, n2):
#     '''essa função soma dois valores númericos recebidos'''

#     c=n1+n2
#     return f"Esta é a soma de {n1} + {n2} = {c}"

# num1 = int(input("numero 1: "))
# num2 = int(input("numero 2: "))
# print(soma(num1, num2), "\n")

# fun de contar
def contar_carateres(txt, char):
    print(f"O caractere '{char}' foi encontrado {txt.count(char)} vezes no texto fornecido")

entrada_txt = input("Insira um texto: ")
caractere = input("Insira o caractere a ser encontrado: ")
contar_carateres(entrada_txt, caractere)