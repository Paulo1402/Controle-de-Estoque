def decorator1(func):
    print('decorator1', func.__name__)

    def inner(*args, **kwargs):
        func(*args, **kwargs)

    return inner


def decorator2(func):
    print('decorator2', func.__name__)

    def inner(*args, **kwargs):
        func(*args, **kwargs)

    return inner


@decorator1
@decorator2
def foo():
    print('foo')


foo()