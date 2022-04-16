class Shoppingcart():
    def __init__(self, basket=[]):
        self.basket = basket
        
    def add_item(self):
        name = input("What would you like to add?")
        quantity = int(input("How much do you want?"))     
        for i in range(quantity):
            self.basket.append(name)
        print(f'You have successfully added {quantity} {name} items.')

    def del_item(self):
        my_set = list(set(self.basket))
        decision = input(f"What would you like to remove from your cart? Here is what is currently in your cart. {my_set}.")
        if decision in my_set:
            quant_dec = int(input(f'How many would like to remove? You currently have {self.basket.count(decision)} of these items in your cart.'))
            for i in range(quant_dec):
                self.basket.remove(decision)
            print(list(set(self.basket)))
        else:
            print('Invalid choice')

Shoppingcart().add_item()
Shoppingcart().del_item()