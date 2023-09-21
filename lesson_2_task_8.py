lst =[]
length = 5
value = 18

for i in range(length):
    lst.append(i)
    lst[i] = value
    value -= 4

print(lst)