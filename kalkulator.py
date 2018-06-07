a = int(input("Number_1: "))
b = int(input("Number_2: "))
operation = input("Choose your character: +, -, **: ")

if operation == '+':
    print(a + b)
elif operation == '-':
    print(a - b)
elif operation == '**':
    print(a ** b)
else:
    print('You have done the wrong choice!')
