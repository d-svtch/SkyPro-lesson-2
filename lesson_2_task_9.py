var_1 = 37
var_2 = 99

print("Было: var1 =", var_1, "var2 =", var_2)

temp = None

temp = var_1
var_1 = var_2
var_2 = temp

print("Стало: var1 =", var_1, "var2 =", var_2)
