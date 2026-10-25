def checkList(list: list, element: int) -> bool:
    return element in list


print(checkList([1, 2, 3, 4, 5], 3))  # True
print(checkList([1, 2, 3, 4, 5], 6))  # False
