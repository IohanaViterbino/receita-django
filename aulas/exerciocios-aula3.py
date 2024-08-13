# nome e senha iguais
nome = input("Digite o nome do usuário: ")
while True:
    senha = input("Digite a senha: ")
    # if senha.upper() == nome.upper():
    if senha.upper() in nome.upper():
        print("Senha inválida.")
    else:
        print("Cadastro realizado!")
        break

# numero maior
num = float(input("Forneça um número: "))
maior = num
for i in range(4):
    num = float(input("Forneça um número: "))
    if num >= maior:
        maior = num
print(f"O maior valor fornecido foi {maior}")

# maiusculo
texto = input("Insira um texto: ")
print("O texto em maiúsculo é: ",texto.upper())

# caracter
texto_entrada = input("Insira um texto: ")
caractere = input("Insira o caractere a ser encontrado: ")

print(f"O caractere '{caractere}' foi encontrado {texto_entrada.count(caractere)} vezes no texto fornecido")