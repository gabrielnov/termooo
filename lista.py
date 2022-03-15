f = open('lista_inteira.txt')
l = open('lista_final.txt', 'a')

for w in f:
    if '-' not in w:
        if '.' not in w:
            if len(w) == 6:
                l.write(w)

