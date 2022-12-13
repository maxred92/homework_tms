""" 1. Создайте генераторную функцию которая в качестве аргумента принимать путь к файлу «unsorted_names.txt» 
и букву английского алфавита, 
открывает файл по данному пути и генерирует последовательность 
из имен начинающихся на указанную букву
names_with_letter = names_gen(«unsorted_names.txt», «A»)
next(names_with_letter)
Amelia
next(names_with_letter)
Adrienne
или
for name in names_with_letter:
	print(i, end=““)
Amelia
Adrienne """



def names_with_letter(file_txt, letter):
      
    with open('unsorted_names.txt', 'r') as file:
        names_gen = file.readlines()
        for i in names_gen:
            if i.startswith(letter):
                yield i

letter = 'A'
file_txt = 'unsorted_names.txt'
for name in names_with_letter(file_txt, letter):
    print(name, end = '')

