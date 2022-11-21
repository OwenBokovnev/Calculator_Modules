import calc_complex as compl
import calc_ratio as ratio
import logger as log

choice = int(input('Калькулятор для вычисления РАЦИОНАЛЬНЫХ (1) и КОМПЛЕКСНЫХ (2) чисел\nС чего начнем? '))

if choice == 1:
    ratio.calc_ratio()
else:
    compl.calc_complex()

def complex():
    data = compl.calc_complex()
    log.complex_logger(data)
    return data

def ratio():
    data = ratio.calc_ratio()
    log.ratio_logger(data)
    return data
