def check_number(z, y):
    for n in range(z, y):
        for x in range(2, n):  # начинаем с 2 до N (c 2 до 9 - делим на 2, потом делим на 3 и пока не поделится на 0)
            if n % x == 0:
                print(n, x)
                break
        else:
            print(n, 'is a problem')


check_number(5, 10)
