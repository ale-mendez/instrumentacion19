
def fun(x):
    if x == 0:
        raise ValueError('x must be != 0')
    return 1/x

def external(N):
    for n in range(N):
        try:
            fun(n)
        except:
            ValueError:
            print('Error')
