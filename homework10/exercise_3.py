""" 3. Реализуйте класс Counter, который дополнительно принимает начальное значение и конечное значение счетчика. Если начальное значение не указано, счетчик должен начинаться с 0.
Если стоп-значение не указано, оно должно считаться вверх бесконечно. Если счетчик достигает стоп-значения, выведите «Maximal value is reached».
Реализовать методы: "increment" (увеличивает счетчик на 1) и "get" (выводит информацию о значении счетчика)
Пример:
c = Counter(start=42)
c.increment()
c.get()
43

c = Counter()
c.increment()
c.get()
1
c.increment()
c.get()
2

c = Counter(start=42, stop=43)
c.increment()
c.get()
43
c.increment()
Maximal value is reached.
c.get()
43
 """


class Counter():

    def __init__(self, start : int = 0, stop : int = -1):
        self.start = start
        self.stop = stop

    def increment(self):
        self.start += 1
        if self.start == self.stop:
            print("Maximal value is reached")

    def get(self):
        print(self.start)


c = Counter(start = 42)
c.increment()
c.get()

c = Counter()
c.increment()
c.get()
c.increment()
c.get()

c = Counter(start = 42, stop = 43)
c.increment()
c.get()
