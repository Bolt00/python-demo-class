# Database

users = {

    'Benita':
    {'username': 'Benita20',
     'password': 'Benita2022@',
     'email': 'Benita2022@gmail.com'},

    'Emeka':
    {'username': 'Emeka40',
     'password': 'Emeka00@',
     'email': 'Emeka2022@gmail.com'},

    'Ugochukwu':
    {'username': 'Ugochukwu500',
     'password': 'Ugochukwu00@',
     'email': 'Ugochukwu2022@gmail.com'}
}


# end of database


name = input('Enter your registered name: ').capitalize()
username1 = input('Enter your username: ').capitalize()
password1 = input('Enter your password: ').capitalize()
email1 = input('Enter your email: ').capitalize()
a = len(password1[2:]) * '*'


def users_data():
    try:

        if username1 in users.get(name).values():
            if password1 in users.get(name).values():
                if email1 in users.get(name).values():
                    print(
                        f'Congratulations, your username ({username1}), password ({password1[0:2]}{a}) and email ({email1}) are valid.\n you will be redirected to your dashboard in few seconds...')
                else:
                    print(
                        'Either one of your credentials is not correct and you cannot login at the moment.')
            else:
                print(
                    'Either one of your credentials is not correct and you cannot login at the moment.')

        elif username1 not in users.get(name).values():
            if password1 not in users.get(name).values():
                if email1 not in users.get(name).values():
                    print(
                        f'None of your details username ({username1}), password ({password1[0:2]}{a}) and email ({email1}) are valid')
                else:
                    print(
                        'Either one of your credentials is not correct and you cannot login at the moment.')
            else:
                print(
                    'Either one of your credentials is not correct and you cannot login at the moment.')
        else:
            print(
                'Either one of your credentials is not correct and you cannot login at the moment.')

    except:
        print(f'Sorry, your name ({name}) wasn\'t found on our database..')


users_data()
