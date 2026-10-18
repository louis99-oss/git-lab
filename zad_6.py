def polacz_i_potegi(lista1: list, lista2: list) -> list:
    polaczona = lista1 + lista2           # 1. złączenie list
    bez_duplikatow = list(set(polaczona))  # 2. set nie trzyma duplikatów
    return [x ** 3 for x in bez_duplikatow]  # 3. potęga 3 (lista składana)


wynik = polacz_i_potegi([1, 2, 3], [3, 4, 2])
print(wynik)   # [1, 8, 27, 64]
# - lista1 + lista2 skleja listy.
# - set to zbiór, który z definicji nie ma powtórzeń. Zamiana list → set → list usuwa duplikaty. Zbiór nie gwarantuje kolejności, więc jeśli chcesz mieć posortowany wynik, użyj sorted(set(polaczona)).
# - ** to potęgowanie: 2 ** 3 == 8.