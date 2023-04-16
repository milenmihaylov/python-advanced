def check_product_limits(meal_type, products_num):
    limits = {
        'Soup': 3,
        'Pizza': 4,
        'Dessert': 2
    }
    return products_num < limits[meal_type]


def sorting(cart: dict):
    for key, value in cart.items():
        cart[key] = sorted(list(value))
    return sorted(cart.items(), key=lambda x: (-len(x[1]), x[0]))


def check_if_products(cart):
    for x, y in cart:
        if len(y) > 0:
            return True
    return False


def formatting(cart: list):
    if not check_if_products(cart):
        return "No products in the cart!"
    return_string = ''
    first_el = True
    for key, value in cart:
        if not first_el:
            return_string += '\n'
        return_string += key + ':'
        for x in value:
            return_string += f'\n - {x}'
        first_el = False
    return return_string


def shopping_cart(*args):
    cart = {
        'Soup': set(),
        'Pizza': set(),
        'Dessert': set()
    }
    for tup in args:
        if tup == 'Stop':
            # Sort
            sorted_cart = sorting(cart)
            # Format and return
            return formatting(sorted_cart)

        meal_type, product = tup

        if check_product_limits(meal_type, len(cart[meal_type])):
            cart[meal_type].add(product)

    sorted_cart = sorting(cart)
    return formatting(sorted_cart)


print(shopping_cart(
    ('Pizza', 'ham'),
    ('Soup', 'carrots'),
    ('Pizza', 'cheese'),
    ('Pizza', 'flour'),
    ('Dessert', 'milk'),
    ('Pizza', 'mushrooms'),
    ('Pizza', 'tomatoes'),
    'Stop',
))