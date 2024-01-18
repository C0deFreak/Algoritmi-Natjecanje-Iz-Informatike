br_sjedala = input()
br_sjedala = br_sjedala.split()
red = int(br_sjedala[0])
stupac = int(br_sjedala[1])

raspored = []

slobodna_mjesta = 0

for x_input in range(red):
    prikaz_reda = input()
    raspored.append([*prikaz_reda])

for x in range(red):
    if 0 < x < (red - 1):
        for y in range(stupac):
            if 0 < y < (stupac - 2):
                if ((raspored[x - 1][y] != '#') and 
                    (raspored[x + 1][y] != '#') and 
                    (raspored[x][y - 1] != '#') and 
                    (raspored[x - 1][y - 1] != '#') and 
                    (raspored[x + 1][y - 1] != '#') and 
                    (raspored[x - 1][y + 1] != '#') and 
                    (raspored[x + 1][y + 1] != '#') and 
                    (raspored[x - 1][y + 2] != '#') and 
                    (raspored[x + 1][y + 2] != '#') and 
                    (raspored[x][y - 1] != '#') and 
                    (raspored[x][y + 2] != '#') and 
                    (raspored[x][y + 1] == '#') and 
                    (raspored[x][y] == '#')):
                    
                    slobodna_mjesta += 1

print(slobodna_mjesta)