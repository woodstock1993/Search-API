def say_hello(func):                    # 1
    def wrapper2(*args, **kwargs):      # 8
        print('Hello')                  # 11
        return func(*args, **kwargs)    # 12
    return wrapper2                     # 9


def say_hi(func):                       # 2
    def wrapper1(*args, **kwargs):      # 5
        print('Hi')                     # 13
        return func(*args, **kwargs)    # 14
    return wrapper1                     # 6


@say_hello                              # 7
@say_hi                                 # 4
def introduce(name):                    # 3
    print(f'My name is {name}!')        # 15


def decorator2(func):  # 받은 func의 이름을 출력하면서 데코레이터가 적용되었다는 메세지를 출력
    def wrapper2(*args, **kwargs):
        print(f'{func.__name__} has been decorated again by decorator2')
        return func(*args, **kwargs)
    return wrapper2


def decorator1(func):  # 받은 func의 이름을 출력하면서 데코레이터가 '또' 적용되었다는 메세지를 출력
    def wrapper1(*args, **kwargs):
        print(f'{func.__name__} has been decorated by decorator1')
        return func(*args, **kwargs)
    return wrapper1


@decorator2
@decorator1
def function():  # 데코레이터를 적용할 함수
    print(f'This is original function')


function()