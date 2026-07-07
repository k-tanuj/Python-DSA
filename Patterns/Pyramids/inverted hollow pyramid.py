print("enter no. of rows:")

n = int(input())

for x in range(n):
    for y in range(x):
        print(" ",end=" ")
    for z in range(2*(n-x)-1):
        if x==0 or z==0 or z==2*(n-x)-2: 
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()