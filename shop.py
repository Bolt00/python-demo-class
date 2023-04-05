import utils
from pprint import pprint
import time
import requests

a = []

products_db = utils.get_products()

# print(products_db)

last_index = 0

products_db = utils.get_products()


def view_products():
    global last_index
    display_prods = []
    next_index = last_index + 2
    for prod in products_db[last_index:next_index]:
        hold = []
        hold.append(prod['id'])
        hold.append(prod['title'])
        hold.append(prod['price'])
        display_prods.append(hold)
    last_index = next_index
    print(display_prods)

base_url = 'https://fakestoreapi.com'
endpoints = {
    'products': '/products',
    'categories': '/products/categories'
}
url = base_url + endpoints['products']
cart = base_url + '/carts'

def cart():
        cart = requests.post(order, json=cart)
        print(f'You have successfully added {cart} to your carts')



while True:
    print('1) View products \n 2) Place an order')
    cmd = input('type here>> ')
    if cmd == '1':
        view_products()

    elif cmd == '2':
        print('Enter the id of the products to place an order')
        order = input('>>>')
        if order in url:
            cart()
            
    else:
        print('Invalid option')
        break


