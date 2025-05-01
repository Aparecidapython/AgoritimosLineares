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


lista = [20, 30, 70, 50, 10, 90, 40, 60,80]
print("Lista original:", lista)
bubble_sort(lista)
print("Lista ordenada:", lista)

