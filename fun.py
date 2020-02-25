
def func1(x):
    if x == 2:
        return True
    else:
        return False

def func2(x):
    if x == 3:
        return True
    else:
        return False


def compose(f,g):
    return lambda x:f(g(x))



h = compose(func1,func2)

print(h(3))