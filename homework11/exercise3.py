""" 3. Реализуйте класс DataObject который имеет обязательный атрибут data (произвольного типа данных)
Реализуйте класс очередь (Deque) с атрибутом класса deque в котором будут хранится элементы добавляемые в очередь, 
Класс Deque имеет методы 
- append_left для добавления элемента в начало очереди deque
- append_right для добавления элемента в конец очереди deque
(в данных методах необходимо реализовать возможность добавления в очередь только экземпляров класса DataObject
 (и его дочерних), а также проверку длины очереди — одновременно там может находится не более 5 элементов —
  в случае добавления 6 элемента добавление не производится и пользователю выдается сообщение о переполнении очереди). 
- pop_left — удаляет из очереди первый элемент слева и возвращает его
- pop_right - удаляет из очереди первый элемент справа и возвращает его
При реализации методов класса Deque воспользуйтесь методами класса (classmethod) """


from typing import Any
from dataclasses import dataclass

@dataclass
class DataObject:
    data: Any

d_1 = DataObject(input('Enter value: '))
d_2 = DataObject(input('Enter value: '))
d_3 = DataObject(input('Enter value: '))

class Deque:
    deque = []

    @classmethod
    def app_left(cls, object: Any):
        if not isinstance(object, DataObject):
            raise NotImplementedError
        cls.deque.insert(0, object.data)
        return cls.deque

    @classmethod
    def app_right(cls, object: Any):
        if not isinstance(object, DataObject):
            raise NotImplementedError
        cls.deque.append(object.data)
        return cls.deque

    @classmethod
    def pop_left(cls):
        return cls.deque.pop(0)
    
    @classmethod
    def pop_right(cls):
        return cls.deque.pop(-1)


print(Deque.app_left(d_1))
print(Deque.app_left(d_2))
print(Deque.app_right(d_3))
print(Deque.app_right(d_3))
print(Deque.app_left(d_1))
print(Deque.pop_left())
print(Deque.pop_right())