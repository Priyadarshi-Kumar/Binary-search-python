#binary search function
def binary_search(input_array, value):
    low = 0         #initially low index is 0
    high = len(test_list) - 1   #high index be the last index    
    while low<=high:
        mid = (low + high)/2       
        if test_list[mid]==value:
            return mid              #mid is equal to the test value return index
        elif test_list[mid] < value:
            low = mid + 1       #if the array mid value is less than test value increment mid index by 1
        else:
            high = mid - 1     #if the array mid value is more than test value decrement mid index by 1
    return -1    #if value not found return -1

#test list
test_list = [1,3,9,11,15,19,29]
test_val1 = 25
test_val2 = 15
print binary_search(test_list, test_val1)
print binary_search(test_list, test_val2)
