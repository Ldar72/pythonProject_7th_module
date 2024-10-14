file = open('products.txt', 'w')
file.close()
class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'

class Shop:
    __file_name = 'products.txt'

    def get_products(self):
       file = open(self._Shop__file_name, 'r')
       return file.read()
       file.close()

    def add(self, *products):
        existing_products = self.get_products().strip().split('\n') if self.get_products() else []
        existing_names = {product.split(', ')[0] for product in existing_products}

        for product in products:
            if product.name in existing_names:
                print(f'Продукт {product} уже есть в магазине')
            else:
                with open(self.__file_name, 'a') as file:
                    file.write(f'{product}\n')

s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')
p4 = Product('Carrot', 10.5, 'Vegetables')

print(p2)

s1.add(p1, p2, p3, p4)

print(s1.get_products())