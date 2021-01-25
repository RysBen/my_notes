def comp(x, t):
    return x * x > t

def binary_search(arr, target):
    l, r = 0, len(arr) - 1
    ret = -1
    while l <= r:
        m = (l+r) // 2
        if comp(arr[m], target):
            ret = m
            r = m -1
        else:
            l = m + 1
    return ret

def solve(arr, target):
    ret = binary_search(arr, target)
    if ret != -1:
        return arr[ret]
    else:
        return -1
