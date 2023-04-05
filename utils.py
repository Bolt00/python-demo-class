import requests
base_url = 'https://fakestoreapi.com'
endpoints = {
    'products': '/products',
    'categories': '/products/categories'
}


def get_products():
    url = base_url + endpoints['products']
    return requests.get(url=url).json()[:50]


def get_categories():
    url = base_url + endpoints['categories']
    return requests.get(url).json()

    


if __name__ == '__main__':
    print(get_categories())
