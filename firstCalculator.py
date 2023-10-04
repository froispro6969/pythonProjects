a = int((input("Podaj liczbe 1: ")))
b = int((input("Podaj liczbe 2: ")))

print("1. Dodaj")
print("2. Odejmnij")
print("3. Pomnoz")
print("4. Podziel")

c = int((input("Wybierz operacje: (wpisz numer) ")))


def dodaj(a, b):
    return a + b


def odejmij(a, b):
    return a - b


def pomnóż(a, b):
    return a * b


def podziel(a, b):
    if b == 0:
        return "Nie można dzielić przez zero"
    else:
        return a / b


if c == 1:
    wynik = dodaj(a, b)
    print("Dodano liczby, wynik to: ", wynik)
elif c == 2:
    wynik = odejmij(a, b)
    print("Odjeto liczby, wynik to: ", wynik)
elif c == 3:
    wynik = pomnóż(a, b)
    print("Pomnozono liczby, wynik to: ", pomnóż(a, b))
elif c == 4:
    print("Podzielno liczby, wynik to: ", podziel(a, b))
else:
    print("Wybrano zly numer!!!!")
