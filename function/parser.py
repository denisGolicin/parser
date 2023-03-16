import pandas as pd
from function import debug

file = pd.read_excel('file.xlsx')

def parser(i):
    result = file.values[i]
    result = str(file.values[i]).replace('[', '+').replace(']', '')

    if result[1] != "7" or len(result) > 12:

        debug.message("Некорректный номер: " + result)
        return False

    debug.save(i)
    return result

def getValue():
    return len(file.values)