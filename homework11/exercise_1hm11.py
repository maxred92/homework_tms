""" 1. Реализуйте класс Блюдо, описывающее количество, название, стоимость и массу блюда.
Далее создайте несколько инстансов этого класса с описанием блюд.
Реализуйте класс Заказ, в инстанс которого можно было бы добавлять блюда. 
Заказ должен содержать вычисляемые свойства: количество, стоимость, масса блюд в заказе.
Также реализуйте дополнительный метод "оплатить" (внесение определенной суммы в счет оплаты заказа) 
и дополнительное свойство, обозначающее сумму, которую осталось оплатить 
(с учетом стоимости заказа и внесенных с помощью метода «оплатить» денег)
 """

class Menu:
    def __init__(self, name: str, price: int):
        self.name = name
        self.price = price

    def info(self):
        return f'{self.name} {str(self.price)}: $'

    def get_total(self, count: int):
        total_price = self.price * count
        return round(total_price)
    
class Food(Menu):
    def __init__(self, name: str, price: int, weight: int):
        super().__init__(name,price)
        self.weight = weight
    
    def info(self):
        return f'{self.name}: {str(self.price)}$({str(self.weight)}gr)'
    
    def calorie_info(self):
        print(f'gr:{str(self.weight)}')


class Drink(Menu):
    def __init__(self, name: str, price: int, weight: int):
        super().__init__(name, price)
        self.weight = weight
    
    def info(self):
        return f'{self.name}: {str(self.price)}$({str(self.weight)}ml)'

class Order:
    def pay(self, money: int):
        self.money = money
        self.total = result - self.money
        if self.total > 0:
            print(f'Are you greedy :(, Pay more  {self.total}$')
        else:
            print(f'Your change - {abs(self.total)}$\nHave a nice day!:)')

print('Hello! Welcome to our cafe:')

f1 = Food('Burger', 7, 500)
f2 = Food('Nachos', 8, 300)
f3 = Food('Pizza', 9, 600)
f4 = Food('French frieds', 2, 150)
f5 = Food('Cheescake', 3, 170)

foods = [f1, f2, f3, f4, f5]

d1 = Drink('Beer', 3, 330)
d2 = Drink('Cola', 2, 250)
d3 = Drink('Espresso', 1, 30)
d4 = Drink('Juice', 2, 200)
d5 = Drink('Mojito', 7, 450)

drinks = [d1, d2, d3, d4,d5]

print('Food:')
index = 0
for food in foods:
    print(f'{str(index)}.{food.info()}')
    index += 1

print('Drinks:')
index = 0
for drink in drinks:
    print(f'{str(index)}.{drink.info()}')
    index += 1

print('--------------------')

food_order = int(input('Enter food item number: '))

drink_order = int(input('Enter drink item number: '))

count=int(input('How many meals would you like to purchase?: '))

result = foods[food_order].get_total(count)+drinks[drink_order].get_total(count)

print(f'Your total is {str(result)}$')

m1 = Order()
m1.pay(int(input('How much do you want to deposit: ')))
