""" 2. Создать 2 класса Truck и Sedan, которые являются наследниками Auto. 
Класс Truck имеет дополнительный обязательный атрибут max_load.  метод drive, который перед появление сообщения «Car <brand> <mark> drives» выводит сообщение «Attention!». 
Реализовать дополнительный метод load. 
При его вызове происходит пауза в 1 секунду (используя модуль time), затем выводится сообщение «load», а затем снова происходит пауза в 1 секунду. 
Класс Sedan имеет дополнительный метод обязательный атрибут max_speed и при вызове метода drive, после появления сообщения «Car <brand> <mark> drives», 
выводит сообщение «max speed of sedan <brand> <mark> is <max_speed>». 
Инициализировать по 2 отдельных объекта этих классов, проверить работы их методов и атрибутов (вызвать методы, атрибуты вывести в печать) """


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


class Truck(Auto):
    def __init__(self, brand, age, mark, max_load):
        super().__init__(self, brand, age, mark, max_load)
    
    def drive(self):
        print(f'Attention!', 'Car {self.brand} {self.mark} drives', sep = '\n')
    def load(self):
        



class Sedan(Auto):
