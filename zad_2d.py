liczby = list(range(10, 20))


def co_drugi(liczby):
    for i in range(0, len(liczby), 2):
        print(liczby[i])


co_drugi(liczby)
