class ShoppingCart(object):
    # Creates shopping cart objects
    items_in_cart = {}
    def __init__(self, customer_name):
        self.customer_name = customer_name

    def add_item(self, product, price):
        # Add product to the cart
        if not product in self.items_in_cart:
            self.items_in_cart[product] = price
            print(product + " added, price is", price)
        else:
            print(product + " is already in the cart.")

    def remove_item(self, product):
        # Remove product from the cart
        if product in self.items_in_cart:
            del self.items_in_cart[product]
            print(product + " removed.")
        else:
            print(product + " is not in the cart.")

    def print_out_cart(self):
        print('Your cart:')
        for key in self.items_in_cart:
            print('Product:', key, 'price:', self.items_in_cart[key])


def choice():       # choice of action
    ch = ''
    while ch != '1' and ch != '2' and ch != '3':
        print('Select further action:', '\n' + '1. Continue adding products to cart', '\n' + '2. Remove product from cart', '\n' + '3. Exit')
        ch = input()
        ch = str(ch)
    return ch

answ = ''
while answ != 'y' and answ != 'n':
    answ = input('Would you like to add products to your cart? (y-Yes or n-No)')
    answ = str(answ.lower())
if 'n' == answ:
    print('By!')
    raise SystemExit()

# while in cart add actions
my_cart = ShoppingCart(input('Hi! Enter your name: '))
while answ == 'y':
    x = input('Enter name of product to add into cart: ')
    y = input('Price: ')
    my_cart.add_item(x, y)
    answ = ''
    while answ != 'y' and answ != 'n':
        answ = input('Would you like to continue to add products to your cart? (y-Yes or n-No)')
        answ = str(answ.lower())
    if answ == 'n':
        res1 = choice()
        if res1 == '1':
            answ = 'y'
        elif res1 == '2':
            my_cart.print_out_cart()
            x = input('Enter name of item to be removed from cart: ')
            my_cart.remove_item(x)
            answ = 'y'          # Not resolved what to do after removing from cart
        else:
            print('By! Come back!')
            break