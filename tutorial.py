import time
import random

username = ['Ghost']
password = ['12345']
first_name = []
last_name = []
email = []

last_index = 0


def view_book():
    global last_index
    nex_index = last_index + 10
    print(libary_db[last_index:nex_index])
    last_index = nex_index


libary_db = [

    {"Title": "Northanger abbey",
     "Author": "Austen, jane",
     "Year": 1814,
     "Edition": "Penguin",
     "Price":  '$18.2'},

    {"Author": "Chinua achebe",
     "Edition": "Penguin",
     "Price": '$30',
     "Title": "Things fall apart",
     "Year": "Released in 1958"},

    {"Title": "War and peace",
     "Author": "Tolstoy, leo",
     "Year": 1865,
     "Edition": "Penguin",
     "Price":  '$12.7'},

    {"Title": "Anna karenina",
     "Author": "Tolstoy, leo",
     "Year": 1875,
     "Edition": "Penguin",
     "Price":  '$13.5'},

    {"Title": "Mrs. dalloway",
     "Author": "Woolf, virginia",
     "Year": 1925,
     "Edition": "Harcourt brace",
     "Price":  '$25'},

    {"Title": "The hours",
     "Author": "Cunnningham, michael",
     "Year": 1999,
     "Edition": "Harcourt brace",
     "Price":  '$12.35'},

    {"Title": "Huckleberry finn",
     "Author": "Twain, mark",
     "Year": 1865,
     "Edition": "Penguin",
     "Price":  '$5.76'},

    {"Title": "Bleak house",
     "Author": "Dickens, charles",
     "Year": 1870,
     "Edition": "Random house",
     "Price":  '$5.75'},

    {"Title": "Tom sawyer",
     "Author": "Twain, mark",
     "Year": 1862,
     "Edition": "Random house",
     "Price":  '$7.75'},

    {"Title": "A room of one's own",
     "Author": "Woolf, virginia",
     "Year": 1922,
     "Edition": "Penguin",
     "Price":  '$29'},

    {"Title": "Harry potter",
     "Author": "Rowling, j.k.",
     "Year": 2000,
     "Edition": "Harcourt brace",
     "Price":  '$19.95'},

    {"Title": "One hundred years of solitude",
     "Author": "Marquez",
     "Year": 1967,
     "Edition": "Harper  perennial",
     "Price":  '$14.00'},

    {"Title": "Hamlet, prince of denmark",
     "Author": "Shakespeare",
     "Year": 1603,
     "Edition": "Signet  classics",
     "Price":  '$7.95'},

    {"Title": "Lord of the rings",
     "Author": "Tolkien, j.r.",
     "Year": 1937,
     "Edition": "Penguin",
     "Price":  '$27.45'}
]


def services():
    service = """
    These are the services we provide to our users.
    1)Search for Books 📕
    2)Buy Books 📕
    3)View Books 📕"""
    print(service)


def registeration():
    welcome = """Welcome To Ghost 👻 Libary
 How can we assist you?
 1) Sign up
 2) Login"""
    print(welcome)


registeration()


welcome1 = int(input('Login or Sign up: '))
if welcome1 == 1:

    fname = input('Enter your first name: ').capitalize()
    lname = input('Enter your last name: ').capitalize()
    mail = input('Enter your email: ').capitalize()
    while True:
        uname = input('Enter your username: ').capitalize()
        if len(uname) >= 5:
            pword = input('Enter your password: ')
            if len(pword) >= 5:
                first_name.append(fname)
                last_name.append(lname)
                email.append(mail)
                username.append(uname)
                password.append(pword)
                print(
                    'You have successfully registered, below are your credentials....')
                time.sleep(5)
                print(
                    f'First name: {fname} \n Last name: {lname} \n Email: {mail} \n Username: {uname} \n Password: {pword}')
                break
            else:
                print('Your password must be greater than or equal to 5 characters')

        else:
            print('Your username must be greater than or equal to 5 characters.')


elif welcome1 == 2:

    print(f'Hello, Welcome to Ghost library login page. \n Enter "Cancel to abort the operation"')
    time.sleep(3)
    while True:
        login_username = input('Enter your username: ').capitalize()
        if login_username in username:
            login_password = input('Enter your password: ')
            if login_password in password:
                print('Checking your credentials, kindly hold on...')
                time.sleep(5)
                print('Login successful....')
                time.sleep(5)
                print(
                    f'Hello {login_username}, Welcome back 😎. You have successfully logged in.')
                services()
                time.sleep(5)
                try:
                    enter = int(input('Select a category: '))
                except:
                    print('You can only select category with numbers.')
                try:
                    if enter == 1:
                        print('Enter the title of the book to search')
                        search_book = input('').capitalize()
                        for x in libary_db:
                            if x['Title'] == search_book:
                                print(
                                    f'Your Search: {search_book} is pocessing...')
                                time.sleep(5)
                                print('Search Completed ✅')
                                time.sleep(5)
                                print('Title:', x['Title'])
                                time.sleep(5)
                                print('Author:', x['Author'])
                                time.sleep(5)
                                print('Year:', x['Year'])
                                time.sleep(5)
                                print('Edition:', x['Edition'])
                                time.sleep(5)
                                print('Price:', x['Price'])
                                break

                            else:
                                print(
                                    f'Your Search: {search_book} is pocessing...')
                                time.sleep(5)
                                print('Search completed ✅')
                                time.sleep(2)
                                print(
                                    f'We don\'t have this book: {search_book}.')
                            break
                        break
                    elif enter == 2:
                        print(
                            "Enter the title of the book to buy \n If it's available, we'll provide you with the book details and price.")
                        buy_book_name = input('').capitalize()
                        time.sleep(2)
                        for y in libary_db:
                            if y['Title'] == buy_book_name:
                                print(
                                    f'Searching if {buy_book_name} is available...')
                                time.sleep(5)
                                a = y['Price']
                                print(
                                    f'Search completed ✅, {buy_book_name} is available with price tag of {a}, do you want to buy?')
                                time.sleep(5)
                                print(
                                    'Enter yes to purchase and enter no to cancel')
                                buy = input('').capitalize()
                                if buy == 'Yes':
                                    print(
                                        f'You have successfully purchased {buy_book_name} for', y['Price'])
                                    break
                                elif buy == 'No':
                                    print(
                                        f'Transaction for {buy_book_name} cancelled successfully.')
                                    break
                            else:
                                print(
                                    f'Searching if {buy_book_name} is available...')
                                time.sleep(5)
                                print('Search completed ✅')
                                time.sleep(2)
                                print(
                                    f'We don\'t have this book: {buy_book_name}.')
                                break
                        break
                    elif enter == 3:
                        view_book()
                        break

                    else:
                        print(f'Invalid selection ({enter})')
                        break
                except ValueError:
                    print('You can only select a category with number')
                continue

            elif login_password == 'Cancel' or login_password == 'cancel' or login_password == 'CANCEL':
                print('You have successfully aborted the operation')
                break
            else:
                print(f'Password ({login_password}) doesn\'t exist.')
            continue
        elif login_username == 'Cancel':
            print('You have successfully aborted the operation')
            break
        else:
            print(f'Username ({login_username}) doesn\'t exist.')
        continue
