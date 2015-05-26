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
        print('Select action:', '\n' + '1. Add product to the cart', '\n' + '2. Remove product from the cart', '\n' + '3. Log out')
        ch = input()
        ch = str(ch)
    return ch

def in_cart():      # user in cart until log out
    name = input('Enter your name: ')
    my_cart = ShoppingCart(name)
    res1 = '1'
    while res1 != '3':
        res1 = choice()
        if res1 == '1':
            x = input('Enter name of product to add into cart: ')
            y = input('Price: ')
            my_cart.add_item(x, y)
        elif res1 == '2':
            my_cart.print_out_cart()
            my_cart.remove_item(input('Enter product name to remove it from cart: '))
    my_cart.print_out_cart()
    print('By,', name + '! You logged out.')

# main part
                 
answer = ''
while answer != 'y' and answer != 'n':
    answer = input('Hi! Would you like to add products to your cart? (y-Yes or n-No)')
    answer = str(answer.lower())
if answer == 'n':
    print('By!')
    raise SystemExit()
else:
    in_cart()
