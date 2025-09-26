from datetime import datetime as dt

def checktime(func):
    def wrapper(*args, **kwargs):
        time_now = dt.now()
        h = time_now.hour
        m = time_now.minute
        s = time_now.second
        d = time_now.day
        mo = time_now.month
        y = time_now.year
        print(f'функция была вызвана в {h}:{m}:{s} {d}/{mo}/{y}')
        result = func(*args, **kwargs)
        print(func.__name__)
        return result
    return wrapper


@checktime
def hello_world():
    print('hello world')


hello_world()
