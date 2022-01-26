from datetime import datetime
import os
import Janelas as J
class Login:
    def verificar(self):
        if J.Login().iniciar() == True: return Menu().principal()
        else:
            Login().verificar()

#     def login(self):
#         nome=input()

class Menu:
    def __init__(self):
        self.ITENS={"cafe":{"preço":2,"unidades":12.0},"feijao":{"preço":7,"unidades":5.0}}

    def principal(self):
        print("Menu principal:")
        print("1-Mostrar estoque")
        #print("2-Carregar itens de arquivo .txt")
        opcao=int(input())
        if opcao==1:
            self.operacao()
        #elif opcao==2:
        #    Atualizacao().carregar(self.ITENS)

    def operacao(self):
        self.printar(self.ITENS)
        print("0-voltar ao menu anterior")
        print("1-adicionar")
        print("2-editar")
        print("3-remover")
        opcao=int(input())
        print()
        if opcao==0:
            self.principal()
        elif opcao==1:
            Edicao().adicionar(self.ITENS)
            self.operacao()
        elif opcao == 2:
            Edicao().editar(self.ITENS)
            self.operacao()
        elif opcao == 3:
            Edicao().apagar(self.ITENS)
            self.operacao()

    def printar(self,lista):
        print("Itens:")
        for c in lista:
              print("{} - {}:{}; {}:{}".format(c,"preço",lista[c]["preço"],"unidades",lista[c]["unidades"]))
        print()

class Edicao:
    # def __init__(self):
    #     self.ITENS=Menu().ITENS

    def adicionar(self,ITENS):
        chave=input("Chave: ")
        if chave in ITENS:
            print("Este item já exite, tente editá-lo!\n")
        else:
            unidades=float(input("Unidades: "))
            preco=float(input("preco: "))
            ITENS[chave]={"unidades":unidades,"preço":preco}
            print("Item adicionado com sucesso!\n")
        return ITENS

    def editar(self,ITENS):
        chave = input("Chave: ")
        if chave in ITENS:
            print("Valores atuais",ITENS[chave])
            unidades = float(input("Unidades: "))
            preco = float(input("preco: "))
            ITENS[chave]={"unidades":unidades,"preço":preco}
        else: print("O item digitado ainda não foi registrado!\n")
        return ITENS

    def apagar(self,ITENS):
        chave = input("Chave: ")
        if chave in ITENS:
            del ITENS[chave]
            print("Item excluido com sucesso!\n")

        else: print("O item digitado ainda não foi registrado!\n")
        return ITENS
# class Atualizacao:
#     def __init__(self):
#         pass
#
#     def carregar(self,itens):
#         nome=input("Insira o nome do arquivo com sua extenção (ex: texto.txt): ")
#         if os.path.isfile(nome) == True:
#             arquivo=open(nome,"r")
#             #json.dumps()
#         #with open(nome, encoding='utf-8') as meu_json:
#             #dados = json.load(meu_json)
#         for c in arquivo:
#             print(c)
#         else:
#             print("File not found!")
#             Menu().principal()
#
#Login().verificar()
if __name__ == '__main__':
    Menu().principal()
