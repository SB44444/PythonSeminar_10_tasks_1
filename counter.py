import sys

def count(my_st):  # Ф-ция калькулятора
    my_st = str(my_st)  # Входные данные привоятся к строке
    lst = ''
    for i in my_st:     # Проходом по строке 
        if i.isdigit() or i == '.': lst += i  # Цифры с точкой групптруются
        if i in '/*-+': lst += f' {i} '       # Знаки добавляются с пробелами с обоих сторон
    lst = lst.split()                         # Строка сплитуется в список по пробелам 
    if lst[0] == '-': lst.insert(0, '0')      # Если первый знак '-' в начало списка втавляем 0, чтобы не нарушались вычисления с минусом 
    
    while '/' in lst:                  # Болок вычислений, почти как в предыдущих заданиях 
        ind = lst.index('/')
        if float(lst[ind + 1]) == 0:
            break # ("Ошибка! Делить на ноль нельзя") Выводится результат вычисления выражения до /0
        res = float(lst[ind - 1]) / float(lst[ind + 1])
        del lst[(ind - 1) : (ind + 2)]
        lst.insert(ind -1, res)
    while '*' in lst:
        ind = lst.index('*')
        res = float(lst[ind - 1]) * float(lst[ind + 1])
        del lst[(ind - 1) : (ind + 2)]
        lst.insert(ind -1, res)
    while '-' in lst:
        ind = lst.index('-')
        res = float(lst[ind - 1]) - float(lst[ind + 1])
        del lst[(ind - 1) : (ind + 2)]
        lst.insert(ind -1, res)
    while '+' in lst:
        ind = lst.index('+')
        res = float(lst[ind - 1]) + float(lst[ind + 1])
        del lst[(ind - 1) : (ind + 2)]
        lst.insert(ind -1, res)
    result = round(float(lst[0]), 4)     # Результат округляем до 4-х знаков
    
    return result
