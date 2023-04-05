# BUILD A SYSTEM TO TAKE CUSTOMER'S ORDERS IN A MALL
# AND RETURN THE RECIEPT AFTER A SUCCESSFUL TRANSACTION
#  (VAT MUST BE INCLUDED IN CUSTOMER'S FEE)
import random


class Random_numbers:
    def __init__(self):
        self.random1 = random.randint(50000, 500000)
        self.random2 = random.randint(500000, 1000000)


class OrderDepartment:
    def __init__(self):
        self.order_department2 = 'Enter 1 for Electronics \n Enter 2 for Grocery \n Enter 3 for Restaurants \n Enter 4 for Clothes \n Enter 5 for Accessory \n Enter 6 for Pharmacy'
        self.order_department = 'Kindly choose the department you want to place an order on:'


class Electronics:
    def __init__(self):
        self.electronics = ['Phone', 'Laptop', 'Computer', 'Printer']


class Pharmacy:
    def __init__(self):
        self.pharmacy = ['Paracetamol', 'Panadol Extra', 'Inhaler', 'Flagyl']


class Accessory:
    def __init__(self):
        self.accessory = ['Watch', 'Sun Shade', 'Necklace', 'Wallet']


class Clothes:
    def __init__(self):
        self.clothes = ['Jeans', 'Polo', 'T-Shirt', 'Hoodie']


class Grocery:
    def __init__(self):
        self.grocery = ['Bread', 'Meat', 'Pasta', 'Cheese']


class Restaurant:
    def __init__(self):
        self.restaurants = ['Swallow', 'Beans', 'Plantain', 'Fish']


class Customer(Random_numbers, OrderDepartment, Electronics, Pharmacy, Accessory, Clothes, Grocery, Restaurant):
    def __init__(self):
        Random_numbers.__init__(self)
        OrderDepartment.__init__(self)
        Electronics.__init__(self)
        Pharmacy.__init__(self)
        Accessory.__init__(self)
        Clothes.__init__(self)
        Grocery.__init__(self)
        Restaurant.__init__(self)

    def Order(self):
        print('WELCOME TO GHOST MALL')
        name = input('What is your name? ').capitalize()
        print(f'Hello {name}, {self.order_department} {self.order_department2}')
        usd = 'USD'
        try:
            order1 = int(input(
                'Select a department for your order from the above lists'))

            if order1 == 1:
                print(self.electronics)
                enter = input(
                    'The above Electronics are available, place your order by entering the correct name of the product. ').capitalize()

                if enter == 'Phone' or enter == 'Phones':
                    print(
                        'These are the available phones we have:\n 1. Samsung S22 Ultra ($2500) \n 2. Iphone 12 pro max ($2034) \n 3. Tecno camon c8 ($340)')
                    try:
                        enter2 = int(input(
                            'Enter 1 to order for Samsung S22 Ultra \n Enter 2 for Iphone 12 pro max \n Enter 3 for Tecno Camon c8 '))

                        if enter2 == 1:
                            print(
                                f'You have successfully placed an order for Samsung S22 Ultra which costs $2500 plus 5% VAT Charges and your total fee is', 2500*5/100+2500, 'USD')
                        elif enter2 == 2:
                            print(
                                f'You have successfully placed an order for Iphone 12 pro max which costs $2034 plus 5% VAT Charges and your total fee is', 2034*5/100+2034, 'USD')
                        elif enter2 == 3:
                            print(
                                f'You have successfully placed an order for Tecno Camon C8 which costs $340 plus 5% VAT Charges and your total fee is', 340*5/100+340, 'USD')
                        else:
                            print(f'Invalid selection ({enter2}).')
                    except:
                        print(
                            f'Your selection ({enter2}) must be numbers only.')

                elif enter == 'Laptop' or enter == 'Laptops':
                    print(
                        'These are the available laptops we have: \n 1. HP Pavilion ($1250) \n Lenovo 2. ThinkBook ($890) \n 3. Apple MacBook ($2200)')
                    try:
                        enter3 = int(input(
                            'Enter 1 to order HP Pavilion \n Enter 2 for Lenovo ThinkBook \n Enter 3 for Apple MacBook'))
                        if enter3 == 1:
                            print(
                                f'You have successfully placed an order for HP Pavillion which costs $1250 plus 5% VAT Charges and your total fee is', 1250*5/100+1250, 'USD')
                        elif enter3 == 2:
                            print(
                                f'You have successfully placed an order for Lenovo ThinkBook which costs $890 plus 5% VAT Charges and your total fee is', 890*5/100+890, 'USD')
                        elif enter3 == 3:
                            print(
                                f'You have successfully placed an order for Apple MacBook which costs $2200 plus 5% VAT Charges and your total fee is', 2200*5/100+2200, 'USD')
                        else:
                            print(f'invalid selection ({enter3})')
                    except:
                        print(
                            f'Your selection ({enter3}) must be numbers only.')

                elif enter == 'Computer' or enter == 'Computers':
                    print('These are the available computers we have: \n 1. Mainframe Computer ($800) \n 2. Workstation Computer ($700) \n 3. Apple Macintosh (Mac) ($3500)')
                    try:
                        enter4 = int(input(
                            'Enter 1 to order Mainframe Computer \n Enter 2 for Workstation Computer \n Enter 3 for Apple Macintosh (Mac)'))
                        if enter4 == 1:
                            print(
                                f'You have successfully placed an order for Mainframe Computer which costs $800 plus 5% VAT Charges and your total fee is', 800*5/100+800, 'USD')
                        elif enter4 == 2:
                            print(
                                f'You have successfully placed an order for Workstation Computer which costs $700 plus 5% VAT Charges and your total fee is', 700*5/100+700, 'USD')
                        elif enter4 == 3:
                            print(
                                f'You have successfully placed an order for Apple Macintosh (Mac) which costs $3500 plus 5% VAT Charges and your total fee is', 3500*5/100+3500, 'USD')
                        else:
                            print(f'Invalid selection ({enter4})')
                    except:
                        print(
                            f'Your selection ({enter4}) must be numbers only.')

                elif enter == 'Printer' or enter == 'Printers':
                    print('These are the available computers we have: \n 1. Laser Printers ($4000) \n 2. Solid Ink Printers ($7100) \n 3. LED Printers ($5000)')
                    try:
                        enter5 = int(input(
                            'Enter 1 to order Laser Printers \n Enter 2 for Solid Ink Printers \n Enter 3 for LED Printers'))
                        if enter5 == 1:
                            print(
                                f'You have successfully placed an order for Laser Printers which costs $4000 plus 5% VAT Charges and your total fee is', 4000*5/100+4000, 'USD')
                        elif enter5 == 2:
                            print(
                                f'You have successfully placed an order for Solid Ink Printers which costs $7100 plus 5% VAT Charges and your total fee is', 7100*5/100+7100, 'USD')
                        elif enter5 == 3:
                            print(
                                f'You have successfully placed an order for LED Printers which costs $5000 plus 5% VAT Charges and your total fee is', 5000*5/100+5000, 'USD')
                        else:
                            print(f'Invalid selection ({enter5})')
                    except:
                        print(
                            f'Your selection ({enter5}) must be numbers only.')

                else:
                    print(f'Invalid selection ({enter}).')
            elif order1 == 2:
                print(self.grocery)
                grocery = input(
                    'The above groceries are available, place your order by entering the correct name of the product.').capitalize()
                if grocery == 'Bread' or grocery == 'Breads':
                    print(
                        'These are the available Breads we have:\n 1. Sourdough ($25) \n 2. Baguette ($350) \n 3. Brioche ($140)')
                    try:
                        select = int(
                            input('Enter 1 for Sourdough \n Enter 2 for Baguette \n Enter 3 for Brioche'))
                        if select == 1:
                            print(
                                f'You have successfully placed an order for Sourdough which costs $25 plus 5% VAT Charges and your total fee is', 25*5/100+25, 'USD')
                        elif select == 2:
                            print(
                                f'You have successfully placed an order for Baguette which costs $350 plus 5% VAT Charges and your total fee is', 350*5/100+350, 'USD')
                        elif select == 3:
                            print(
                                f'You have successfully placed an order for Brioche which costs $140 plus 5% VAT Charges and your total fee is', 140*5/100+140, 'USD')
                        else:
                            print(f'Invalid selection ({select})')
                    except:
                        print(
                            f'Your selection ({select}) must be numbers only.')
                elif grocery == 'Meat' or grocery == 'Meats':
                    print(
                        'These are the available Meats we have:\n 1. Chicken ($75) \n 2. Turkey ($80) \n 3. Goat ($100)')
                    try:
                        select1 = int(
                            input('Enter 1 for Chicken \n Enter 2 for Turkey \n Enter 3 for Goat'))
                        if select1 == 1:
                            print(
                                f'You have successfully placed an order for Chicken which costs $75 plus 5% VAT Charges and your total fee is', 75*5/100+75, 'USD')
                        elif select1 == 2:
                            print(
                                f'You have successfully placed an order for Turkey which costs $80 plus 5% VAT Charges and your total fee is', 80*5/100+80, 'USD')
                        elif select1 == 3:
                            print(
                                f'You have successfully placed an order for Goat which costs $100 plus 5% VAT Charges and your total fee is', 100*5/100+100, 'USD')
                        else:
                            print(f'Invalid selection ({select1})')
                    except:
                        print(
                            f'Your selection ({select1}) must be numbers only.')

                elif grocery == 'Pasta' or grocery == 'Pastas':
                    print(
                        'These are the available Pastas we have:\n 1. Bow Tie Pasta ($95) \n 2. Bucatini Pasta ($120) \n 3. Ditalini Pasta ($130)')
                    try:
                        select2 = int(input(
                            'Enter 1 for Bow Tie Pasta \n Enter 2 for Bucatini Pasta \n Enter 3 for Ditalini Pasta'))
                        if select2 == 1:
                            print(
                                f'You have successfully placed an order for Bow Tie Pasta which costs $95 plus 5% VAT Charges and your total fee is', 95*5/100+95, 'USD')
                        elif select2 == 2:
                            print(
                                f'You have successfully placed an order for Bucatini Pasta which costs $120 plus 5% VAT Charges and your total fee is', 120*5/100+120, 'USD')
                        elif select2 == 3:
                            print(
                                f'You have successfully placed an order for Ditalini Pasta which costs $130 plus 5% VAT Charges and your total fee is', 130*5/100+130, 'USD')
                        else:
                            print(f'Invalid selection ({select2})')
                    except:
                        print(
                            f'Your selection ({select2}) must be numbers only.')

                elif grocery == 'Cheese' or grocery == 'Cheeses':
                    print(
                        'These are the available Cheese we have:\n 1. Mozzarella  ($15) \n 2. Gouda  ($20) \n 3. Emmental  ($30)')
                    try:
                        select3 = int(
                            input('Enter 1 for Mozzarella \n Enter 2 for Gouda \n Enter 3 for Emmental'))
                        if select3 == 1:
                            print(
                                f'You have successfully placed an order for Mozarella which costs $15 plus 5% VAT Charges and your total fee is', 15*5/100+15, 'USD')
                        elif select3 == 2:
                            print(
                                f'You have successfully placed an order for Gouda which costs $20 plus 5% VAT Charges and your total fee is', 20*5/100+20, 'USD')
                        elif select3 == 3:
                            print(
                                f'You have successfully placed an order for Emmental which costs $30 plus 5% VAT Charges and your total fee is', 30*5/100+30, 'USD')
                        else:
                            print(f'Invalid selection ({select3})')
                    except:
                        print(
                            f'Your selection ({select3}) must be numbers only.')
                else:
                    print(f'Invalid selection ({select3})')

            elif order1 == 3:
                print(self.restaurants)
                restaurant = input(
                    'The above Foods are available in our restaurant, place your order by entering the correct name of the product.').capitalize()
                if restaurant == 'Swallow' or restaurant == 'Swallows':
                    print(
                        'These are the available Swallows we have:\n 1. Eba ($5) \n 2. Fufu ($7) \n 3. Semovita ($9)')
                    try:
                        choose = int(
                            input('Enter 1 for Eba \n Enter 2 for Fufu \n Enter 3 for Semovita'))
                        if choose == 1:
                            print(
                                f'You have successfully placed an order for Eba which costs $5 plus 5% VAT Charges and your total fee is', 5*5/100+5, 'USD')
                        elif choose == 2:
                            print(
                                f'You have successfully placed an order for Fufu which costs $7 plus 5% VAT Charges and your total fee is', 7*5/100+7, 'USD')
                        elif choose == 3:
                            print(
                                f'You have successfully placed an order for Semovita which costs $9 plus 5% VAT Charges and your total fee is', 9*5/100+9, 'USD')
                        else:
                            print(f'Invalid selection ({choose})')
                    except:
                        print(
                            f'Your selection ({choose}) must be numbers only.')

                elif restaurant == 'Bean' or restaurant == 'Beans':
                    print(
                        f'You have successfully placed an order for Beans which costs $10 plus 5% VAT Charges and your total fee is', 10*5/100+10, 'USD')

                elif restaurant == 'Plantain' or restaurant == 'Plantains':
                    print(
                        f'You have successfully placed an order for Plantain which costs $20 plus 5% VAT Charges and your total fee is', 20*5/100+20, 'USD')

                elif restaurant == 'Fish' or restaurant == 'Fishes':
                    print(
                        'These are the available Fishes we have:\n 1. Tilapia ($50) \n 2. Catfish ($70) \n 3. Salmon ($90)')
                    try:
                        restaurant1 = int(
                            input('Enter 1 for Tilapia \n Enter 2 for Catfish \n Enter 3 for Salmon'))
                        if restaurant1 == 1:
                            print(
                                f'You have successfully placed an order for Tilapia which costs $50 plus 5% VAT Charges and your total fee is', 50*5/100+50, 'USD')
                        elif restaurant1 == 2:
                            print(
                                f'You have successfully placed an order for Catfish which costs $70 plus 5% VAT Charges and your total fee is', 70*5/100+70, 'USD')
                        elif restaurant1 == 3:
                            print(
                                f'You have successfully placed an order for Salmon which costs $90 plus 5% VAT Charges and your total fee is', 90*5/100+90, 'USD')
                        else:
                            print(f'Invalid selection ({restaurant1})')
                    except:
                        print(
                            f'Selection ({restaurant1}) must be numbers only.')

                else:
                    print(f'Invalid selection ({restaurant})')

            elif order1 == 4:
                print(self.clothes)
                print(
                    'Enter 1 for Jeans ($55) \n Enter 2 for Polo ($44) \n Enter 3 for T-Shirt ($33) \n Enter 4 for Hoodie ($20)')
                try:
                    clothes1 = int(input(
                        'Enter 1 for Jeans ($55) \n Enter 2 for Polo ($44) \n Enter 3 for T-Shirt ($33) \n Enter 4 for Hoodie ($20)'))
                    if clothes1 == 1:
                        print(
                            f'You have successfully placed an order for Jeans which costs $55 plus 5% VAT Charges and your total fee is', 55*5/100+55, 'USD')
                    elif clothes1 == 2:
                        print(
                            f'You have successfully placed an order for Polo which costs $44 plus 5% VAT Charges and your total fee is', 44*5/100+44, 'USD')
                    elif clothes1 == 3:
                        print(
                            f'You have successfully placed an order for T-Shirt which costs $33 plus 5% VAT Charges and your total fee is', 33*5/100+33, 'USD')
                    elif clothes1 == 4:
                        print(
                            f'You have successfully placed an order for Hoodie which costs $20 plus 5% VAT Charges and your total fee is', 20*5/100+20, 'USD')
                    else:
                        print(f'Invalid selection ({clothes1})')
                except:
                    print(f'Selection ({clothes1}) must be numbers only.')

            elif order1 == 5:
                print(self.accessory)
                print(
                    'Enter 1 for Watch ($39) \n Enter 2 for Sun Shade ($54) \n Enter 3 for Necklace ($39) \n Enter 4 for Wallet ($21)')
                try:
                    accessory1 = int(
                        input('Enter 1 for Watch ($39) \n Enter 2 for Sun Shade ($54) \n Enter 3 for Necklace ($39) \n Enter 4 for Wallet ($21)'))
                    if accessory1 == 1:
                        print(
                            f'You have successfully placed an order for Watch which costs $39 plus 5% VAT Charges and your total fee is', 39*5/100+39, 'USD')
                    elif accessory1 == 2:
                        print(
                            f'You have successfully placed an order for Sun Shade which costs $54 plus 5% VAT Charges and your total fee is', 54*5/100+54, 'USD')
                    elif accessory1 == 3:
                        print(
                            f'You have successfully placed an order for Necklace which costs $39 plus 5% VAT Charges and your total fee is', 39*5/100+39, 'USD')
                    elif accessory1 == 4:
                        print(
                            f'You have successfully placed an order for Wallet which costs $21 plus 5% VAT Charges and your total fee is', 21*5/100+21, 'USD')
                    else:
                        print(f'Invalid selection ({accessory1})')
                except:
                    print(f'Selection ({accessory1}) must be numbers only.')

            elif order1 == 6:
                print(self.pharmacy)
                print(
                    'Enter 1 for Paracetamol ($3) \n Enter 2 for Panadol Extra ($4) \n Enter 3 for Inhaler ($5) \n Enter 4 for Flagyl ($2)')
                try:
                    pharmacy1 = int(
                        input('Enter 1 for Paracetamol ($3) \n Enter 2 for Panadol Extra ($4) \n Enter 3 for Inhaler ($5) \n Enter 4 for Flagyl ($2)'))
                    if pharmacy1 == 1:
                        print(
                            f'You have successfully placed an order for Paracetamol which costs $3 plus 5% VAT Charges and your total fee is', 3*5/100+3, 'USD')
                    elif pharmacy1 == 2:
                        print(
                            f'You have successfully placed an order for Panadol Extra which costs $4 plus 5% VAT Charges and your total fee is', 4*5/100+4, 'USD')
                    elif pharmacy1 == 3:
                        print(
                            f'You have successfully placed an order for Inhaler which costs $5 plus 5% VAT Charges and your total fee is', 5*5/100+5, 'USD')
                    elif pharmacy1 == 4:
                        print(
                            f'You have successfully placed an order for Flagyl which costs $2 plus 5% VAT Charges and your total fee is', 2*5/100+2, 'USD')
                    else:
                        print(f'Invalid selection ({pharmacy1})')
                except:
                    print(f'Selection ({pharmacy1}) must be numbers only.')

            else:
                print('Department doesn\'t exist')
        except:
            print('Department selection must be numbers only.')


obj = Customer()
obj.Order()
