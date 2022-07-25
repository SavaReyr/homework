from datetime import datetime

def decorator(func):
    def inner(*args, **kwargs):
        date = datetime.now()
        with open("log_file.txt", "w") as file:
            file.write(f'Запускается {func.__name__}\nДата и время запуска: {date}\nВызвана с аргументами {args, kwargs}\nBозвращаемое значение {inner}')
        print(f"Запускается '{func.__name__}'. Дата и время запуска: {date}")
        func(args)

    return inner


@decorator
def test(arg):
    x = int(input("Input your number:"))
    if x == 1:
        print("ok")
    else:
        print("not ok)")

test()
