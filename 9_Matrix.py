fi = open("Input", "r")
fo = open("Output", "w")
lines = fi.readlines()
n = int(lines[0])
matrix_1 = []
matrix_2 = []
for a in range(1, n+1):
    f = lines[a].split()
    b = []
    for e in f:
        b.append(int(e))
    row_1 = []
    row_2 = []
    for c in enumerate(b):
        if c[0] < n:
            row_1.append(c[1])
        else:
            row_2.append(c[1])
    matrix_1.append(row_1)
    matrix_2.append(row_2)


def matrix_multiply(x, y):
    z = []
    for d in range(n):
        z.append(list(range(n)))
    for i in range(n):
        for j in range(n):
            z[i][j] = 0
            for k in range(n):
                z[i][j] = z[i][j] + x[i][k]*y[k][j]
    return z


print(matrix_multiply(matrix_1,matrix_2))


import math


def decimal(s):
    return int(s) if s.is_integer() else s


def two_exp(matrix):
    if type(decimal(math.log2(len(matrix)))) != int:
        for f in matrix:
            f.append(0)
        matrix.append([0] * (len(matrix) + 1))
        two_exp(matrix)
    else:
        return matrix


def breakdown(matrix):
    a = []
    for i in range(len(matrix) // 2):
        inner = []
        for j in range(len(matrix[i]) // 2):
            inner.append(matrix[i][j])
        a.append(inner)
    b = []
    for i in range(len(matrix) // 2):
        inner = []
        for j in range(len(matrix[i]) // 2, len(matrix)):
            inner.append(matrix[i][j])
        b.append(inner)
    c = []
    for i in range(len(matrix) // 2, len(matrix)):
        inner = []
        for j in range(len(matrix[i]) // 2):
            inner.append(matrix[i][j])
        c.append(inner)
    d = []
    for i in range(len(matrix) // 2, len(matrix)):
        inner = []
        for j in range(len(matrix[i]) // 2, len(matrix)):
            inner.append(matrix[i][j])
        d.append(inner)
    return a, b, c, d


def minus(x, y):
    z = []
    for d in range(len(x)):
        z.append(list(range(len(x))))
    for i in range(len(x)):
        for j in range(len(x)):
            z[i][j] = x[i][j] - y[i][j]
    return z


def plus(x, y):
    z = []
    for d in range(len(x)):
        z.append(list(range(len(x))))
    for i in range(len(x)):
        for j in range(len(x)):
            z[i][j] = x[i][j] + y[i][j]
    return z


def no_zeros(matrix):
    while n < len(matrix):
        for f in matrix:
            f.pop(-1)
        matrix.pop(-1)
    else:
        return matrix


def strassen(x, y):
    two_exp(x)
    two_exp(y)
    if len(x) <= 2:
        a, b, c, d = x[0][0], x[0][1], x[1][0], x[1][1]
        e, f, g, h = y[0][0], y[0][1], y[1][0], y[1][1]
        p1 = a * (f - h)
        p2 = (a + b) * h
        p3 = (c + d) * e
        p4 = d * (g - e)
        p5 = (a + d) * (e + h)
        p6 = (b - d) * (g + h)
        p7 = (a - c) * (e + f)
        z = []
        for p in range(len(x)):
            z.append(list(range(len(x))))
        z[0][0] = p5 + p4 - p2 + p6
        z[0][1] = p1 + p2
        z[1][0] = p3 + p4
        z[1][1]= p1 + p5 - p3 - p7
    else:
        a,b,c,d = breakdown(x)
        e,f,g,h = breakdown(y)
        p1 = strassen(a, minus(f, h))
        p2 = strassen(plus(a, b), h)
        p3 = strassen(plus(c, d), e)
        p4 = strassen(d, minus(g, e))
        p5 = strassen(plus(a, d), plus(e, h))
        p6 = strassen(minus(b, d), plus(g, h))
        p7 = strassen(minus(a, c), plus(e, f))
        z1 = minus(plus(p5, p4),minus(p2, p6))
        z2 = plus(p1, p2)
        z3 = plus(p3, p4)
        z4 = minus(plus(p1, p5),plus(p3, p7))
        z = []
        for p in range(len(x)):
            z.append(list(range(len(x))))
        for i in range(len(z) // 2):
            for j in range(len(z[i]) // 2):
                z[i][j] = z1[i][j]
        for i in range(len(z) // 2):
            for j in range(len(z[i]) // 2, len(z)):
                z[i][j] = z2[i][j - len(z[1]) // 2]
        for i in range(len(z) // 2, len(z)):
            for j in range(len(z[i]) // 2):
                z[i][j] = z3[i - len(z) // 2][j]
        for i in range(len(z) // 2, len(z)):
            for j in range(len(z[i]) // 2, len(z)):
                z[i][j] = z4[i - len(z) // 2][j - len(z) // 2]
        no_zeros(z)
    return z


for i in strassen(matrix_1, matrix_2):
    for j in i:
        fo.write(str(j))
        fo.write(" ")
    fo.write("\n")

fi.close()
fo.close()