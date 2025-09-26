from typing import List

#Bubble Sort
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr


#Insertion Sort
def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

#Merge Sort
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])
    return merge(left_half, right_half)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

#Quick Sort
def quick_sort(arr):
    def partition(low, high):
        pivot = arr[(low+high) // 2]
        i = low
        j = high
        while i <= j:
            while arr[i] < pivot:
                i += 1
            while arr[j] > pivot:
                j -= 1
            if i <= j:
                arr[i], arr[j] = arr[j], arr[i]
                i += 1
                j -= 1
        return i, j
    def sort(low, high):
        if low < high:
            i, j  = partition(low, high)
            sort(low, j)
            sort(i, high)
    sort(0, len(arr) - 1)
    return arr

#Heap Sort
def heap_sort(arr):
    def heapify(a, n, i):
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2
        if left < n and a[left] > a[largest]:
            largest = left
        if right < n and a[right] > a[largest]:
            largest = right
        if largest != i:
            a[i], a[largest] = a[largest], a[i]
            heapify(a, n, largest)
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    for end in range(n-1, 0, -1):
        arr[0], arr[end] = arr[end], arr[0]
        heapify(arr, end, 0)
    return arr

#counting sort
def counting_sort(arr):
    if not arr:
        return []
    min_val = min(arr)
    max_val = max(arr)
    k = max_val - min_val + 1
    count = [0] * k
    for num in arr:
        count[num - min_val] += 1
    output = []
    for i, freq in enumerate(count):
        value = i + min_val
        output.extend([value] * freq)
    return output


# Counting Sort
def counting_sort_by_digit(arr: List[int], exp: int, base: int = 10) -> None:
    n = len(arr)
    output = [0] * n
    count = [0] * base
    for num in arr:
        digit = (num // exp) % base
        count[digit] += 1
    for i in range(1, base):
        count[i] += count[i - 1]
    for i in range(n -1, -1, -1):
        digit = (arr[i] // exp) % base
        output[count[digit] - 1] = arr[i]
        count[digit] -= 1
    for i in range(n):
        arr[i] = output[i]

# Radix Sort
def radix_sort(arr: List[int], base: int = 10) -> List[int]:
    if not arr:
        return arr
    max_val = max(arr)
    exp = 1
    while max_val // exp > 0:
        counting_sort_by_digit(arr, exp, base)
        exp *= base
    return arr

def bucket_sort(arr: List[float]) -> List[float]:
    n = len(arr)
    if n == 0:
        return arr
    buckets: List[List[float]] = [[] for _ in range(n)]
    for x in arr:
        idx = int(n * x)
        if idx >= n:
            idx = n - 1
        buckets[idx].append(x)
    for b in buckets:
        b.sort()
    out: List[float] = []
    for b in buckets:
        out.extend(b)
    return out


#Quick Select
def partition(arr: List[int], low: int, high: int) -> int:
    pivot = arr[high]
    i = low
    for j in range(low, high):
        if arr[j] <= pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    arr[i], arr[high] = arr[high], arr[i]
    return i
def quick_select(arr: List[int], low: int, high: int, k: int) -> int:
    if low <= high:
        pi = partition(arr, low, high)
        if pi == k:
            return arr[pi]
        elif pi > k:
            return quick_select(arr, low, pi - 1, k)
        else:
            return quick_select(arr, pi + 1, high, k)