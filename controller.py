from xmlrpc.client import Boolean
from models import *
from DAO import *

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

        if len(category_exists) == 0:
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