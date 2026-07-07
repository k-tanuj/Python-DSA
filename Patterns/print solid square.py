# Given an integer n, print a solid square pattern of size n × n using "* " (a star followed by exactly one space).

n = int(input())

for x in range(n):
    for y in range(n):
        print("*",end=" ")
    print()