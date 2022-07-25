from datetime import datetime
import requests

PATH ="decorator_logs.txt"

def path(path):
    def decorator(func):
        def inner(*args, **kwargs):
            date = datetime.now()
            with open(path, "w") as file:
                file.write(f'Запускается {func.__name__}\nДата и время запуска: {date}\nВызвана с аргументами {args, kwargs}\nBозвращаемое значение {inner}')
            #print(f"Запускается '{func.__name__}'. Дата и время запуска: {date}")  При вызове функции несколько раз выглядит плохо
            return func(*args)
        return inner
    return decorator

@path(PATH)
def summator(x, y):
   return x + y

three = summator(1, 2)
five = summator(2, 3)

result = summator(three, five)

print('result: ', result)
print('result type: ', type(result))