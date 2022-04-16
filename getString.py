class convertStrings():
    def __init__(self):
        self.items = ""

    # Method to take string input
    def get_String(self):
        self.items = input('Please enter a message.')
    
    # Method to convert string to upper case only.
    def print_String(self):
        print(self.items.upper())

items = convertStrings()
items.get_String()
items.print_String()