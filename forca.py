import random

def jogo_forca():
    palavra_secreta = inicia()
    letras_acertadas = ['_' for i in palavra_secreta]
    enforcou = False
    acertou = False
    tentativas = 6
    chutes = []
    enforcado = forca(tentativas)

    while(not enforcou and not acertou):

        print(f'Seus chutes: {chutes}')
        print(enforcado)
        print(letras_acertadas)
        chute = input('Qual letra? ')
        chute = chute.strip()
        chute = chute.upper()
        if(chute in chutes):
            print("Voce já tentou essa letra cabaço!")
        else:
            chutes.append(chute)

            indice = 0

            for letra in palavra_secreta:
                if (chute == letra.upper()):
                    letras_acertadas[indice] = chute

                indice = indice + 1

            print('===============================')
            if (chute in letras_acertadas):
                print('Boa!')
            else:
                print('Ai não né paizão..')
                tentativas = tentativas - 1
                enforcado = forca(tentativas)


            acertou = not('_' in letras_acertadas)
            enforcou = tentativas == 0
            if(not enforcou and not acertou):print(f'Voce ainda tem {tentativas} tentativas')

    if(acertou):
        print(f'Parabéns você acertou, a palavra era {palavra_secreta}!!!')
        imprime_mensagem_vencedor()

    elif(enforcou):
        print(enforcado)
        print('Acabaram suas tentativas :(')
        print(f'A palavra era {palavra_secreta}...')
        imprime_mensagem_perdedor()

    print("Fim do jogo")

def inicia():
    print("===============================|")
    print("Bem vindo ao jogo de Forca!|")
    print("===============================|")

    arquivo = open("palavras.txt", "r")
    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

    arquivo.close()

    numero = random.randrange(0, len(palavras))

    palavra_secreta = palavras[numero].upper()

    return (palavra_secreta)

def forca(tentativas):
    if tentativas == 6:
        carinha_da_forca = '''______
|/   |
|    
|  
|   
|
|'''
    if tentativas == 5:
        carinha_da_forca = '''______
|/   |
|    0
|  
|
|
|'''
    if tentativas == 4:
        carinha_da_forca = '''______
|/   |
|    0
|    |
|   
|
|'''
    if tentativas == 3:
        carinha_da_forca = '''______
|/   |
|    0
|    |
|   / 
|
|'''
    if tentativas == 2:
        carinha_da_forca = '''______
|/   |
|    0
|    |
|   / \
|
|'''
    if tentativas == 1:
        carinha_da_forca = '''______
|/   |
|    0
|  --|
|   / \
|
|'''
    if tentativas == 0:
        carinha_da_forca = '''______
|/   |
|    0
|  --|--
|   / \
|
|'''

    return (carinha_da_forca)

def imprime_mensagem_perdedor():
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


if(__name__ == "__main__"):
    jogo_forca()