
def calc_ratio():
    m = int(input('Для проведения операций с рациональными числами:\nВведите ПЕРВОЕ число "m": '))
    n = int(input('Введите ВТОРОЕ число "n": '))
    a = str(input(f'Какое действие вы хотите совершити с этими числами "{m}" и "{n}"?\nДопускается (+, -, /, *): '))
    if a == '-':
        res_ratio = print(f'Результат равен: {m - n}')
    elif a == '+':
        res_ratio = print(f'Результат равен: {m + n}')
    elif a == '/':
        res_ratio = print(f'Результат равен: {m / n}')
    elif a == '*':
        res_ratio = print(f'Результат равен: {m * n}')
    return res_ratio

