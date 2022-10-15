list_numbers = [2, -93, -2, 8, -36, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO Оформить решение
alfa = 0
omega = list_numbers[0]
for index, value in enumerate(list_numbers):
    if value > omega:
        omega = value
        alfa = index


list_numbers[-1], list_numbers[alfa] = list_numbers[alfa], list_numbers[-1]

print(list_numbers)
