import random
import Menu
def jogar():
    acertou = False
    enforcou = False
    errou = 0

    palavra_secreta = carrega_arquivo_palavras(arquivo = "palavras.txt")
    letras_acertadas = carrega_acertos(palavra_secreta)
    imprime_mensagem_boas_vindas()


    while (not acertou and not enforcou):

        chute = solicita_chute(letras_acertadas)

        if (chute in palavra_secreta):
            letras_acertadas = letra_correta(chute,letras_acertadas,palavra_secreta)
        else:
            errou += 1
            desenha_forca(errou)

        enforcou = errou == 7
        acertou = '_' not in letras_acertadas

    if (acertou):
        imprime_mensagem_vencedor()
    else:
        imprime_mensagem_perdedor(palavra_secreta)

    Menu.menu()


#---------------------------------------------------------------------------------------------

def imprime_mensagem_boas_vindas():
    print("********************************")
    print("Bem vindo ao Jogo da forca!")
    print("********************************")
#-----------------------------------------------------------------------------------------------

def carrega_arquivo_palavras(arquivo):
    lista_de_palavras = []
    palavras = open(arquivo, "r")

    for palavra in palavras:
        palavra = palavra.strip()
        lista_de_palavras.append(palavra)

    palavras.close()

    indice = random.randrange(0,len(lista_de_palavras))
    palavra_secreta = lista_de_palavras[indice].upper()

    return palavra_secreta
#__________________________________________________________________________________________________

def carrega_acertos(palavra_secreta):
    acertos = ['_' for letra in palavra_secreta]
    return acertos
#__________________________________________________________________________________________________

def solicita_chute(letras_acertadas):
    print(letras_acertadas)
    chute = input("Chute uma letra: ")
    chute = chute.strip().upper()
    return chute
#__________________________________________________________________________________________________
def letra_correta(chute,letras_acertadas,palavra_secreta):
    index = 0
    for letra in palavra_secreta:
        if (letra == chute):
            letras_acertadas[index] = letra
        index += 1

    return letras_acertadas
#---------------------------------------------------------------------------------------------------
def imprime_mensagem_vencedor():
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")

#__________________________________________________________________________________________________
def imprime_mensagem_perdedor(palavra_secreta):
    print("Puxa, você foi enforcado!")
    print("A palavra era {}".format(palavra_secreta))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")
#__________________________________________________________________________________________________
def desenha_forca(errou):
    print("  _______     ")
    print(" |/      |    ")

    if(errou == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(errou == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(errou == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(errou == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(errou == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(errou == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (errou == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()









if (__name__ == "__main__"):
    jogar()
