print("enter no. of rows:")

n = int(input())

for x in range(n):
    for y in range(n-x-1):
        print(" ",end=" ")
    for z in range(2*x+1):
        print("*",end=" ")
    print()