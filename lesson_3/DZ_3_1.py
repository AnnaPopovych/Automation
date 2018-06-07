c = [-1, 2, -1, -1]

def my_new_function(a):
    b = []
    for i in a:
        b.append(abs(i))
    b.sort()
    return b

print(my_new_function())
