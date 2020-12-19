import random
import Menu

def jogar():
    numero = random.randrange(1,101)
    tentativas = 3
    rodada = 1
    pontos = 1000

    print("********************************")
    print("Bem vindo ao Jogo de Advinhação!")
    print("********************************")
    print("**Escolha o nivel de dificuldade**")
    print("(1) Facil (2) Médio (3) Dificíl")
    nivel = int(input("Qual o nivel desejado:"))

    while nivel > 3 or nivel < 1:
        print("Nivel invalido")
        nivel = int(input("Qual o nivel desejado:"))

    if (nivel == 1):
        tentativas = 20
    elif(nivel == 2):
        tentativas = 10
    else:
        tentativas = 5

    for rodada in range(tentativas + 1):
        print(f"Tentativa {rodada} de {tentativas}")
        chute = int(input("Digite um numero entre 1 e 100: "))

        if (chute < 1 or chute > 100):
            print("Numero invalido! Digite um numero entre 1 e 100")
            continue

        certo = numero == chute
        maior = numero < chute
        menor = numero > chute

        if(certo):
            print("Voce acertou!")
            break
        else:
            if(maior):
                print("Um pouco menos")
            if(menor):
                print("Um pouco mais")

        pontos = pontos - abs((chute - numero))
        if pontos < 0:
            print("Voce perdeu todos seus pontos")
            break

    print(f"O numero sorteado foi: {numero}")
    print(f"Seu total de pontos: {pontos}")

    print("Fim de jogo!")

    Menu.menu()

if (__name__ == "__main__"):
    jogar()