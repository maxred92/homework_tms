""" 1) Создайте интерактивный калькулятор.
Пользовательский ввод представляет собой формулу, состоящую из числа, оператора (+,-,*,/,**) и другого числа, разделенных пробелом (например, 1 + 1). 
Проверьте input по следующим правилам:
1. Если входные данные не состоят из 3 действительных элементов, вызовите InputFormulaError, которая является пользовательским исключением.
2. Если первый и третий элемент не являются действительными числами — выводится ошибка InputNumberError.
3. Если второй элемент не соответствует поддерживаемым операторам — выводится ошибка InputOperatorError.
Если ввод верен, выполните вычисление и выведите результат (в случае возникновения ошибки при вычислении — также выводим ее). 
Затем пользователю предлагается ввести новый ввод и так далее, пока пользователь не введет quit.

Взаимодействие может выглядеть так:
1 + 1
2.0
3,2 - 1,5
1.70
quit """

import math

def num_input(prompt_str):
    while True:
        try:
            num = float(input(prompt_str))
        except ValueError:
            print("Please enter a numeric value: ")
            continue
        else:
            break

    return num

def calculate(operator, operand1, operand2):

    if operator == "+":
        result = operand1 + operand2
    elif operator == "-":
        result = operand1 - operand2
    elif operator == "*":
        result = operand1 * operand2
    elif operator == "/":
        try:
            result = operand1 / operand2
        except ZeroDivisionError:
            result = "Cannot divide by 0"         
    elif operator == "**":
        result = math.pow(operand1, operand2)
    return result


def main():

    operation = ['+', '-', '*', '/', '**']

    print("=========Simple Calculator========")
    print("The following operations are available: ")
    print(operation)

    while True:
        op = input("What operation would you like to perform? ")
        if op not in operation:
            print("This operation is not recognized by the calculator. Pleas try again.")
            continue
        else:
            number1 = num_input("enter the first number: ")
            number2 = num_input("enter the second number: ")
            result = calculate(op, number1, number2)
            print(result)

main()


