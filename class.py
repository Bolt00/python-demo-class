database = {
    'Ghost': 12345,
    'Bolt': 404040
}


book1 = ['To Kill a Mockingbird', 'Pride and Prejudice', 'Jane Eyre', 'The Great Gatsby',
         '1984 (Paperback)', 'Wuthering Heights', 'The Grapes of Wrath', 'The Rock', 'Aging', 'Ghost']

book2 = ['The Train', 'The Batch', 'The Foody',
         'Hell Gate', 'Journey of No Mercy']

try:

    username = input('Enter your username: ').capitalize()
    if username in database:
        password = int(input('Enter your password: '))
        for x, y in database.items():
            if password == y:
                print('Below are the books we have')
                for x in book1:
                    print(x)
                    break

                more_books = input(
                    'Enter Yes to see more books /n Enter No to abort: ').capitalize()
                if more_books == 'Yes':
                    for i in book2:
                        print(i)
                        break
                elif more_books == 'No':
                    print('You have successfully aborted.')
                else:
                    print('Invalid selection.')
            else:
                print(f'Password ({password}) doesn\'t exist in our database')
    else:
        print(f'Your username ({username}) doesn\'t exist in our database')
except:
    print('You encountered an error.')
