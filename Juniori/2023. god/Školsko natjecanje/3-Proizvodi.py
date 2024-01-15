br_proizvoda = int(input())
predmet = []
drzava = []
cijene = []
ukupna_cijena = 0
kolicina = 0

for proizvod in range(br_proizvoda):
    info = input()
    isprekidano = info.split('-')
    broj = isprekidano[2].split(",")
    broj = float(broj[0]) + (float(broj[1]) / 100)
    if (isprekidano[0] not in predmet) and (isprekidano[1] not in drzava):
        predmet.append(isprekidano[0])
        drzava.append(isprekidano[1])
        cijene.append(broj)
        kolicina += 1
        ukupna_cijena += broj
    elif isprekidano[0] in predmet:
        izbaci_predmet = predmet.index(isprekidano[0])
        if (broj < cijene[izbaci_predmet]):
            predmet.remove(izbaci_predmet)
            drzava.remove(izbaci_predmet)
            ukupna_cijena -= cijene[izbaci_predmet]
            cijene.remove(izbaci_predmet)
            predmet.append(isprekidano[0])
            drzava.append(isprekidano[1])
            cijene.append(broj)
            ukupna_cijena += broj
    elif isprekidano[0] in drzava:
        izbaci_drzavu = drzava.index(isprekidano[1])
        if (broj < cijene[izbaci_predmet]):
            predmet.remove(izbaci_drzavu)
            drzava.remove(izbaci_drzavu)
            ukupna_cijena -= cijene[izbaci_drzavu]
            cijene.remove(izbaci_drzavu)
            predmet.append(isprekidano[0])
            drzava.append(isprekidano[1])
            cijene.append(broj)
            ukupna_cijena += broj


print(f"{kolicina} {round(ukupna_cijena, 2)}")