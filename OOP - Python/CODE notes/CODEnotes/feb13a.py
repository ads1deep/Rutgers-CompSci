def somefun(a, b):
    c = a + b
    b = c
    return b

def otherfun(L, M):
    K = M
    for i in L:
        K.append(i)
    return K
