num = int(input('Number: '))

if num > 10:
    print('num more than 10 \nthis number is {}'.format(num))
elif 0 < num < 5:
    if num + 11 > 13:
        print('стало больше 13 \n номер {}'.format(num + 11))
    else:
        print('число меньше 5 \n Число {}'.format(num + 11))
else:
    if (num - 100) > -200 and num - 100 < -50:
        print('number between -200 nd -50 \n number {}'.format(
            num - 100
        ))
    else:
        print('что-то пошло на право')