def linear_Search(arr,target):

    size = len(arr)

    for i in range(0,size):
        if (arr[i]==target):
            return i
    return -1


my_list = [20,30,10,40,22]
target = 22

result = linear_Search(my_list,target)

print(result)