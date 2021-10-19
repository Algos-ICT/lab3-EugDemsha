fi = open("TeslaStocks", "r")
fo = open("Output", "w")
lines = fi.readlines()
company = lines[0]
dates = lines[1]
array = []
d_array = []
for a in range(2, len(lines)):
    date, price = lines[a].split()
    array.append(float(price))
    d_array.append(str(date))
n = len(array)


def find_max_crossing_subarray(A, low, mid, high):
    leftsum = float("-inf")
    sum = 0
    maxleft = mid
    for i in range(mid, low - 1, -1):
        sum += A[i]
        if sum > leftsum:
            leftsum = sum
            maxleft = i
    rightsum = float("-inf")
    sum = 0
    maxright = mid
    for j in range(mid + 1, high + 1):
        sum += A[j]
        if sum > rightsum:
            rightsum = sum
            maxright = j
    return maxleft, maxright, leftsum + rightsum


def find_maximum_subarray(A, low, high):
    if high == low:
        return low, high, A[low]
    else:
        mid = (low + high) // 2
        leftlow, lefthigh, leftsum = find_maximum_subarray(A, low, mid)
        rightlow, righthigh, rightsum = find_maximum_subarray(A, mid + 1, high)
        crosslow, crosshigh, crosssum = find_max_crossing_subarray(A, low, mid, high)
        if leftsum >= rightsum and leftsum >= crosssum:
            return leftlow, lefthigh, leftsum
        elif rightsum >= leftsum and rightsum >= crosssum:
            return rightlow, righthigh, rightsum
        else:
            return crosslow, crosshigh, crosssum


start, finish, summ = find_maximum_subarray(array, 0, n-2)

fo.write(str(company))
fo.write(str(dates))
fo.write(str(d_array[start]))
fo.write(" ")
fo.write(str(d_array[finish]))
fo.write(" ")
fo.write(str(summ))

fi.close()
fo.close()
