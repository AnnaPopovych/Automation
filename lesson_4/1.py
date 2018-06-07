#a = int(input("введи число: "))
#b = a


#def increase(a):
#    if -10 < a < 10:
#        b = a + 5
#        return b
#    else:
#        b = a - 10
#        return b


#print(increase(b))


def number_between(number):
    if -10 < number < 10:
        return number + 5
    else:
        return number - 10


print(number_between(15))