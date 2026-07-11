def InsertionSort(arr):
    n= len(arr)

    for current in range(1,n):
        current = arr[current]
        correctPosition = current - 1

        while correctPosition >= 0:
            if arr[correctPosition]>current:
                break
            else:
                arr[correctPosition + 1] = arr[correctPosition]
                correctPosition -= 1
        
        

    return arr 

unsorted_list = [12,25,11,34,90,22]
sorted_list = InsertionSort(unsorted_list)
print("Sorted elements:", sorted_list)