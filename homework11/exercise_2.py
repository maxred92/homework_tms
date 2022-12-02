""" Реализуйте класс который представляет собой универсальный интерфейс 
по представлению температуры в шкалах Цельсия/Кельвина/Фаренгейта 
и поддерживает конвертацию значений температуры между этими шкалами  """


class Temperature:
    def __init__(self):
        self.__value = 0
    
    @property
    def celsius(self):
        return self.__value - 273.15

    @property
    def kelvin(self):
       return self.__value

    @property
    def fahrenheit(self):
        return (self.__value - 273.15) * 9 / 5 + 32

    @celsius.setter
    def celsius(self, val):
        self.__value = val + 273.15

    @kelvin.setter
    def kelvin(self, val):
        self.__value = val

    @fahrenheit.setter
    def fahrenheit(self, val):
        self.__value = ((val - 32) * 5 / 9) + 273.15

t = Temperature()

t.celsius = 0
print(t.kelvin)
print(t.fahrenheit)
