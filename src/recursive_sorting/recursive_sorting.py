# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements
    # TO-DO
    for i in range(0, len(merged_arr)):
        if len(arrA) == 0:
            merged_arr[i] = arrB.pop(0)
        elif len(arrB) == 0:
            merged_arr[i] = arrA.pop(0)
        elif arrA[0] < arrB[0]:
            merged_arr[i] = arrA.pop(0)
        else:
            merged_arr[i] = arrB.pop(0)

    return merged_arr

# print(merge([2,4,10], [3,6,8]))

# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # TO-DO
    if len(arr) > 1:
        # Do some stuff
        left = merge_sort(arr[:len(arr)//2])
        right = merge_sort(arr[len(arr)//2:])
        return merge(left, right)
    else:
        return arr

    return arr

# print(merge_sort([4,6,2]))

# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr
