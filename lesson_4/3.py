def numbers(number1, number2, number3):
    if (
            number1 == number2 or
            number1 == number3 or
            number3 == number2
    ):
        return "Yes"


print(numbers(1, 3, 2))