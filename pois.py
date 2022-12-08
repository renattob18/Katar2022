import numpy as np

kolvo = 10

def pois(lam, n):
    a = []
    s = np.e ** (-lam)
    for i in range(1, n + 1):
        a.append(s)
        s = s * lam / i
    return np.array(a)

def f(x, y):
    x1 = pois(x, kolvo)
    y1 = pois(y, kolvo)
    a = np.outer(x1, y1)
    r1 = np.sum(np.triu(a.T, k=1))
    r3 = np.sum(np.triu(a, k=1))
    r2 = 1 - r1 - r3
    return (r1, r2, r3)

print(f(1, 2))
