from models import *


class DaoCategory:
    @classmethod
    def save(cls, category):
        with open('categorys.txt', 'a') as file:
            file.writelines(f'{category}\n')

    @classmethod
    def read(cls):
        with open('categorys.txt', 'r') as file:
            cls.category = file.readlines()
        cls.category = list(map(lambda x: x.replace('\n', ''), cls.category))
        return [Category(i) for i in cls.category]


class DaoSale:
    @classmethod
    def save(cls, sale: Sale):
        with open('sales.txt', 'a') as file:
            file.writelines(f'{sale.itens_sold.name} | {sale.itens_sold.price} | {sale.itens_sold.category} | {sale.salesman} | {sale.buyer} | str({sale.quantity_sould}) | {sale.date}\n')

    @classmethod
    def read(cls):
        with open('sales.txt', 'r') as file:
            cls.sales = file.readlines()
            cls.sales = list(map(lambda x: x.replace('\n', ''), cls.sales))
            cls.sales = list(map(lambda x: x.split('|'), cls.sales))
            return [Sale(Product( i[0], i[1], i[2] ),  i[3], i[4], i[5], i[6]  ) for i in cls.sales]


class DaoStock:
    @classmethod
    def save(cls, product: Product, quantify):
        with open('stocks.txt', 'a') as file:
            file.writelines(f'{product.name} | {product.price} | {product.category} | {str(quantify)}\n')

    @classmethod
    def read(cls):
        with open('stocks.txt', 'r') as file:
            cls.stock = file.readlines()

        cls.stock = list(map(lambda x: x.replace('\n', ''), cls.stock))
        cls.stock = list(map(lambda x: x.split('|'), cls.stock))
        return [Stock(Product( i[0], i[1], i[2] ),  i[3]  ) for i in cls.stock]


class DaoProvider:
    @classmethod
    def save(cls, provider: Provider):
        with open('providers.txt', 'a') as file:
            file.writelines(f'{provider.name} | {provider.cnpj} | {provider.phone} | {provider.category}\n')

    @classmethod
    def read(cls):
        with open('provideres.txt', 'r') as file:
            cls.providers = file.readlines()
        
        cls.providers = list(map(lambda x: x.replace('\n', ''), cls.providers))
        cls.providers = list(map(lambda x: x.split('|'), cls.providers))
        return [Provider( i[0], i[1], i[2], i[3] ) for i in cls.providers]


class DarPerson:
    @classmethod
    def save(cls, person: Person):
        with open('clientes.txt', 'a') as file:
            file.writelines(f'{person.name} | {person.phone} | {person.cpf} | {person.email} | {person.endereco}\n')

    @classmethod
    def read(cls):
        with open('clientes.txt', 'r') as file:
            cls.persons = file.readlines()
        
        cls.persons = list(map(lambda x: x.replace('\n', ''), cls.persons))
        cls.persons = list(map(lambda x: x.split('|'), cls.persons))
        return [Person(i[0], i[1], i[2], i[3], i[4]) for i in cls.persons]


class DaeEmployee:
    @classmethod
    def save(cls, employe: Employee):
        with open('employes.txt', 'a') as file:
            file.writelines(f'{employe.clt} | {employe.name} | {employe.phone} | {employe.cpf} | {employe.email} | {employe.address}\n')

    def read(cls):
        with open('employes.txt', 'r') as file:
            cls.employes = file.readlines()
        cls.employes = list(map(lambda x: x.replace('\n', ''), cls.employes))
        cls.employes = list(map(lambda x: x.split('|'), cls.employes))
        return [Employee(i[0], i[1], i[2], i[3], i[4], i[5]) for i in cls.employes]




