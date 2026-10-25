def pomnoz_for(liczby):
    wyniki = []
    for liczba in liczby:
        wyniki.append(liczba * 2)
    return wyniki


def pomnoz_skladana(liczby):
    return [liczba * 2 for liczba in liczby]


moje_liczby = [1, 2, 3, 4, 5]
print(pomnoz_for(moje_liczby))
print(pomnoz_skladana(moje_liczby))
