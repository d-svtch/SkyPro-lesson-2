def fizz_buzz(range_num):
    output = ""
    for i in range(range_num):
        if i % 3 == 0 and i % 5 == 0:
            output = "FizzBuzz"
        else:
            if i % 3 == 0 and i % 5 != 0:
                output = "Fizz"
            elif  i % 3 != 0 and i % 5 == 0:


                output = "Buzz"
            else:
                output = i

        print(output)

fizz_buzz(int(input("Введите число: ")))
