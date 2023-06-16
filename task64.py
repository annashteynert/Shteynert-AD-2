class Product:
    def __init__(self, name, cost, part):
        self.name = name
        self.cost = cost
        self.part = part

    def part(self, amount):
        if self.part - amount < 0:
            print("Ошибка")
        else:
            self.part -= amount

    def cost_1(self, cost1):
        if cost1 < 0:
            print("Ошибкай")
        else:
            self.cost=cost1

result1 = Product("яблоки", 400, 1)
result2 = Product("груши", 300, 1)
result3 = Product("виноград", 500, 1)

products = [result1, result2, result3]
products.sort(key=lambda x: x.cost)

for product in products:
    print(f"{product.name}: стоимость - {product.cost}, количество - {product.part}")
    product.part(2)
    product.cost_1(product.cost - 100)
    print(f"Новая стоимость: {product.cost}, новое количество: {product.part}")
    print()