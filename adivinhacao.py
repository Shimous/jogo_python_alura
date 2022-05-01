import random
def jogo_adivinhacao():
    print ("===============================|")
    print ("Bem vindo ao jogo de avinhação!|")
    print ("===============================|")

    NumeroSecreto = random.randrange(1,101)
    rodada = 1
    pontos = 1000

    dificuldade = int(input ("Escolha a dificuldade - 1 Fácil | 2 Médio | 3 Difícil: "))

    if (dificuldade == 1):
        print('dificuldade Fácil selecionada.')
        print("===============================|")
        total_tentativas = 20

    elif(dificuldade == 2):
        print('dificuldade Média selecionada.')
        print("===============================|")
        total_tentativas = 10

    elif (dificuldade == 3):
        print('dificuldade Dificil selecionada.')
        print("===============================|")
        total_tentativas = 5

    while (rodada <= total_tentativas):
        print(f"Tentativa {rodada} de {total_tentativas}")
        print("_______________________________")
        Chute = int(input ("Digite o seu número: "))

        print ("Você digitou", Chute)

        if (NumeroSecreto == Chute):
            print("Você acertou, o número secreto era {} e fez {} pontos! :D".format(NumeroSecreto, pontos))
            break

        else:
            pontos = pontos - abs(NumeroSecreto - Chute)
            if(NumeroSecreto < Chute):
                print("Você errou para cima ^ :[")
                print("===============================")

            if (NumeroSecreto > Chute):
                print("Você errou para baixo v :[")
                print("===============================")

        rodada = rodada + 1

    print("Fim do jogo")

if(__name__ == "__main__"):
    jogo_adivinhacao()