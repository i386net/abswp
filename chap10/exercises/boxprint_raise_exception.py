def boxprint(symbol, width, height):
    if len(symbol) != 1:
        raise Exception('Var symbol should be 1 symbol string')
    if width <= 2:
        raise Exception('Width should be not more than 2')
    if height <= 2:
        raise Exception('Height should be not more than 2')
    print(symbol * width)
    for i in range(height -2):
        print(symbol + (' ' * (width - 2)) + symbol)
    print(symbol * width)


for sym, w, h in (('*', 4, 4), ('O', 20, 5), ('x', 1, 3), ('zz', 3, 3)):
    try:
        boxprint(sym, w, h)
    except Exception as err:
        print('Exception raised: ', err)
