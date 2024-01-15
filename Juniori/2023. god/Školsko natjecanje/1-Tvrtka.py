# Broj radnika
radnici = int(input())

# Variable
razlika_vremena = []
najkrace_vrijeme = 100
najranije_vrijeme = 100
konacno = 0

# Ponavljaš kako bi dobioodgovarajuće vrijeme svakog radnika
for radnik in range(radnici):
    vrijeme = input()

    # Vrijeme se rastavlja na dva dijela
    razlika_vremena = vrijeme.split()
    privremena_razlika = int(razlika_vremena[1]) - int(razlika_vremena[0])

    # Ako je ovo vrijeme najkraće to će vrijeme bit odabrano
    if (privremena_razlika < najkrace_vrijeme):
        najkrace_vrijeme = privremena_razlika
        konacno = vrijeme
        najranije_vrijeme = int(razlika_vremena[0])
    # Ako su najkraća vremena ista odaberi ono najranije
    elif (privremena_razlika == najkrace_vrijeme):
        if (int(razlika_vremena[0]) < najranije_vrijeme):
            najkrace_vrijeme = privremena_razlika
            konacno = vrijeme
            najranije_vrijeme = int(razlika_vremena[0])

print(konacno)