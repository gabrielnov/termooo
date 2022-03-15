from random import randint
import os
import time

content = []
def draw_word():
    f = open('words.txt')
    for line in f:
        if len(list(line)) == 6:
            content.append(line.replace("\n", ""))
    f.close()
    word = content[randint(0, len(content))]
    print("palavra sorteada: ", word)
    return word

def find_word(word):
    for w in content:
        if word == w:
            return True
    return False

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

def clear_console():
    command = 'clear'
    if os.name in ('nt', 'dos'):
        command = 'cls'
    os.system(command)

lines = []
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

def save_ranking(total_time, player, tries):
    try:
        f = open('ranking.csv', 'x')
        f.write('tries;minutes;player\n')
    except FileExistsError:
        f = open('ranking.csv', 'a')
    minutes =total_time/60
    f.write(f'{tries};{minutes:.2f};{player}\n')

def finish_game(total_time, player, tries):
    save_ranking(total_time, player, tries)
    headers()

def run_game(start, player, word):
    for t in range(1, 5):
        print(f"Tentativa {t}/5")
        guess = ''
        while not valid_guess(guess):
            guess = input("Sua tentativa: ")
        marks = verify_guess(guess, word)
        output(list(guess), marks)

        if guess == word:
            total_time = time.time() - start
            finish_game(total_time, player, t)
            return

def start_game(player):
    clear_console()
    word = draw_word()
    start = time.time()
    run_game(start, player, word)

def sort_ranking(ranking):
    pass

def show_ranking():
    ranking = open('ranking.csv')
    sort_ranking(ranking)
    for line in ranking:
        tries, time, player = line.split(';')
        print(f'\t{tries: <5} | {time: <9} | {player}', end='')

def headers():
    print("=== BEM VINDO AO TERM.OOO ===")
    print("\n(1) Iniciar novo jogo")
    print("(2) Visualizar ranking")
    print("(3) Ajuda")
    print("\n(0) Sair")
    opt = input("Opção: ")
    if opt == '1':
        clear_console()
        player = input ("Informe o seu nome: ")
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
