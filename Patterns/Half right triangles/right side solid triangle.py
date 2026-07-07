n = int(input())

for x in range(n):
    for y in range(n-x-1):
        print(" ",end=" ")
    for z in range(x+1):
        print("*",end=" ")
    print()