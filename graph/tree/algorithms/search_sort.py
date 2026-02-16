# Linear Search

def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1


# Bubble Sort

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]


data = [64, 34, 25, 12, 22]

bubble_sort(data)
print("Sorted:", data)

print("Search 25 at index:", linear_search(data, 25))
