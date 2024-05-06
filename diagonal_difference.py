#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

arr = [[11, 2, 4], [4, 5, 6], [10, 8, -12]]

def diagonalDifference(arr):
    d1 = d2 = 0
    arr_len = len(arr)
    
    for i in range(0, arr_len):
        d1 += arr[i][i]
        d2 += arr[i][arr_len - i - 1]
    return abs(d1 - d2)

print(diagonalDifference(arr))

