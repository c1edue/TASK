import numpy as np
def square(side):
    print('----------------------')
    print(f'[+]perimeter: {side+side+side+side}')
    print(f'[+]square: {side**2}')
    print(f'[+]diagonal: {np.sqrt(side**2+side**2)}')

while True:
    try:
        side = int(input('type side of square: '))
        square(side)
    except Exception as e:
        print('----------------------')
        print(e)
