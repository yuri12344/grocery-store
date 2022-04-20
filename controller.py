from math import prod
from xmlrpc.client import Boolean

from models import *
from DAO import *
from ipdb import set_trace as st

class ControllerCategory:
    def registerCategory(self, new_category):
        all_cat = DaoCategory.read()
        already_exists = False
        for i in all_cat:
            if i.category == new_category:
                already_exists = True
                break
        if not already_exists:
           DaoCategory.save(new_category) 
           print(f'Category {new_category} sucessfull registered')
        else:
            print(f'The category {new_category} already exists')


    def deleteCategory(self, categoryToRemove):
        x = DaoCategory.read()
        cat = list(filter(lambda x: x.category == categoryToRemove, x))

        if len(cat) == 0:
            print(f'The category {categoryToRemove} does not exist')

        else:
            for i in range(len(x)):
                if x[i].category == categoryToRemove:
                    del x[i]
                    print('Category sucessfull removed')
                    break
        with open('categorys.txt', 'w') as f:
            for i in x:
                f.writelines(f'{i.category}\n')
        # TODO: REMOVER FROM THE STOCKS LIST

    def changeCategory(self, old_category, new_category):
        all_cats = DaoCategory.read()
        cat = list(filter(lambda x: x.category == old_category, all_cats))
        if len(cat) > 0:
            'Verify is new category already exists'
            res = list(filter(lambda x: x.category == new_category, all_cats))
            
            if len(res) == 0:

                new_res = []
                for item in all_cats:
                    if item.category == old_category:
                        new_res.append(Category(new_category))
                        print('Success')
                    else:
                        new_res.append(item)
            else:
                print('The category already exists')
        else:
            print(f'The {new_category} does not exists, you should create first')
        with open('categorys.txt', 'w') as f:
            for i in new_res:
                f.writelines(f'{i.category}\n')
        # TODO - REMOVE CATEGORY FROM STOCK

    def listAllCategorys(self):
        category = DaoCategory.read()
        if len(category) == 0:
            print('Does not exists categorys registereds')
        else:
            for i in category:
                print(f'Category: {i.category}')

class ControllerStock:
    def registerProduct(self, name, price, category, quantity):
        all_stocks = DaoStock.read()
        all_categorys = DaoCategory.read()
        category_exists = list(filter(lambda x: x.category == category, all_categorys))
        stock = list(filter(lambda x: x.product.name == name, all_stocks))
        if len(category_exists) > 0 and len(stock) != 0:
            if len(stock) == 0:
                product = Product(name, price, category)
                DaoStock.save(product, quantity)
                print('Sucess product registered')
        else:
            print('Product already exists in stock')
    
    def removeProduct(self, name):
        all_stocks = DaoStock.read()
        stock = list(filter(lambda x: x.product.name == name, all_stocks))
        if len(stock) == 0:
            print(f'The product {name} does not exists')

        else:
            for i in range(len(all_stocks)):
                if all_stocks[i].product.name == name:
                    del all_stocks[i]
                    print('Product sucessfull removed')
                    break

        with open('stocks.txt', 'w') as f:
            for i in all_stocks:
                f.writelines(f'{i.product.name} {i.quantity}\n')

    def changeProduct(self, name, new_name, new_price, new_category, new_quantity):
        all_stocks = DaoStock.read()
        all_categorys = DaoCategory.read()

        'Verify if the new category exists and if the product exists'
        category_exists = list(filter(lambda x: x.category == new_category, all_categorys))
        old_product_exists = list(filter(lambda x: x.product.name.replace(" ", "") == name.replace(" ", ""), all_stocks))
        new_product_exists = list(filter(lambda x: x.product.name.replace(" ", "") == new_name.replace(" ", ""), all_stocks))
        
        if len(category_exists) != 0 and len(old_product_exists) != 0 and len(new_product_exists) == 0:
            all_stocks = list(map(lambda x: Stock(Product(new_name, new_price, new_category), new_quantity) if(x.product.name.replace(" ", "") == name.replace(" ", "")) else (x), all_stocks))
            print(f'Product {name} sucessfull changed to {new_name} and others atributes')
        
        else:
           print(f'Maybe the category {new_category} does not exists or the new product {new_name} already exists')
            

        with open('stocks.txt', 'w') as f:
            for i in all_stocks:
                f.writelines(f'{i.product.name}|{i.product.price}|{i.product.category}|{i.quantity}\n')

        if len(category_exists) == 0:
            print(f'The category {new_category} where you trying to change does not exists')


    def listAllProducts(self):
        all_stock = DaoStock.read()

        if len(all_stock) == 0:
            print('Does not exists products registereds')

        else:
            print("Products registereds:")
            for i in all_stock:
                print(f'Product: {i.product.name} - Price: {i.product.price} - Category: {i.product.category} - Quantity: {i.quantity}')

class ControllerSales:
    """
    return 1: product does not exists
    return 2: product is not in stock
    return 3 and value of sale: sucessfull sale

    :param name: name of the product;
    :param quantity: quantity of the product;
    :param price: price of the product;
    :param category: category of the product;
    """

    def registerSale(self, name_of_sale_product, salesman, buyer, quantity_sould):
        products_in_stock = DaoStock.read()
        temp = []
        prod_exists = False
        have_in_stock = False

        for prod in products_in_stock:
            if prod.product.name == name_of_sale_product and int(prod.quantity) >= int(quantity_sould):
                prod.quantity = int(prod.quantity) - int(quantity_sould)
                sould = Sale(Product(prod.product.name, prod.product.price, prod.product.category), salesman, buyer, quantity_sould)
                DaoSale.save(sould)

                value_of_sale = int(quantity_sould) * int(prod.product.price)
                tempx = [Product(prod.product.name, prod.product.price, prod.product.category), prod.quantity]
                temp.append(tempx)

                prod_exists, have_in_stock = True, True

        with open('stocks.txt', 'w') as arq:
            for i in products_in_stock:
                arq.writelines(f'{i.product.name}|{i.product.price}|{i.product.category}|{i.quantity}\n')
        
        if prod_exists == False:
            return 1
        elif not have_in_stock:
            return 2
        else:
            return 3, value_of_sale

    def productsReports(self):
        all_sales = DaoSale.read()
        if len(all_sales) == 0: print('Does not exists sales registereds')

        products = []
        for i in all_sales:
            name = i.itens_sold.name
            quantity = i.quantity_sould
            size = list(filter(lambda x: x['product'] == name, products))

            if len(size) != 0:
                products = list(map(lambda x: {'product': name, 'quantity': int(x['quantity']) +int(quantity) } 
                if x['product'] == name else x, products))
            else:
                products.append({'product': name, 'quantity': quantity})

        ordenated = sorted(products, key=lambda k: k['quantity'], reverse=True)
      
        print('Most sold products:')
        for i in ordenated:
            print(f'Product: {i["product"]} - Quantity: {i["quantity"]}')





a = ControllerSales()
#print(a.registerSale('maca', 'João', 'Maria', '2'))
print(a.registerSale('banana', 'João', 'Maria', '2'))
