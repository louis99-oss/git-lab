def czyParzysta(liczba: int) -> bool:
    return liczba % 2 == 0


wynik = czyParzysta(5)
if wynik:
    print("Liczba parzysta")
else:
    print("Liczba nieparzysta")
