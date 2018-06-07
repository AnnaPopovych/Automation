def listsum(a):
    b = 0
    for i in a[::2]:
        b = b + i * a[-1]
    return b


print(listsum([1, 3, 5, 7, 9]))
