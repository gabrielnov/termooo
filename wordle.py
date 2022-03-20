from random import randint
import os
import time

def clear_console():
    command = 'clear'
    if os.name in ('nt', 'dos'):
        command = 'cls'
    os.system(command)

def save_ranking(total_time, player, tries, word):
    f = open('scores.txt', 'a', encoding='utf-8')
    total_time = time.strftime('%H:%M:%S', time.gmtime(total_time))
    player = player[0:20]
    f.write(f'{tries};{total_time};{player};{word}\n')
    f.close()

def finish_game(total_time, player, tries, word):
    save_ranking(total_time, player, tries, word)
    clear_console()
    print(f'\n\t\t === Parabéns! === \n\n {player}, você acertou o termo {word} com {tries} tentativas\n\n')
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
            print(f" | {lines[i][j]}", end = '')
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

def valid_guess(guess, words):
    if guess == '':
        return False
    l_guess = list(guess)
    if len(l_guess) != 5:
        print("Digite uma palavra com apenas 5 letras")
        return False
    for w in words:
        if guess == w.upper():            
            return True
    print(f"\nPalavra {guess} inválida. Tente novamente.")    
    return False

def run_game(start, player, word, words):
    print(f'palavra sorteada: {word}')
    for t in range(1, 7):
        print(f"\n\t === Tentativa {t}/6 ===")
        guess = ''
        while not valid_guess(guess, words):
            guess = input("\nSua tentativa: ")
            guess = guess.upper()
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

def generate_words():
    f = open('words.txt', 'r', encoding='utf-8')
    words = f.read().splitlines()
    return words

def draw_word(words):    
    word = words[randint(0, len(words))]
    return word

def start_game(player):
    global lines
    lines = []
    clear_console()
    words = generate_words()
    word = draw_word(words)
    start = time.time()
    run_game(start, player, word.upper(), words)

def show_ranking():
    scores = open('scores.txt', 'r', encoding='utf-8')    
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
    scores.close()
    input("\n\nAperte qualquer tecla para voltar ao menu...")
    headers()

def show_help():
    clear_console()
    file = open("help.txt", 'r', encoding='utf-8')    
    for line in file:
        print(line, end='')
    input("\n\nAperte qualquer tecla para voltar ao menu...")
    file.close()
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
            player = 'Anônimo'
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
