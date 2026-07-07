n= int(input())
for x in range(n):
    for y in range(x+1):
        if y == 0 or x == n-1 or y == x:
            print("1",end=" ")
        else:
            print("0",end=" ")
    print() 