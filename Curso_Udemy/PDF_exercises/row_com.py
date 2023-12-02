def repeat(f):
    f()
    f()
    f()
    f()


def plus_symbol():
    print('+ ', end=' ')


def minus_symbol():
    print('- ', end=' ')


def bar_symbol():
    print('| ', end='')


def line():
    plus_symbol()
    repeat(minus_symbol)
    plus_symbol()
    repeat(minus_symbol)
    plus_symbol()
    print()


def bars():
    bar_symbol()
    print('             ', end='')
    bar_symbol()
    print('             ', end='')
    bar_symbol()
    print()


def shape():
    line()
    repeat(bars)
    line()
    repeat(bars)
    line()


shape()


"""
def do_twice(f, x):
    f(x)
    f(x)


def print_spam():
    print('spam')


def print_twice(oi):
    print(oi)
    print(oi)


do_twice(print_twice, 'spam')

x = '+  -  -  -  -  +'  16
y = '              '  14

print(len(y))


# def repeat_numb(f, x):
#     f(x)

"""
