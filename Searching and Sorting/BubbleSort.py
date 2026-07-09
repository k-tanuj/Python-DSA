def bubbleSort(arr):
    n= len(arr)

    for passes in range(0,n):
        for j in range(0,n-1-passes):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
    return arr 

unsorted_list = [5,4,7,3,2,6,1]
sorted_list = bubbleSort(unsorted_list)
print("Sorted elements:", sorted_list)