br_prozora = int(input())
br_vrsta = input()
vrsta = [*br_vrsta]

A_prozor = ['....', '....', '....', '....']
B_prozor = ['####', '#..#', '#..#', '####']
C_prozor = ['....', '.##.', '.##.', '....']
D_prozor = ['####', '####', '####', '####']

vrste = [*br_vrsta]
for red in range(4):
    rezultat = ''
    for stupac in vrsta:
        if stupac == 'A':
            rezultat += A_prozor[red]
        elif stupac == 'B':
            rezultat += B_prozor[red]
        elif stupac == 'C':
            rezultat += C_prozor[red]
        else:
            rezultat += D_prozor[red]
    print(rezultat)
