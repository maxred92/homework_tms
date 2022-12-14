""" 5*. Реализуйте генератор, который будет бесконечно генерировать числа Фибоначчи
 (https://en.wikipedia.org/wiki/Fibonacci_number). """



import time # импортировал для того, чтобы была возмоность успеть посмотреть цикл:)

def generate_fibonacci(pause):
    num_1 = 0
    num_2 = 1
    while True:
        yield num_2
        time.sleep(pause)
        num_1, num_2 = num_2, num_1 + num_2


gen = generate_fibonacci(1)
while True:
    print(next(gen))
