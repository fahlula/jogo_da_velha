# Jogo da Velha

from colorama import Fore, Style, init
init(autoreset=True)

def colorir(valor):
    """Deixa X vermelho e O azul; números permanecem normais."""
    if valor == "X":
        return Fore.RED + valor + Style.RESET_ALL
    elif valor == "O":
        return Fore.BLUE + valor + Style.RESET_ALL
    return valor

def mostrar_tabuleiro(tab):
    """Desenha o tabuleiro maior com separadores."""
    for i, linha in enumerate(tab):
        print("     |     |    ")
        print(f"  {colorir(linha[0])}  |  {colorir(linha[1])}  |  {colorir(linha[2])}  ")
        print("     |     |    ")
        if i < 2:
            print("-----+-----+-----")
    print()

def verificar_vitoria(tab, j):
    """Checa linhas, colunas e diagonais para o jogador j."""
    # Linhas
    for i in range(3):
        if tab[i][0] == j and tab[i][1] == j and tab[i][2] == j:
            return True
    # Colunas
    for i in range(3):
        if tab[0][i] == j and tab[1][i] == j and tab[2][i] == j:
            return True
    # Diagonais
    if tab[0][0] == j and tab[1][1] == j and tab[2][2] == j:
        return True
    if tab[0][2] == j and tab[1][1] == j and tab[2][0] == j:
        return True
    return False

def posicao_para_indices(pos):
    """Converte posição 1-9 para (linha, coluna)."""
    pos -= 1
    return pos // 3, pos % 3

# Tabuleiro inicial
tabuleiro = [["1","2","3"],
             ["4","5","6"],
             ["7","8","9"]]

jogador_atual = "X"
jogadas_validas = 0  # conta só jogadas válidas

while True:
    mostrar_tabuleiro(tabuleiro)

    # Entrada do usuário com validação
    escolha = input(f"Jogador {colorir(jogador_atual)}, escolha uma posição (1-9): ").strip()
    if not escolha.isdigit():
        print(Fore.YELLOW + "Por favor, digite um número de 1 a 9.\n" + Style.RESET_ALL)
        continue

    pos = int(escolha)
    if pos < 1 or pos > 9:
        print(Fore.YELLOW + "Posição inválida. Use um número entre 1 e 9.\n" + Style.RESET_ALL)
        continue

    linha, coluna = posicao_para_indices(pos)

    if tabuleiro[linha][coluna] in ("X", "O"):
        print(Fore.YELLOW + "Posição já ocupada. Tente outra.\n" + Style.RESET_ALL)
        continue

    # Faz a jogada
    tabuleiro[linha][coluna] = jogador_atual
    jogadas_validas += 1

    # Verifica vitória
    if verificar_vitoria(tabuleiro, jogador_atual):
        mostrar_tabuleiro(tabuleiro)
        print(Fore.GREEN + f"Jogador {jogador_atual} venceu!" + Style.RESET_ALL)
        break

    # Verifica empate (tabuleiro cheio sem vencedor)
    if jogadas_validas == 9:
        mostrar_tabuleiro(tabuleiro)
        print(Fore.YELLOW + "Empate!" + Style.RESET_ALL)
        break

    # Alterna jogador
    jogador_atual = "O" if jogador_atual == "X" else "X"
