""" 3*) Создайте класс, который имеет атрибут queue (допускается использование списка)
 который имеет метод add позволяющий добавлять в queue следующие объекты — целые числа, числа с плавающей запятой, строки. 
 При этом в момент добавления происходит валидация элементов по следующим правилам:
1. Целые числа — должны делится на 8, состоять из не более чем 4 символов
2. Числа с запятой — не более 3 символов после запятой
3. Строки — длина не более 4 символов без дублирования символов
В результате работы метода add элементы прошедшие валидацию добавляются в queuе, 
элементы не прошедшие валидацию  выводятся пользователю с сообщением о причине недобавления, например 
q=Queue()
q.add(1, 16, 280, 80000, 2.51, 1.875, text, data, world)
InvalidIntDivision → 1 # не делится на 8
InvalidIntNumberCount → 80000 # больше 4 символов
InvalidFloat → 1.875 # больше 2 символов после запятой
InvalidTextLength → world # больше 4 символов
DuplicatesInText → data # повторяющиеся символы
q.queue
 """
from dataclasses import dataclass

@dataclass
class InvalidIntDivision(Exception):
    x: int
    name: str = 'InvalidIntDivision'

    def __str__(self):
        return f'{self.name} -> {self.x}'

@dataclass
class InvalidIntNumberCount(Exception):
    x: int
    name: str = 'InvalidIntNumberCount'
    
    def __str__(self):
        return f'{self.name} -> {self.x}'

@dataclass
class InvalidFloat(Exception):
    x: float
    name: str = 'InvalidFloat'
    
    def __str__(self):
        return f'{self.name} -> {self.x}'

@dataclass
class InvalidTextLength(Exception):
    x: str
    name: str = 'InvalidTextLength'

    def __str__(self):
        return f'{self.name} -> {self.x}'

@dataclass
class DuplicatesInText(Exception):
    x: str
    name: str = 'DuplicatesInText'
    
    def __str__(self):
        return f'{self.name} -> {self.x}'


class Deque:
    def __init__(self):
        self.queue = []
        self.errors = []
    def add(self, *args):
        for x in args:
            if isinstance(x, int):
                if x % 8:
                    self.errors.append(InvalidIntDivision(x))
                if len(str(x)) > 4:
                    self.errors.append(InvalidIntNumberCount(x))
            if isinstance(x, float):
                number = str(x)
                i = number.find('.')
                number = number[i + 1:]
                if len(str(number)) > 3:
                    self.errors.append(InvalidFloat(x))
            if isinstance(x, str):
                str_1 = 0
                for val in x:
                    count = x.count(val)
                    str_1 = count
                if str_1 >= 2:
                    self.errors.append(DuplicatesInText(x))
                if len(x) > 4:
                    self.errors.append(InvalidTextLength(x))
        for error in self.errors:
            print(error)
        self.errors = []


q = Deque()
q.add(1, 16, 280, 1.82, "world", 1.8345, "text", 80000)
