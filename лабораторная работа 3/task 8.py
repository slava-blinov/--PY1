money_capital = 10000
salary = 5000
spend = 6000
increase = 0.05

month = 0  # количество месяцев, которое можно прожить

# TODO Оформить решение

while money_capital + salary > spend:
    spend = spend*(1 + increase)
    money_capital = money_capital + salary - spend
    month += 1

print(month)
