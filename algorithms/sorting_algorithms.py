from heapq import merge

def insertion_sort(l):
    for i in range(1, len(l)):
        key = l[i]
        j = i - 1
        while j >= 0 and l[j] > key:
            l[j + 1] = l[j]
            j = j - 1
        l[j + 1] = key
    return l

def bubble_sort(l):
    for i in range(len(l)):
        for j in range(len(l) - i - 1):
            if l[j] > l[j + 1]:
                l[j], l[j + 1] = l[j + 1], l[j]
    return l

def merge_sort(l):
    if len(l) <= 1:
        return l
    mid = len(l) // 2
    left = merge_sort(l[:mid])
    right = merge_sort(l[mid:])
    return merge(left, right)

def selection_sort(l):
    for i in range(len(l)):
        min_index = i
        for j in range(i + 1, len(l)):
            if l[j] < l[min_index]:
                min_index = j
        l[i], l[min_index] = l[min_index], l[i]
    return l

def quick_sort(l):
    if len(l) <= 1:
        return l
    pivot = l[0]
    less = []
    greater = []
    for i in l[1:]:
        if i < pivot:
            less.append(i)
        else:
            greater.append(i)
    return quick_sort(less) + [pivot] + quick_sort(greater)