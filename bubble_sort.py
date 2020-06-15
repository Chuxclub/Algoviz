#!/usr/bin/env python3

def swap(arr, pos1, pos2):
    temp = arr[pos1]
    arr[pos1] = arr[pos2]
    arr[pos2] = temp

    return arr


def printarr(arr):

    str_res = []

    for i in range(len(arr)):
        str_res.append(str(arr[i]))

    print(" ".join(str_res))


def bubble_sort(arr):

    arr_len = len(arr)
    
    for i in range(arr_len):
        for j in range(arr_len-1-i):
            if(arr[j] > arr[j + 1]):
                swap = arr[j+1]
                arr[j+1] = arr[j]
                arr[j] = swap

    return arr

def bubble_sort(arr):

    arr_len = len(arr)
    
    for i in range(arr_len):
        for j in range(arr_len-1-i):
            if(arr[j] > arr[j + 1]):
                swap = arr[j+1]
                arr[j+1] = arr[j]
                arr[j] = swap

    return arr


def areListsEqual(arr1, arr2):

    if(len(arr1) != len(arr2)):
        return False

    for i in range(len(arr1)):
        if(arr1[i] != arr2[i]):
            return False

    return True


def bubble_sort_register(arr):

    arr_len = len(arr)
    res = []

    for i in range(arr_len):
        for j in range(arr_len-1-i):
            old_arr = arr.copy()

            if(arr[j] > arr[j + 1]):
                swap = arr[j+1]
                arr[j+1] = arr[j]
                arr[j] = swap

            if not(areListsEqual(old_arr, arr)) :
                res.append(arr.copy())

    return res


def bubble_sort_registerV2(arr):

    arr_len = len(arr)
    res = []

    for i in range(arr_len):
        for j in range(arr_len-1-i):

            if(arr[j] > arr[j + 1]):
                swap = arr[j+1]
                arr[j+1] = arr[j]
                arr[j] = swap

            res.append(arr.copy())

    return res

# test1 = [1, 2, 3, 4, 5]
# test2 = [5, 4, 3, 2, 1]
# test3 = [4, 3, 2, 1, 5]
# test4 = []

# printarr(bubble_sort(test1))
# printarr(bubble_sort(test2))
# printarr(bubble_sort(test3))
# printarr(bubble_sort(test4))
