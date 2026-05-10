#Лаба8_в11
#найти строку с наибольшим ср арифм
#Переставить местами строки с наибольшим и наименьшим количеством 
#отрицательных элементов. 
#Найти столбец, имеющий наибольшее количество простых чисел.
#Переставить местами столбцы с максимальной и минимальной суммой 
#элементов. 
#Найти максимальное значение в квадратной матрице над главной диагональю и 
#минимальное - под побочной диагональю. 
#Выполнить транспонирование квадратной матрицы. 
is_correct_n = False
numbers = '0123456789'
while is_correct_n == False:
    n = input('Введите количество столбцов матрицы: ')
    is_correct_n = True
    if len(n) == 0:
        is_correct_n = False
    for i in range(len(n)):
        if n[i] not in numbers:
            is_correct_n = False
    if is_correct_n == True:
        n = int(n)
        if n <= 0:
            is_correct_n = False
column = n
is_correct_m = False
while is_correct_m == False:
    m = input('Введите количество строк матрицы: ')
    if_correct_m = True
    if len(m) == 0:
        is_correct_m = False
    for i in range(len(m)):
        if m[i] not in numbers:
            is_correct_m = False
    if is_correct_m == True:
        m = int(m)
        if m <= 0:
            is_correct_m = False
line = m