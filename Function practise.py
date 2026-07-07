#Celsius to Fahrenheit
def temp():
    print("enter the temp in celsius:")
    C = float(input())
    F = (C * 9/5) + 32
    print(f"temp in Fahrenheit is :{F}")

#temp()
    

#Area of a Rectangle
def Area():
    print("enter length:")
    l = float(input())
    print("enter breadth:")
    b = float(input())
    Area = l*b
    print(f'the area of rectangle is {Area}')

#Area()


#Distance covered by a Vehicle

def distance():
    print("enter speed in meter/second:")
    speed = float(input())
    print("enter time in seconds:")
    time = float(input())
    Distance = speed*time
    print(f"the distance covered by the vehicle is {Distance/1000} km") 

#distance()


#Number of Rounds of Lift
def rounds():
    print("what are the no. of people:")
    peoples = int(input())
    print("capacity of the lift: ")
    capacity = int(input())

    TotalRounds = (peoples+capacity-1)//capacity

    print(f"rounds: {TotalRounds}")

#rounds()

#Line Equation

def line():
    print("slope:")
    m= float(input())

    print("intercept:")
    c= float(input())

    print("value of x:")
    x= float(input())

    y = m*x + c

    print(f"eqn of line is : {y}")
line()



