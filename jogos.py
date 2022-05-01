import forca
import adivinhacao
def menu():
    print ("===============================|")
    print ("Bem vindo aos jogos do Japoneis|")
    print ("===============================|")

    jogo = int(input("Selecione o jogo desejado - (1) Adivinhação | (2) Forca: "))

    if (jogo == 1):
        print('Jogo de Adivinhação selecionado...')
        adivinhacao.jogo_adivinhacao()

    elif (jogo == 2):
        print('Jogo de Forca selecionado...')
        forca.jogo_forca()

if(__name__ == "__main__"):
    menu()