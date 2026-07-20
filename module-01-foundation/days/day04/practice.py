# Exercise 1: Book class

class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def describe(self):
        print(f"{self.title} by {self.author}, {self.pages} pages")


book1 = Book("The Alchemist", "Paulo Coelho", 208)
book2 = Book("Python Basics", "John Smith", 300)

book1.describe()
book2.describe()


# Exercise 2, 3, and 4: Product class

class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.__quantity = quantity

    # Getter: allows us to read the private quantity
    @property
    def quantity(self):
        return self.__quantity

    # Setter: prevents the quantity from becoming negative
    @quantity.setter
    def quantity(self, value):
        if value < 0:
            print("Quantity cannot be below zero.")
        else:
            self.__quantity = value

    def restock(self, n):
        if n > 0:
            self.__quantity += n

    def sell(self, n):
        if n <= 0:
            print("Sell amount must be positive.")
        elif n > self.__quantity:
            print("Not enough items in stock.")
        else:
            self.__quantity -= n


# Exercise 5: Prove independence

product1 = Product("Phone", 15000, 10)
product2 = Product("Laptop", 40000, 5)
product3 = Product("Headphones", 3000, 20)

product1.sell(3)

print(f"{product1.name}: {product1.quantity}")
print(f"{product2.name}: {product2.quantity}")
print(f"{product3.name}: {product3.quantity}")
