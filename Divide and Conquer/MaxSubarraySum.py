def max_crossing_sum(arr, left, right, mid):
    s = 0
    left_sum = float("-inf")
    
    for i in range(mid, left - 1, -1):
        s += arr[i]
        left_sum = max(left_sum, s)

    s = 0
    right_sum = float("-inf")

    for i in range(mid + 1, right + 1):
        s += arr[i]
        right_sum = max(right_sum, s)

    return left_sum + right_sum

def max_subarray_sum(arr, left, right):
    if left == right:
        return arr[left]

    mid = (left + right) // 2

    left_sum = max_subarray_sum(arr, left, mid)
    right_sum = max_subarray_sum(arr, mid + 1, right)
    crossing_sum = max_crossing_sum(arr, left, right, mid)

    return max(left_sum, right_sum, crossing_sum)

arr = [-1, -2, 3, 4, 5, -1, 4, 3]
print(max_subarray_sum(arr, 0, len(arr) - 1))

