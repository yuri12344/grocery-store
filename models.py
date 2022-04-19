from datetime import datetime

class Category():
    def __init__(self, category) -> None: 
        self.category = category

class Product():
    def __init__(self, name, price, category) -> None: 
        self.name = name
        self.price = price
        self.category = category

class Stock:
    def __init__(self, product: Product, quantity) -> None:
        self.product = product
        self.quantity = quantity

class Sale:
    def __init__(self, itens_sold: Product, salesman, buyer, quantity_sould, date = datetime.now().strftime('%d/%m/%Y')) -> None:
        self.itens_sold = itens_sold
        self.salesman = salesman
        self.buyer = buyer
        self.quantity_sould = quantity_sould
        self.date = date

class Provider():
    def __init__(self, name, cnpj, phone, category) -> None: 
        self.name = name
        self.cnpj = cnpj
        self.phone = phone
        self.category = category

class Person:
    def __init__(self, name, phone, cpf, email, address) -> None: 
        self.name = name
        self.phone = phone
        self.cpf = cpf
        self.email = email
        self.address = address

class Employee(Person):
    def __init__(self, name, phone, cpf, email, address, clt) -> None: 
        super().__init__(name, phone, cpf, email, address)
        self.clt = clt






