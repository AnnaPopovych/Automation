from random import randint


def cube(x, y):
    x = randint(1, 6)
    y = randint(1, 6)




    for i in range(x, y):
        for n in range(1, 7):
            if sum(x, y) == 8:
                print(x, y)
                break


