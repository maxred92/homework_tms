""" 2. Создать 2 класса Truck и Sedan, которые являются наследниками Auto. 
Класс Truck имеет дополнительный обязательный атрибут max_load.  метод drive, который перед появление сообщения «Car <brand> <mark> drives» выводит сообщение «Attention!». 
Реализовать дополнительный метод load. 
При его вызове происходит пауза в 1 секунду (используя модуль time), затем выводится сообщение «load», а затем снова происходит пауза в 1 секунду. 
Класс Sedan имеет дополнительный метод обязательный атрибут max_speed и при вызове метода drive, после появления сообщения «Car <brand> <mark> drives», 
выводит сообщение «max speed of sedan <brand> <mark> is <max_speed>». 
Инициализировать по 2 отдельных объекта этих классов, проверить работы их методов и атрибутов (вызвать методы, атрибуты вывести в печать) """

from time import sleep

class Auto():

    color = "red"
    weight = 1900
    
    max_speed = 320

    def __init__(self, brand : str, age : int, mark : str):
        self.brand = brand
        self.age = age
        self.mark = mark

    def drive(self):
        print(f"Car {self.brand} {self.mark} drives")

    def stop(self):
        print(f"Car {self.brand} {self.mark} stops")

    def use(self):
        self.age += 1
        return self.age

class Truck(Auto):
    
    def __init__(self, brand : str, age : int, mark : str, max_load : float):
        super().__init__(brand, age, mark)
        self.max_load = max_load
        
    def drive(self):
        print('Attention!')
        return super().drive()
    
    def load(self):
        sleep(1)
        print('Loading')
        sleep(1)

class Sedan(Auto):
    
    def __init__(self, brand : str, age : int, mark : str, max_speed : float):
        super().__init__(brand, age, mark)
        self.max_speed = max_speed 
    
    def drive(self):
        print(f"Max speed of sedan {self.brand} {self.mark} is {self.max_speed}")
        return super().drive()


auto_1 = Truck("Toyota", 2015, "RAV4", 1600)
auto_2 = Sedan("Honda", 2020, "CR-V", 320)
auto_1.drive()
auto_1.load()
auto_1.stop()
auto_2.drive()
print(auto_1.max_load)