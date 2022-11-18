# import cmath, math, numpy

def calc_complex():
    x = complex(input('Введите ПЕРВОЕ комплексное число: '))
    y = complex(input('Введите ВТОРОЕ комплексное число: '))
    act = input ('Что с ними нужно сделать?\nДопускается (+, -, *, /): ')

    if act == '+':
        res_complex = x + y
    elif act == '*':
        res_complex = x * y
    elif act == '/':
        res_complex = x / y
    elif act == '-':
        res_complex = x - y
    # elif act == 'sqrt':
    #     res_complex = cmath.sqrt(x)
    return res_complex

