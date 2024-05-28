from math import sin, cos, log    #Импорт математических функций

def one_function(dot):    #Вычисление функций
    base = abs(2 / 10) + 2

    if sin(dot + 2) != 0:
        arg = (1 - 2) / sin(dot + 2)
    else:
        return None

    if base <= 0 or base == 1 or arg <= 0:    #Проверка вычислений
        return None
    return log(arg, base)

def two_function(dot):
    if cos(dot) != 0:
        return abs(cos(dot) / 2)
    else:
        return None
def FindMax(num1, num2):    #Вычисление максимума
    try:
        return max(num1, num2)
    except:
        if num1 == None:
            return num2
        else:
            return num1

print('Введите значения начала диапазона X')
while True:
    try:
        x_start = float(input())
        break
    except:
        print('Ошибка! Введено неправильное значение (возможно текст), повторите ввод')
x = x_start

print('Введите конечное значение диапазона X')
while True:
    try:
        x_end = float(input())   #Проверка правильности ввода конечного значения диапазона
        while x_start >= x_end:    #Проверка правильности ввода первого и последнего значения
            print('Ошибка! Последнее значение диапазона не может быть меньше начального, '
                  'либо равно ему, повторите ввод')
            x_end = float(input())
        break
    except:
        print('Ошибка! Введено неправильное значение (возможно текст), повторите ввод')

print('Введите значение шага (deltaX)')
while True:
    try:
        delta_x = float(input())
        while delta_x <= 0:
             print('Ошибка! Шаг изменения переменной равен 0, либо меньше 0, введите значение заново')
             delta_x = float(input())
        break
    except:
        print('Ошибка, Введено неправильное значение (возможно текст), повторите ввод')
print('_'*63)
print('|','Значение Х',' ' * 8,'|' ' Максимальное значение', ' ' * 15, '|') #Шапка таблицы
print('-'*63)

while round(x,6) <= round(x_end,6):
    max_function = FindMax(one_function(x),two_function(x))
    print('|х = ', '%15.6f' % x, '| максимальное значение = ','%10.6f' % max_function, '  |')
    x += delta_x
print('-'*63)