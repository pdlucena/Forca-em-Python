# importando bibliotecas.
import random
import time
import os


def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')


def status(palavra_escondida, letras_adivinhadas, max_tentativas):
    print("Palavra sorteada:", ' '.join(palavra_escondida))
    print(f"\nLetras já tentadas: {', '.join(letras_adivinhadas)}")
    print(f"\nTentativas restantes: {max_tentativas}")


def jogo_forca():

    # criando uma lista de palavras que serão sorteadas.
    palavras = ["python", "programacao",
                "computador", "aula", "mouse", "variavel"]

    # escolhendo uma das palavras.
    palavra_sorteada = random.choice(palavras)

    # criando uma variavel que representa as letras.
    palavra_escondida = '_' * len(palavra_sorteada)

    # criando uma lista vazia para armazenar as letras já escolhidas.
    letras_adivinhadas = []

    # definindo o número máximo de tentativas.
    max_tentativas = 6

    while True:

        status(palavra_escondida, letras_adivinhadas, max_tentativas)

        # pedindo ao jogador para digitar uma letra.
        letra = str(input("\nDigite uma letra: ")).lower()

        if letra.isalpha() == False or len(letra) != 1:
            print(
                "\n\033[1;33mPor favor, digite apenas \033[4;33mUMA LETRA\033[0m\033[1;33m válida.\033[0m")
            time.sleep(2)
            limpar_tela()
            continue

        # verificando se a letra já foi digitada.
        if letra in letras_adivinhadas:
            print(
                "\n\033[1;33mVocê já digitou essa letra. Tente novamente.\033[0m")
            time.sleep(1.5)
            limpar_tela()
            continue

        letras_adivinhadas.append(letra)

        # verificando se a letra digitada está na palavra sorteada.
        if letra in palavra_sorteada:
            print(
                f"\n\033[1;32mLetra encontrada! Atualizando palavra...\033[0m")
            time.sleep(1)

            nova_palavra = []

            for indice in range(len(palavra_sorteada)):
                if letra == palavra_sorteada[indice]:
                    nova_palavra.append(letra)
                else:
                    nova_palavra.append(palavra_escondida[indice])
            palavra_escondida = ''.join(nova_palavra)

        else:
            max_tentativas -= 1
            print(
                f"\n\033[1;31mLetra não encontrada. Você tem mais {max_tentativas} tentativas!\033[0m")
            time.sleep(1.5)

        # verificando se o jogador venceu ou perdeu.
        if palavra_escondida == palavra_sorteada:
            limpar_tela()
            print("\033[1;32m👊🥳 Parabéns! Você venceu! 🎉🎊\033[0m")
            print(f"\n✅ A palavra era \033[1;36m{palavra_sorteada}\033[0m.")
            input("\nPressione a tecla ENTER para voltar ao menu.")
            time.sleep(0.5)
            limpar_tela()
            break

        elif max_tentativas == 0:
            limpar_tela()
            print("\033[1;31m💀😥 Que pena! Você perdeu. 👎🆘\033[0m")
            print(f"\n✅ A palavra era: \033[1;36m{palavra_sorteada}\033[0m.")
            input("\nPressione a tecla ENTER para voltar ao menu.")
            time.sleep(0.5)
            limpar_tela()
            break

        time.sleep(1.5)
        limpar_tela()

# para executar somente a forca ---> jogo_forca()

# criando um menu simples.


def menu_forca():

    while True:

        print("\033[1;45;37m=== Jogo da Forca ===")
        print("1 - Jogar")
        print("2 - Sair\033[0m")
        op = input("\nEscolha uma opção: ")

        if op == '1':
            print("\n\033[1;36mCarregando jogo...\033[0m")
            time.sleep(1.5)
            limpar_tela()
            jogo_forca()

        elif op == '2':

            print("\n\033[1;36m👍 Obrigado por jogar! Até a próxima. 😁\033[0m")
            break

        else:
            print("\n\033[1;31m❌ Opção inválida. Tente novamente.\033[0m")
            time.sleep(1.5)
            limpar_tela()
            continue


menu_forca()
