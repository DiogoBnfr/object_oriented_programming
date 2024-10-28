from decimal import Decimal

class Product:
    totalProducts = 0
    
    def __init__(self, description, price, cost):
        self.productId = self.totalProducts
        self.description = description
        self.price = price
        self.cost = cost

    def getDescription(self):
        return self.description
    def getPrice(self):
        return self.price
    def getCost(self):
        return self.cost
    def setDescription(self, description):
        self.description = description
    def setPrice(self, price):
        if (self.price * Decimal(0.9) < price < self.price * Decimal(1.1)):
            self.price = price
    def setCost(self, cost):
        self.cost = cost
        
    def calculateMargin(self):
        return ((self.price - self.cost) / self.price) * 100

products = []

while (True):
    print('''
    1. Register product
    2. Calculate margin
    3. List products
    4. Update product
    5. Quit
    ''')
    opt = int(input("Insert option: "))

    if (opt == 1):
        Product.totalProducts += 1
        description = str(input("Description: "))
        price = Decimal(input("Price: "))
        cost = Decimal(input("Cost: "))

        p = Product(description, price, cost)
        products.append(p)
    if (opt == 2):
        print('')
        print('ID'.center(3, ' '),
              'Description'.center(30, ' '),
              'Price'.center(10, ' '),
              'Cost'.center(10, ' '),
              'Margin'.center(7, ' '))
        for p in products:
            print((str(p.productId).center(3, ' ')),
                  (p.description).center(30, ' '),
                  ("R$" + str(f"{p.price:.2f}")).center(10, ' '),
                  ("R$" + str(f"{p.cost:.2f}")).center(10, ' '),
                  (str(f"{p.calculateMargin():.2f}") + '%').center(7, ' '))
    if (opt == 3):
        print('')
        print('ID'.center(3, ' '),
              'Description'.center(30, ' '),
              'Price'.center(10, ' '),
              'Cost'.center(10, ' '))
        for p in products:
            print((str(p.productId).center(3, ' ')),
                  (p.description).center(30, ' '),
                  ("R$" + str(f"{p.price:.2f}")).center(10, ' '),
                  ("R$" + str(f"{p.cost:.2f}")).center(10, ' '))
    if (opt == 4):
        p = products[int(input('ID of the product: ')) - 1]
        p.setDescription(str(input('New description: ')))
        p.setPrice(Decimal(input('New price: ')))
        p.setCost(Decimal(input('New cost: ')))
    if (opt == 5):
        break
