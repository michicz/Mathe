import random

def auswertung(w):
    if w != 1:
        print(w, 'falsche Ergebnisse')
    else:
        print('1 falsches Ergebnis')
    pass


def einmaleins(): # Multiplikation 2 - 12
    wrong = 0
    for i in range(20):
        a = random.randint(2, 12)
        b = random.randint(2, 12)
        print(a, 'mal', b)
        ergebnis = input("Ergebnis? ")
        if int(ergebnis) == a * b:
            print('korrekt')
        else:
            print('falsch - richtig: ', a * b)
            wrong += 1
    return wrong


def runden(n):
    wrong = 0
    for i in range(20):
        a = random.randint(0, 1000)
        print(a, 'auf', n)
        ergebnis = input('gerundet? ')
        if int(ergebnis) == n * int((a+5)/n):
            print('korrekt')
        else:
            print('falsch - richtig: ', n * int((a+5)/n))
            wrong += 1
    return wrong


def quersumme(): # Zahlen von 0-1000
    wrong = 0
    for i in range(20):
        zahl = random.randint(0, 1000)
        print(zahl)
        qs = 0
        for ziffer in str(zahl):
            qs += int(ziffer)
        if qs == int(input('Quersumme? ')):
            print('korrekt')
        else:
            print('falsch - richtig: ', qs)
            wrong += 1
    return wrong


def division():
    wrong = 0
    for i in range(20):
        a = random.randint(2, 12)
        b = random.randint(2, 12)
        print(a*b, 'geteilt durch', b)
        ergebnis = input("Ergebnis? ")
        if int(ergebnis) == a:
            print('korrekt')
        else:
            print('falsch - richtig: ', a)
            wrong += 1
    return wrong


def plusminus():
    wrong = 0
    for i in range(20):
        a = random.randint(1, 1000)
        b = random.randint(1, 1000)
        if (a + b) < 1000:
            print(a, '+', b)
            ergebnis = input("Ergebnis? ")
            if int(ergebnis) == a + b:
                print('korrekt')
            else:
                print('falsch - richtig: ', a+b)
                wrong += 1
        elif a >= b:
            print(a, '-', b)
            ergebnis = input("Ergebnis? ")
            if int(ergebnis) == a - b:
                print('korrekt')
            else:
                print('falsch - richtig: ', a - b)
        else:
            print(b, '-', a)
            ergebnis = input("Ergebnis? ")
            if int(ergebnis) == b - a:
                print('korrekt')
            else:
                print('falsch - richtig: ', b - a)
                wrong += 1
    return wrong


def main():
    print('Kopfrechentrainer 0.1')
    selection = input('Auswahl:\nEinmaleins: e, Runden auf 10: r10, Runden auf 100: r100, Quersumme: q, Division: d, Plus/Minus p ')
    if selection in ('e', 'r10', 'r100', 'q', 'd', 'p'): ## todo: geteilt, Addition/Subtraktion
        if selection == 'e':
            print('Einmaleins ausgewählt')
            auswertung(einmaleins())
        if selection == 'r100':
            print('Runden auf 100 ausgewählt')
            auswertung(runden(100))
        if selection == 'r10':
            print('Runden auf 10 ausgewählt')
            auswertung(runden(10))
        if selection == 'q':
            print('Quersumme ausgewählt')
            auswertung(quersumme())
        if selection == 'd':
            print('Division ausgewählt')
            auswertung(division())
        if selection == 'p':
            print('Plus/Minus ausgewählt')
            auswertung(plusminus())
    else: print('Auswahl nicht erkannt!')


main()