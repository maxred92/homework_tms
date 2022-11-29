""" 1. Создать родительский класс Auto, у которого есть атрибуты: brand, age, color, mark и weight. 
В классе должны быть реализованы следующие методы — drive, use и stop. 
Методы drive и stop выводят сообщение «Car <brand> <mark> drives / stops». Метод use увеличивает атрибут 
age на 1 год. Атрибуты brand, age и mark необходимо инициализировать при объявлении объекта """


class Auto():

    color = "red"
    weight = 1900

    def __init__(self, brand, age, mark):
        self.brand = brand
        self.age = age
        self.mark = mark

    def drive(self):
        print(f"Car {self.brand} {self.mark} drives")

    def stop(self):
        print(f"Car {self.brand} {self.mark} stops")

    def use(self):
        self.age += 1
        print(auto_1.age, auto_2.age, sep='\n')


auto_1 = Auto("Toyota", 2015, "RAV4")
auto_1.drive()
auto_2 = Auto("Honda", 2020, "CR-V")
auto_2.stop()
auto_1.use()
