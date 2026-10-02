# swap = True
#     print("BEFORE WHILE")
#     while swap:
#         print('ran while')
#         for i in range(0, len(arr) - 1):
#             print('ran for')
#             if arr[i+1] < arr[i]:
#                 print('less than')
#                 curr_val = arr[i] #storing
#                 print(arr, "before change")
#                 arr[i] = arr[i+1] #swap
#                 arr[i+1] = curr_val #swap
#                 swap = True
#                 print(arr, "after change", i)
#                 for j in range(0, len(arr) - 1):
#                     print("ran J for")
#                     if arr[j] < arr[j+1]:
#                         print("j less than", j)
#                         swap = False
#                     else:
#                         print("j else", j)
#                         print(arr, "before change (j)")
#                         curr_val = arr[j] #storing
#                         arr[j] = arr[j+1] #swap
#                         arr[j+1] = curr_val #swap
#                         print(arr, "after change (j)", j)
#                         swap = True
#             # else:
#             #     print("i else", i)
#             #     swap = False
#         # for j in range(0, len(arr) - 1):
#         #     print("ran J for")
#         #     if arr[j] < arr[j+1]:
#         #         print("j less than")
#         #         swap = False
#         #     else:
#                 # print("j else", j)
#                 # print(arr, "before change (j)")
#                 # curr_val = arr[j] #storing
#                 # arr[j] = arr[j+1] #swap
#                 # arr[j+1] = curr_val #swap
#                 # print(arr, "after change (j)", i)
#                 # swap = True


# swap = None
#     for i in range(0, len(arr) - 1):
#         print('ran for (i)')
#         swap = False
#         for j in range(0, len(arr) - 1):
#             print('ran for (j)')
#             if arr[i+1] < arr[i]:
#                 print('less than')
#                 curr_val = arr[i] #storing
#                 print(arr, "before change")
#                 arr[i] = arr[i+1] #swap
#                 arr[i+1] = curr_val #swap
#                 swap = True
#                 print(arr, "after change", j)
#         if not swap:
#             return


# def bubble_sort( arr ):
#     swap = None
#     for _ in range(0, len(arr) - 1):
#         # print('ran for (i)', _)
#         swap = False
#         for j in range(0, len(arr) - 1):
#             # print('ran for (j)')
#             if arr[j+1] < arr[j]:
#                 # print('less than')
#                 curr_val = arr[j] #storing
#                 # print(arr, "before change")
#                 arr[j] = arr[j+1] #swap
#                 arr[j+1] = curr_val #swap
#                 swap = True
#                 # print(arr, "after change", j)
#         if not swap:
#             # print("in the not swap -----------")
#             # return print(arr, "Returned from NOT swap")
#             return arr
#     # return print(arr, "final array")
#     return arr


#     ##### Recursion ########

def partition(l):
    left = []
    pivot = l[0]
    right = []

    for v in l[1:]:
        if v <= pivot:
            left.append(v)
        else:
            right.append(v)
    return left, pivot, right

def quicksort(l):
    if len(l) <= 1:
        return l

    left, pivot, right = partition(l)

    return quicksort(left) + [pivot] + quicksort(right)


data = [4,5,12,8]
print(quicksort(data))