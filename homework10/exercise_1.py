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
        print(car_1.age, car_2.age, sep='\n')


car_1 = Auto("Toyota", 2015, "RAV4")
car_1.drive()
car_2 = Auto("Honda", 2020, "CR-V")
car_2.stop()
car_1.use()
