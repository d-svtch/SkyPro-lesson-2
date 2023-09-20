def is_year_leap (year):
    if year % 4 == 0:
        return True
    else:
        return False

inputed_year = input("Введите год: ")

leap = is_year_leap(int(inputed_year))

print("Год " +  inputed_year + ": " + str(leap))