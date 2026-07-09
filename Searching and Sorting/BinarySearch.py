def binarySearch(arr,target):
    start = 0 
    end = len(arr) - 1
    
    
    while start <= end:
        mid = (start + end)//2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            start = mid+1
        elif arr[mid] > target:
            end = mid - 1
    return -1







my_list = [10,15,20,25,30,35,40]
target = 40
print(binarySearch(my_list,target))
