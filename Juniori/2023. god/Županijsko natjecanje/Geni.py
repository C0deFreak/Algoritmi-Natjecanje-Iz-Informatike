gen = [*input()]
k = int(input())
kod_lista = []
rješenje = []

if k == 0:
    for i in gen:
        print(i, end='')
else:
    kod_lista = gen
    for x in gen:
        privremeno = ''
        kod_lista.append(kod_lista[k - 1])
        kod_lista.remove(kod_lista[k - 1])

        for slovo in kod_lista:
            privremeno += slovo
        
        rješenje.append(privremeno)

    print(min(rješenje))

        


