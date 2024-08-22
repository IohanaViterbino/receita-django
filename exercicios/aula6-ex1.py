from typing import Any


class Produto:
    qtdProd = 0

    def __init__(self, cod, preco):
        self.__cod = cod
        self.__preco = preco
        Produto.qtdProd += 1

    def cod_produto(self):
        return self.__cod
    def mudar_cod(self, valor):
        self.__cod = valor

    def preco_produto(self):
        return self.__preco
    def atualizar_preco(self, valor):
        if valor > 0.0:
            self.__preco = valor
        else:
            print( "Digite um valor válido.")
          
    def mostrar_quantidade(self):
        print(f"A quantidade de produtos em estoque são de {Produto.qtdProd}")    

        
if __name__ == "__main__":
    prod1 = Produto(cod=12457, preco=23.65)
    prod2 = Produto(cod=12432, preco=26.80)
    prod3 = Produto(cod=12472, preco=25.80)
    prod1.mostrar_quantidade()

    print(prod1.qtdProd)
