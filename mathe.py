import random

QUESTIONS_DEFAULT = 20


def _ask_int(prompt: str) -> int:
    """Prompt until the user enters a valid integer."""
    while True:
        s = input(prompt)
        try:
            return int(s)
        except ValueError:
            print("Bitte eine ganze Zahl eingeben.")


def auswertung(wrong: int) -> None:
    """Print a short evaluation message for number of wrong answers."""
    if wrong == 0:
        print("Keine falschen Ergebnisse. Gut gemacht!")
    elif wrong == 1:
        print("1 falsches Ergebnis")
    else:
        print(f"{wrong} falsche Ergebnisse")


def einmaleins(questions: int = QUESTIONS_DEFAULT) -> int:
    """Multiplikationsaufgaben (2 - 12). Returns number of wrong answers."""
    wrong = 0
    for _ in range(questions):
        a = random.randint(2, 12)
        b = random.randint(2, 12)
        print(a, "mal", b)
        ergebnis = _ask_int("Ergebnis? ")
        if ergebnis == a * b:
            print("korrekt")
        else:
            print("falsch - richtig:", a * b)
            wrong += 1
    return wrong


def runden(n: int, questions: int = QUESTIONS_DEFAULT) -> int:
    """Round random integers [0,1000] to nearest multiple of n.
    Uses integer arithmetic and rounds halves up (ties to higher multiple).
    """
    if n <= 0:
        raise ValueError("n muss größer als 0 sein")
    wrong = 0
    for _ in range(questions):
        a = random.randint(0, 1000)
        print(a, "auf", n)
        # round to nearest multiple of n, tie-breaking upwards
        correct = ((a + n // 2) // n) * n
        ergebnis = _ask_int("gerundet? ")
        if ergebnis == correct:
            print("korrekt")
        else:
            print("falsch - richtig:", correct)
            wrong += 1
    return wrong


def quersumme(questions: int = QUESTIONS_DEFAULT) -> int:
    """Ask for digit sum of random integers [0,1000]."""
    wrong = 0
    for _ in range(questions):
        zahl = random.randint(0, 1000)
        print(zahl)
        qs = sum(int(z) for z in str(zahl))
        ergebnis = _ask_int("Quersumme? ")
        if ergebnis == qs:
            print("korrekt")
        else:
            print("falsch - richtig:", qs)
            wrong += 1
    return wrong


def division(questions: int = QUESTIONS_DEFAULT) -> int:
    """Division tasks: present a*b divided by b and ask for a."""
    wrong = 0
    for _ in range(questions):
        a = random.randint(2, 12)
        b = random.randint(2, 12)
        dividend = a * b
        print(dividend, "geteilt durch", b)
        ergebnis = _ask_int("Ergebnis? ")
        if ergebnis == a:
            print("korrekt")
        else:
            print("falsch - richtig:", a)
            wrong += 1
    return wrong


def plusminus(questions: int = QUESTIONS_DEFAULT) -> int:
    """Random addition (if sum < 1000) otherwise subtraction.
    Ensures wrong is incremented for any incorrect answer.
    """
    wrong = 0
    for _ in range(questions):
        a = random.randint(1, 1000)
        b = random.randint(1, 1000)
        if (a + b) < 1000:
            print(a, "+", b)
            ergebnis = _ask_int("Ergebnis? ")
            if ergebnis == a + b:
                print("korrekt")
            else:
                print("falsch - richtig:", a + b)
                wrong += 1
        else:
            # subtraction: present the larger minus the smaller
            if a >= b:
                print(a, "-", b)
                ergebnis = _ask_int("Ergebnis? ")
                if ergebnis == a - b:
                    print("korrekt")
                else:
                    print("falsch - richtig:", a - b)
                    wrong += 1
            else:
                print(b, "-", a)
                ergebnis = _ask_int("Ergebnis? ")
                if ergebnis == b - a:
                    print("korrekt")
                else:
                    print("falsch - richtig:", b - a)
                    wrong += 1
    return wrong


def mittelwert(questions: int = QUESTIONS_DEFAULT) -> int:
    """Average tasks: present a and b and ask for average, both even or both odd."""
    wrong = 0
    for _ in range(questions):
        a = random.randint(0, 1000)
        b = 2 * random.randint(0, 500) + a%2
        print("Mittelwert aus", a, "und", b)
        mitte = int((a + b) / 2)
        ergebnis = _ask_int("Ergebnis? ")
        if ergebnis == mitte:
            print("korrekt")
        else:
            print("falsch - richtig:", mitte)
            wrong += 1
    return wrong

def main() -> None:
    print("Kopfrechentrainer 0.1")
    selection = input(
        "Auswahl:\nEinmaleins: e, Runden auf 10: r10, Runden auf 100: r100,"
        "Quersumme: q, Division: d, Plus/Minus: p, Mittelwert: m\n"
    ).strip().lower()

    if selection not in ("e", "r10", "r100", "q", "d", "p", "m"):
        print("Auswahl nicht erkannt!")
        return

    if selection == "e":
        print("Einmaleins ausgewählt")
        auswertung(einmaleins())
    elif selection == "r100":
        print("Runden auf 100 ausgewählt")
        auswertung(runden(100))
    elif selection == "r10":
        print("Runden auf 10 ausgewählt")
        auswertung(runden(10))
    elif selection == "q":
        print("Quersumme ausgewählt")
        auswertung(quersumme())
    elif selection == "d":
        print("Division ausgewählt")
        auswertung(division())
    elif selection == "p":
        print("Plus/Minus ausgewählt")
        auswertung(plusminus())
    elif selection == "m":
        print("Mittelwert ausgewählt")
        auswertung(mittelwert())


if __name__ == "__main__":
    main()
