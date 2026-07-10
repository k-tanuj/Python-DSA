def SelectionSort(arr):
    n= len(arr)

    for i in range(0,n-1):
        minIndex = i
        for j in range(i+1,n):

            if arr[minIndex]>arr[j]:
                minIndex = j
        
        arr[i], arr[minIndex] = arr[minIndex],arr[i]

    return arr 

unsorted_list = [12,25,11,34,90,22]
sorted_list = SelectionSort(unsorted_list)
print("Sorted elements:", sorted_list)