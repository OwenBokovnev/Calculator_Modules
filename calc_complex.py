

def calc_complex():
    a = input('Нужна ли справка по комплексным числам? y/n: ')
    if a == 'y':
        try:
            load()
        except:
            print('Справка отсутствует.')
    x = complex(input('Введите ПЕРВОЕ комплексное число: '))
    y = complex(input('Введите ВТОРОЕ комплексное число: '))
    act = input ('Что с ними нужно сделать?\nДопускается (+, -, *, /): ')

    if act == '+':
        res_complex = print(f'Результат равен: {x + y}')
    elif act == '*':
        res_complex = print(f'Результат равен: {x * y}')
    elif act == '/':
        res_complex = print(f'Результат равен: {x / y}')
    elif act == '-':
        res_complex = print(f'Результат равен: {x - y}')

    return res_complex

def load():
    with open("Desc.csv", "r") as file:
        for line in file:
            print(line, end="")