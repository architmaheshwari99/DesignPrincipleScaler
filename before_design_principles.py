class Order:
    def __init__(self, items, customer_name, address):
        self.items = items
        self.customer_name = customer_name
        self.address = address

    def calculate_total(self):
        total = 0
        for item in self.items:
            total += item['price'] * item['quantity']
        return total

    def print_invoice(self):
        print(f"Invoice for {self.customer_name}")
        for item in self.items:
            print(f"{item['name']} - {item['quantity']} x ${item['price']}")
        print(f"Total: ${self.calculate_total()}")

    def save_to_database(self):
        # Pseudo code for saving to a database
        print(f"Saving order for {self.customer_name} to the database")
