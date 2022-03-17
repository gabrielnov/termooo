from random import randint
import os
import time

def clear_console():
    command = 'clear'
    if os.name in ('nt', 'dos'):
        command = 'cls'
    os.system(command)

def save_ranking(total_time, player, tries, word):
    f = open('scores.txt', 'a')
    minutes =total_time/60
    player = player[0:20]
    f.write(f'{tries};{minutes:.2f};{player};{word}\n')
    f.close()

def finish_game(total_time, player, tries, word):
    save_ranking(total_time, player, tries, word)

    clear_console()
    print(f'\n\t\t === Parabéns! === \n\n {player}, você acertou o termo {word.upper()} com {tries} tentativas\n\n')
    input("Aperte qualquer tecla para voltar ao menu...")
    headers()

def output(guess, marks):
    clear_console()
    lines.append(guess)
    lines.append(marks)
    for i in range(len(lines)):
        if i % 2 == 0:
            print()
        for j in range(5):
            print(f" | {lines[i][j].upper()}", end = '')
        print(' |')

def verify_guess(guess, word):
    l_word = list(word)
    l_guess = list(guess)
    marks = ['x'] * 5
    for i in range(5):
        if l_guess[i] == l_word[i]:
            marks[i] = '^'
        for j in range(5):
            if j != i and l_guess[i] == l_word[j]:
                if marks[i] != '^':
                    marks[i] = '!'
    return marks

def valid_guess(guess):
    if guess == '':
        return False
    l_guess = list(guess)
    if len(l_guess) != 5:
        print("Digite uma palavra com apenas 5 letras")
        return False
    elif not find_word(guess):
        print("Palavra inválida, tente novamente")
        return False
    else:
        return True

def find_word(word):
    for w in content:
        if word == w:
            return True
    return False

def run_game(start, player, word):
    print(f'palavra sorteada: {word}')
    for t in range(1, 7):
        print(f"\n\t === Tentativa {t}/6 ===")
        guess = ''
        while not valid_guess(guess):
            guess = input("\nSua tentativa: ")
            guess = guess.lower()
            guess = guess.strip()
        marks = verify_guess(guess, word)
        output(list(guess), marks)

        if guess == word:
            total_time = time.time() - start
            finish_game(total_time, player, t, word)
            return
    print(f'\n\nFim das tentativas. A palavra era {word}.')
    input("\n\nAperte qualquer tecla para voltar ao menu...")
    headers()

content = []
def draw_word():
    f = open('words.txt')
    for line in f:
        if len(list(line)) == 6:
            content.append(line.replace("\n", ""))
    f.close()
    word = content[randint(0, len(content))]
    return word

def start_game(player):
    global lines
    lines = []
    clear_console()
    word = draw_word()
    start = time.time()
    run_game(start, player, word)

def show_ranking():
    scores = open('scores.txt', 'r')
    first_line = True 
    for line in scores:
        tries, time, player, word = line.split(';')
        if first_line:
            print(f'\t{tries: <11} | {time: <17} | {player: <20} | {word}', end='')
            print('\t', end='')
            print('-' * 65)
            first_line = False
        else:
            print(f'\t{tries: <11} | {time: <17} | {player: <20} | {word}', end='')
    input("\n\nAperte qualquer tecla para voltar ao menu...")
    headers()

def show_help():
    clear_console()
    file = open("help.txt")
    for line in file:
        print(line, end='')
    input("\n\nAperte qualquer tecla para voltar ao menu...")
    headers()

def headers():
    clear_console()
    print("=== BEM VINDO AO TERM.OOO ===")
    print("\n(1) Iniciar novo jogo")
    print("(2) Visualizar últimas partidas")
    print("(3) Ajuda")
    print("\n(0) Sair")
    opt = input("Opção: ")
    if opt == '1':
        clear_console()
        player = input ("Informe o seu nome: ")
        if player == '':
            player = 'anônimo'
        start_game(player)
    if opt == '2':
        show_ranking()
    if opt == '3':
        show_help()
    if opt == '0':
        print("Saindo do jogo. Até a próxima.")
        exit(0)

def main():
    headers()

main()
