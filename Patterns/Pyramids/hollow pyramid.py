print("enter no. of rows:")

n = int(input())

for x in range(n):
    for y in range(n-x-1):
        print(" ",end=" ")
    for z in range(2*x+1):
        if x==n-1 or z==0 or z ==2*x:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()