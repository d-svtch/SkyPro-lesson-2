import math

def square (side):
    return  math.ceil(side*side)

square_side = float(input("Введите значение стороны квадрата: "))

print("Площадь квадрата равна:", square(square_side))