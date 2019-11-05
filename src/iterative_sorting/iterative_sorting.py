# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index

        for j in range(i+1, len(arr)):
            if arr[smallest_index] > arr[j]:
                smallest_index = j

        curr_val = arr[cur_index] # save current value
        arr[cur_index] = arr[smallest_index]
        arr[smallest_index] = curr_val

    return arr

# print(selection_sort([4545,454,545,454,54,545,4]))


# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    swap = None
    for _ in range(0, len(arr) - 1):
        swap = False
        for j in range(0, len(arr) - 1):
            if arr[j+1] < arr[j]:
                curr_val = arr[j] #storing
                arr[j] = arr[j+1] #swap
                arr[j+1] = curr_val #swap
                swap = True
        if not swap:
            return arr
    return arr

# bubble_sort( [3,2,4,1] )
# bubble_sort( [10,21,44,1] )
# bubble_sort( [1, 5, 8, 4, 2, 9, 6, 0, 3, 7] )




# # STRETCH: implement the Count Sort function below
# def count_sort( arr, maximum=-1 ):

#     # return arr