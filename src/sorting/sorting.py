# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements

    i, j, k = 0, 0, 0

    while i < len(arrA) and j < len(arrB):
        #find the smallest when comparing 2 numbers from the 2 subarrays. Place the smallest in the merged_arr
        if arrA[i] < arrB[j]:
            merged_arr[k] = arrA[i]
            i+=1
        else:
            merged_arr[k] = arrB[j]
            j+=1
        k+=1
    
    #if items were left over in one of the subarrays, add them onto the end of the merged_arr
    while i < len(arrA):
        merged_arr[k] = arrA[i]
        i+=1
        k+=1
    while j < len(arrB):
        merged_arr[k] = arrB[j]
        j+=1
        k+=1

    return merged_arr

# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    # base case
    if len(arr) <= 1:
        return arr

    #else, divide array in half and sort the subarrays, then merge
    half = len(arr) // 2
    left = merge_sort(arr[:half])
    right = merge_sort(arr[half:])

    return merge(left, right)


# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
def merge_in_place(arr, start, mid, end):
    # Your code here
    pass


def merge_sort_in_place(arr, l, r):
    # Your code here
    pass