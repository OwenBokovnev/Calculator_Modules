from datetime import datetime as dt


def complex_logger(data):
    time = dt.now().strftime('%H:%M')
    with open ('calc_log.csv', 'a') as file:
        file.write('{};calc_complex;{}\n'
                    .format(time, data))

def ratio_logger(data):
    time = dt.now().strftime('%H:%M')
    with open ('calc_log.csv', 'a') as file:
        file.write('{};calc_ratio;{}\n'
                    .format(time, data))


