bräde = [' ' for x in range(10)]

# Den sätter in bokstaven i den rutan man valt
def sättInBokstav(bokstav, pos):
    bräde[pos] = bokstav

# En ruta är ledig
def rutaÄrLedig(pos):
    return bräde[pos] == ' '

#Den skriver ut brädspelet
def skrivUtBräde(bräde):
    print('   |   |   ')
    print(' ' + bräde[1] + ' | ' + bräde[2] + ' | ' + bräde[3])
    print('   |   |   ')
    print('------------')
    print('   |   |   ')
    print(' ' + bräde[4] + ' | ' + bräde[5] + ' | ' + bräde[6])
    print('   |   |   ')
    print('------------')
    print('   |   |   ')
    print(' ' + bräde[7] + ' | ' + bräde[8] + ' | ' + bräde[9])
    print('   |   |   ')

# När brädspelet är fullt 
def ärBrädetFullt(bräde):
    if bräde.count(' ') > 1:
        return False
    else:
        return True

# Funktionen är när du vinner
def ärVinnare(b, l):
    return ((b[1] == l and b[2] == l and b[3] == l) or
    (b[4] == l and b[5] == l and b[6] == l) or
    (b[7] == l and b[8] == l and b[9] == l) or
    (b[1] == l and b[4] == l and b[7] == l) or
    (b[2] == l and b[5] == l and b[8] == l) or
    (b[3] == l and b[6] == l and b[9] == l) or
    (b[1] == l and b[5] == l and b[9] == l) or
    (b[3] == l and b[5] == l and b[7] == l))

# Spelaren ska välja ett drag alltså välja en siffra mellan 1 och 9
def spelarDrag():
    kör = True
    while kör:
        drag = input("Vänligen välj en position för att lägga till X mellan 1 och 9\n")
        try:
            drag = int(drag)
            if drag > 0 and drag < 10:
                if rutaÄrLedig(drag):
                    kör = False
                    sättInBokstav('X', drag)
                else:
                    print('Förlåt, denna ruta är upptagen')
            else:
                print('Snälla skriv ett nummer mellan 1 och 9')

        except:
            print('Snälla lägg in ett nummer')

# Funktion för datorns drag
def datornsDrag():
    möjligaDrag = [x for x, bokstav in enumerate(bräde) if bokstav == ' ' and x != 0]
    drag = 0

    for bokstav in ['O', 'X']:
        for i in möjligaDrag:
            brädeKopia = bräde[:]
            brädeKopia[i] = bokstav
            if ärVinnare(brädeKopia, bokstav):
                drag = i
                return drag


    öppnaHörn = []
    for i in möjligaDrag:
        if i in [1, 3, 7, 9]:
            öppnaHörn.append(i)

    if len(öppnaHörn) > 0:
        drag = slumpa(öppnaHörn)
        return drag

    if 5 in möjligaDrag:
        drag = 5
        return drag

    öppnaSidor = []
    for i in möjligaDrag:
        if i in [2, 4, 6, 8]:
            öppnaSidor.append(i)

    if len(öppnaSidor) > 0:
        drag = slumpa(öppnaSidor)
        return drag

def slumpa(lista):
    import random
    ln = len(lista)
    r = random.randrange(0, ln)
    return lista[r]

def huvudprogram():
    print("Välkommen till spelet!")
    skrivUtBräde(bräde)

    while not(ärBrädetFullt(bräde)):
        if not(ärVinnare(bräde, 'O')):
            spelarDrag()
            skrivUtBräde(bräde)
        else:
            print("Neej, du förlorade!")
            break

        if not(ärVinnare(bräde, 'X')):
            drag = datornsDrag()
            if drag == 0:
                print("Datorn gör inget drag.")
            else:
                sättInBokstav('O', drag)
                print('Datorn placerade en O på position', drag, ':')
                skrivUtBräde(bräde)
        else:
            print("Ajajaj, du vann!")
            break

    if ärBrädetFullt(bräde):
        print("Oj, där blev det oavgjort")

# Huvudloopen för att spela spelet
while True:
    val = input("Vill du spela? Tryck på y för ja eller n för nej (y/n)\n")
    if val.lower() == 'y':
        bräde = [' ' for x in range(10)]
        print('--------------------')
        huvudprogram()
    elif val.lower() == 'n':
        print("Tack för att du spelade. Hej då!")
        break
    else:
        print("Ogiltigt val. Försök igen.")
