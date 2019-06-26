
def boo(arr):
    """冒泡"""
    for i in range(1, len(arr)):
        for j in range(0, len(arr)-i):
            if arr[j+1] < arr[j]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr


def sel(arr):
    """选择排序"""
    for i in range(len(arr)-1):
        index = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[index]:
                index = j
        if i != index:
            arr[i], arr[index] = arr[index], arr[i]
    return arr


def fast(arr):
    """快速排序"""
    if arr:
        mid = arr[0]
        left = [l for l in arr[1:] if l < mid]
        right = [r for r in arr[1:] if r > mid]
        return left + [mid] + right
    else:
        return []


def insert(arr):
    """插入排序"""
    for i in range(1, len(arr)):
        for j in range(i, 0, -1):
            if arr[j] < arr[j-1]:
                arr[j], arr[j-1] = arr[j-1], arr[j]
    return arr


if __name__ == '__main__':
    a = [3, 56, 23, 14, 6, 36, 9, 77]
    print(boo(a))
    print(sel(a))
    print(fast(a))
    print(insert(a))
