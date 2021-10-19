fi = open("Input", "r")
fo = open("Output", "w")
lines = fi.readlines()
n = int(lines[0])
lst = list(lines[1].split())
array = []
for e in lst:
    array.append(int(e))


def merge(A, p, q, r):
    fo.write(str(p))
    fo.write(" ")
    fo.write(str(r))
    fo.write(" ")
    n1 = q - p + 1
    n2 = r - q
    L = list(range(n1 + 1))
    R = list(range(n2 + 1))
    for i in range(n1):
        L[i] = A[p + i - 1]
    for j in range(n2):
        R[j] = A[q + j]
    L[-1] = float("inf")
    R[-1] = float("inf")
    i, j = 0, 0
    for k in range(p-1, r):
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1
    fo.write(str(A[p-1]))
    fo.write(" ")
    fo.write(str(A[r-1]))
    fo.write("\n")


def merge_sort(A, p, r):
    if p < r:
        if ((p + r) // 2) % 2 == 0 or (p + r)//2 == p or (p + r)//2 == r:
            q = (p + r) // 2
        else:
            q = (p + r) // 2 + 1
        merge_sort(A, p, q)
        merge_sort(A, q+1, r)
        merge(A, p, q, r)
        return A


merge_sort(array, 1, n)
for e in array:
    fo.write(str(e))
    fo.write(" ")

fi.close()
fo.close()
