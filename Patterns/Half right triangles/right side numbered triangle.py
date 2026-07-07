n = int(input())

# code here
for x in range(n):
    number = 1
    for z in range(n-x-1):
        print(" ",end = " ")
    for y in range(x+1):
        print(number,end = " ")
        number+=1
    print()