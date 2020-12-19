import advinhacao
import Forca

def menu():

    print("********************************")
    print("**Bem vindo ao menu de Jogos!***")
    print("********************************")
    print("********Escolha um jogo**********")
    print("*(1) Advinação (2) Forca (3)Sair*")
    escolha = int(input("Qual o jogo desejado:"))

    if (escolha == 1):
        advinhacao.jogar()
    if (escolha == 2):
        Forca.jogar()
    if (escolha == 3):
        print("Obrigado por ter jogado!!!!")

if (__name__ == "__main__"):
    menu()