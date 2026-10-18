liczby = list(range(10))

def wyswietl_parzyste(liczby):
    for liczna in liczby:
        if liczna % 2 == 0:
            print(liczna)

wyswietl_parzyste(liczby)