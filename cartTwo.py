class Cart():
    def __init__(self, cart={}):
        self.cart = cart

    def add_item(self):
        item_add = input("\nWhat item would you like to add? ")
        quantity_add = int(input(f"\nHow many {item_add} would you like to add? "))
        self.cart[item_add] = quantity_add
        print(f'Here is self.cart as of right now: {self.cart}')
        print(f"{quantity_add} {item_add} was/were added to your cart.")

    def remove_item(self, item_del, quantity_del):
        self.cart[item_del] -= quantity_del
        print(f"{quantity_del} {item_del} was/were removed from your cart.")

    def show_cart(self):
        print(f'Here is self.cart when I click \'show\': {self.cart}.')
        if self.cart == {}:
            print("\nYour shopping cart is empty.")
        else:
            print("\nYour shopping cart items are: ")
            for key, value in self.cart.items():
                print(f"{key} - {value}")

    def clear_cart(self):
        self.cart.clear()
        print("\nYour shopping cart is now empty.")

    def quit(self):
        if self.cart == {}:
            print("\nYour shopping cart is empty. Goodbye.")
        else:
            print("\nYou left the following items in your cart without purchasing: ")
            for key, value in self.cart.items():
                print(f"{key} - {value}")
            print("\nGoodbye.")

class UI(Cart):
    def __init__(self):
        super().__init__()

    def user_interface():
        print("Welcome to your shopping cart!")
        myCart = Cart()
        print(myCart)
        while True:
            action = input("\nDo you want to add items ['add'], remove items ['remove'], show your cart ['show'], clear your cart['clear'], or quit ['quit']? ")
            if action.lower().strip() == "add":
                myCart.add_item()
            elif action.lower().strip() == "remove":
                item_rem = input("\nWhat item would you like to remove? ")
                quantity_rem = int(input(f"\nHow many {item_rem} would you like to delete? ")) 
                myCart.remove_item(item_rem, quantity_rem)
            elif action.lower().strip() == "show":
                myCart.show_cart()    
            elif action.lower().strip() == "clear":
                Cart.clear_cart()
            elif action.lower().strip() == "quit":
                Cart.quit()
                break
            else:
                print("\nInvalid entry. Please select a valid option.")
            
UI.user_interface()