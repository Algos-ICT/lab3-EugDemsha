fi = open("Input", "r")
fo = open("Output", "w")
lines = fi.readlines()
n = int(lines[0])
lst = list(lines[1].split())
array = []
for e in lst:
    array.append(int(e))

def merge(A, p, q, r):
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


def merge_sort(A, p, r):
    if p < r:
        q = (p + r) // 2
        merge_sort(A, p, q)
        merge_sort(A, q+1, r)
        merge(A, p, q, r)
        return A


def merge_(A, p, q, r):
    print(A,p,q,r)
    n1 = q - p + 1
    n2 = r - q
    L = list(range(n1))
    R = list(range(n2))
    for i in range(n1):
        L[i] = A[p + i - 1]
    for j in range(n2):
        R[j] = A[q + j]
    print(L,R)
    i, j = 0, 0
    for k in range(p-1, r):
        if i < len(L) and j < len(R):
            if L[i] <= R[j]:
                A[k] = L[i]
                i += 1
            else:
                A[k] = R[j]
                j += 1
        elif i >= len(L):
            A[k] = R[j]
            j += 1
        elif j >= len(R):
            A[k] = L[i]
            i += 1


def merge_sort_(A, p, r):
    if p < r:
        q = (p + r) // 2
        merge_sort_(A, p, q)
        merge_sort_(A, q+1, r)
        merge_(A, p, q, r)
        return A


print(merge_sort_(array, 1, n))

merge_sort(array, 1, n)
for e in array:
    fo.write(str(e))
    fo.write(" ")

fi.close()
fo.close()