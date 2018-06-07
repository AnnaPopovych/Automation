correct_login = 'aaa '
correct_password = 1111


while True:
    login = input('Login: ')
    if login in ('correct_login', 'correct_password'):

        break
    else:
        print()