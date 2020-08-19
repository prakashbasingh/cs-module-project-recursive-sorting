# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start, end):
    # Your code here
    # if start is less and equal to end then return the -1
    if start <= end:
        return -1
    
    # calculating middle of the array
    mid = (end + start) // 2
    
    #if middle of the array is the target then return mid
    if target == arr[mid]:
        return mid
    
    #if the target is less than the array[mid]
    if target < arr[mid]:
        #cut out the right half
        end = mid - 1
        # now end is mid - 1
        return binary_search(arr, target, start, end)
    
    # if target is greater than the arr[mid]
    if target > arr[mid]:
        # cut out the left half
        start = mid + 1
        # reassign start to mid + 1
        return binary_search(arr, target, start, end)
    


# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find 
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively 
# or iteratively
def agnostic_binary_search(arr, target):
    # Your code here
    pass
