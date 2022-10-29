# TODO посчитать количество каждой буквы в строке в аргументе str_
def get_count_char(str_: str):
    str_ = str_.lower()
    slovar = {}
    for bukvi in str_:
        if not bukvi.isalpha():
            continue
        slovar[bukvi] = slovar.get(bukvi, 0) + 1
    return slovar


def get_count_procent(slovar: dict):
    noviy_slovar = {}
    summa = sum(slovar.values())
    for key in slovar:
        noviy_slovar[key] = (slovar[key] / summa) * 100
    return noviy_slovar


main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""

print(get_count_char(main_str))

