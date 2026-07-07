n = int(input())

for x in range(n):
    for z in range(x):
        print(" ",end=" ")
    for y in range(n-x):
        print("*",end=" ")
    
    print()

