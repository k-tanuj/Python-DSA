# Right angled triangle left side alternating 1 0 pattern


for x in range(1,6):
    for y in range(x):
        
        #for Even values of y = 0,2,4
        if y%2 == 0:   
            print("1", end = " ")
            
        #for odd values of y = 1,3,5
        else:
            print("0", end = " ")
    print()