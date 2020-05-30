class Customer:
    'This is Customer class'

    def __init__(self, name, phone, address):
        self.name = name
        self.phone = phone
        self.address = address


john = Customer("John", 1234567, "USA")

print("john.__dict__ = ", john.__dict__)
