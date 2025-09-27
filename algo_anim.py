

def bubble_sort_anim(arr):
    arr = arr.copy()
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
                yield arr[:]
        if not swapped:
            break
    yield arr[:]

def insertion_sort_anim(arr):
    arr = arr.copy()
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
            yield arr[:]
        arr[j + 1] = key
        yield arr[:]
    yield arr[:]

def merge_sort_anim(arr):
    arr = arr.copy()
    def merge_sort_rec(a, l, r):
        if r - l <= 1:
            return
        m = (l + r) // 2
        yield from merge_sort_rec(a, l, m)
        yield from merge_sort_rec(a, m, r)
        left, right = a[l:m], a[m:r]
        i = j = 0
        k = l
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                a[k] = left[i]
                i += 1
            else:
                a[k] = right[j]
                j += 1
            k += 1
            yield a[:]
        while i < len(left):
            a[k] = left[i]
            i += 1
            k += 1
            yield a[:]
        while j < len(right):
            a[k] = right[j]
            j += 1
            k += 1
            yield a[:]

    yield from merge_sort_rec(arr, 0, len(arr))
    yield arr[:]

def quick_sort_anim(arr):
    arr = arr.copy()
    def quicksort(l, r):
        if l >= r:
            return
        pivot = arr[(l + r) // 2]
        i, j = l, r
        while i <= j:
            while i <= j and arr[i] < pivot:
                i += 1
            while i <= j and arr[j] > pivot:
                j -= 1
            if i <= j:
                arr[i], arr[j] = arr[j], arr[i]
                yield arr[:]
                i += 1
                j -= 1
        yield from quicksort(l, j)
        yield from quicksort(i, r)
    yield from quicksort(0, len(arr) - 1)
    yield arr[:]

def heap_sort_anim(arr):
    arr = arr.copy()

    def heapify(n, i):
        largest = i
        l = 2 * i + 1
        r = 2 * i + 2
        if l < n and arr[l] > arr[largest]:
            largest = l
        if r < n and arr[r] > arr[largest]:
            largest = r
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            yield arr[:]
            yield from heapify(n, largest)

    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        yield from heapify(n, i)
    for end in range(n - 1, 0, -1):
        arr[0], arr[end] = arr[end], arr[0]
        yield arr[:]
        yield from heapify(end, 0)
    yield arr[:]

def counting_sort_anim(arr):
    arr = arr.copy()
    if not arr:
        return
    min_val, max_val = min(arr), max(arr)
    k = max_val - min_val + 1
    count = [0] * k
    for num in arr:
        count[num - min_val] += 1
    idx = 0
    for i, c in enumerate(count):
        for _ in range(c):
            arr[idx] = i + min_val
            idx += 1
            yield arr[:]
    yield arr[:]



def radix_sort_anim(arr, base=10):
    arr = arr.copy()
    if not arr:
        return

    def counting_sort_by_digit(exp):
        n = len(arr)
        output = [0] * n
        count = [0] * base
        for num in arr:
            digit = (num // exp) % base
            count[digit] += 1
        for i in range(1, base):
            count[i] += count[i - 1]
        i = n - 1
        while i >= 0:
            digit = (arr[i] // exp) % base
            output[count[digit] - 1] = arr[i]
            count[digit] -= 1
            i -= 1
        for i in range(n):
            arr[i] = output[i]
            yield arr[:]

    max_val = max(arr)
    exp = 1
    while max_val // exp > 0:
        yield from counting_sort_by_digit(exp)
        exp *= base
    yield arr[:]

def bucket_sort_anim(arr):
    arr = arr.copy()
    n = len(arr)
    if n == 0:
        return
    max_val = max(arr)
    buckets = [[] for _ in range(n)]
    for x in arr:
        idx = int(n * x / (max_val + 1))
        buckets[idx].append(x)
        flat = [item for b in buckets for item in b]
        yield flat.copy()
    out = []
    for b in buckets:
        b.sort()
        out.extend(b)
        yield out.copy()
    yield out

