def month_to_season(mount_number):
    if 3 <= mount_number <= 5:
        print("Весна")
    elif 6 <= mount_number <= 8:
        print("Лето")
    elif 9<= mount_number <= 11:
        print("Осень")
    else: print("Зима")

month_to_season(int(input("Введите номер месяца: ")))

