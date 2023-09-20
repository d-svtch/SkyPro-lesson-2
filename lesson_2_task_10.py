def bank(cash,time):
    deposit = cash
    for i in range(time):
        deposit += ( deposit * 0.1 )
    print("Итоговая выплата:", deposit )

amount = float(input("Введите сумму вклада: "))
years = int(input("Введите срок вклада в годах: "))

bank(amount, years)