fi = open("Input", "r")
fo = open("Output", "w")
lines = fi.readlines()
n = int(lines[0])
a_list = list(lines[1].split())
a_array = []
for e in a_list:
    a_array.append(int(e))
k = int(lines[2])
b_list = list(lines[3].split())
b_array = []
for e in b_list:
    b_array.append(int(e))


def binary_search(A, low, high, V):
    if high <= low:
        if V == A[low]:
            return fo.write(str(low)), fo.write(" ")
        else:
            return fo.write("-1"), fo.write(" ")
    mid = low + (high - low) // 2
    if V == A[mid]:
        return fo.write(str(mid)), fo.write(" ")
    elif V < A[mid]:
        return binary_search(A, low, mid - 1, V)
    else:
        return binary_search(A, mid + 1, high, V)


for i in b_array:
    binary_search(a_array, 0, n - 1, i)
    
fi.close()
fo.close()
