# Given an integer n, write a program to print the square of size n using "*" character. 
n = int(input())
for x in range(n):
    for y in range(n):
        if x == 0 or x== n-1 or y ==0 or y==n-1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()